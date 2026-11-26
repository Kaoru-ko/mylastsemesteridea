#!/usr/bin/env python3
# Merge local 44-idea registry into the remote 6-idea ledger schema (10 columns).
# Run from repo root: python -I _tools/merge_remote_ideation.py
import csv, os, re, zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REMOTE_CSV = os.path.join(ROOT, "IDEATION_REPORT.csv")
LOCAL_CSV = os.path.join(ROOT, "_backup_local", "local_44.csv")
LOCAL_MEMORY = os.path.join(ROOT, "_backup_local", "local_MEMORY.md")
MEMORY = os.path.join(ROOT, "MEMORY.md")
MISTAKES = os.path.join(ROOT, "MISTAKES.md")

CONTEXT = {
    "IDEA-035": "Pengendalian suhu, kelembapan, dan sirkulasi ruang jamur tiram; evaporative cooling dibatasi wet-bulb.",
    "IDEA-036": "Verifikasi siklus sterilisasi autoklaf dengan F0 dan audit trail.",
    "IDEA-037": "Pemantauan kontinu kinerja fume hood (face velocity, posisi sash) untuk keselamatan lab.",
    "IDEA-038": "Pemantauan tekanan panas (WBGT) pekerja outdoor.",
    "IDEA-039": "Pemantauan dosis kebisingan kerja (Leq, LEX,8h).",
    "IDEA-040": "Peringatan dini hotspot silo gabah (suhu berlapis, RH, CO2).",
    "IDEA-041": "Pelacak kurva I-V panel surya portabel untuk deteksi shading/degradasi.",
    "IDEA-042": "Pemantauan oksigen terlarut (DO) kolam budidaya dengan kompensasi suhu.",
    "IDEA-043": "Dosing nutrisi hidroponik dengan kompensasi drift sensor EC/pH.",
    "IDEA-044": "Pemantauan kualitas udara dalam ruang dan kendali ventilasi (CO2, PM2.5, VOC).",
    "IDEA-045": "Irigasi presisi dengan kelembapan tanah terkalibrasi dan neraca air.",
    "IDEA-046": "Perangkap cahaya pintar untuk monitoring populasi hama dengan penghitungan citra.",
    "IDEA-047": "Pemantauan energi surya mandiri tegangan rendah (shunt, coulomb counting).",
    "IDEA-048": "Pengukuran kadar air gabah untuk petani kecil; gugur karena target adopter salah.",
    "IDEA-049": "Pemantauan iklim dan amonia kandang broiler dengan kendali ventilasi.",
    "IDEA-050": "Pemantauan suhu dan mutu susu di koperasi.",
    "IDEA-051": "Pemantauan sarang lebah/kelulut (berat, suhu, RH, suara).",
}

def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def short_titles():
    out = {}
    if not os.path.exists(LOCAL_MEMORY):
        return out
    for line in open(LOCAL_MEMORY, encoding="utf-8"):
        m = re.match(r"\| (IDEA-\d+) \| (.+?) \|", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out

def build():
    remote = read_csv(REMOTE_CSV)
    local = read_csv(LOCAL_CSV)
    rmap = {r["IDEA-ID"]: r for r in remote}
    lmap = {r["IDEA-ID"]: r for r in local}
    merged = []
    # preserve remote 001-006
    for rid in ["IDEA-001","IDEA-002","IDEA-003","IDEA-004","IDEA-005","IDEA-006"]:
        r = dict(rmap[rid])
        if rid == "IDEA-003":
            r["Status"] = "SUPERSEDED"
            r["Unblock_Trigger_Reeval_Ref"] = "Superseded-By: IDEA-034; ruang lingkup dikunci ke rantai dingin vaksin rutin 2-8 C."
        merged.append(r)
    # add local 013-051
    for rid in sorted(lmap, key=lambda x: int(x.split("-")[1])):
        n = int(rid.split("-")[1])
        if n < 13:
            continue
        l = lmap[rid]
        ctx = CONTEXT.get(rid, "Ide %s: %s." % (l["Tema"], l["Judul"]))
        if l["Status"] == "FAILED_ARCHIVED":
            trig = "Lihat %s" % l["Ref_Terkait"] if l["Ref_Terkait"].startswith("MISTAKE") else l["Kendala_Atau_Bukti"]
        else:
            trig = l["Kendala_Atau_Bukti"]
        merged.append({
            "IDEA-ID": l["IDEA-ID"], "Tema": l["Tema"], "Judul": l["Judul"],
            "Status": l["Status"], "Iterasi": l["Iterasi"], "Sync_State": l["Sync_State"],
            "Ref_Terkait": l["Ref_Terkait"], "Konteks_Masalah_Kontribusi": ctx,
            "Evidence_Log_Terkini": l["Kendala_Atau_Bukti"],
            "Unblock_Trigger_Reeval_Ref": trig,
        })
    merged.sort(key=lambda r: int(r["IDEA-ID"].split("-")[1]))
    return merged

def counts(rows):
    order = ["DRAFT","EVALUATING","PROVISIONAL_PASS","REVISING","BLOCKED_PENDING_EVIDENCE",
             "ON_HOLD","VALIDATED_ACTIVE","FAILED_ARCHIVED","SUPERSEDED"]
    c = {k:0 for k in order}
    for r in rows: c[r["Status"]] += 1
    return c

def write_csv(rows):
    cols = ["IDEA-ID","Tema","Judul","Status","Iterasi","Sync_State","Ref_Terkait",
            "Konteks_Masalah_Kontribusi","Evidence_Log_Terkini","Unblock_Trigger_Reeval_Ref"]
    with open(REMOTE_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)

def write_txt(rows):
    c = counts(rows)
    lines = ["="*80,
             "LAPORAN RINGKAS IDEASI TUGAS AKHIR (SYNCED WITH MEMORY.md & MISTAKES.md)",
             "Repositori : https://github.com/Kaoru-ko/mylastsemesteridea (Branch: IdeJudulTA)",
             "Tanggal    : 2026-11-26",
             "="*80, "",
             "1. RINGKASAN STATUS IDE",
             "   - Total Ide Terdaftar        : %d" % len(rows)]
    for k in ["FAILED_ARCHIVED","BLOCKED_PENDING_EVIDENCE","EVALUATING","REVISING","VALIDATED_ACTIVE","DRAFT","SUPERSEDED"]:
        ids = ", ".join(r["IDEA-ID"] for r in rows if r["Status"] == k)
        lines.append("   - %-26s : %d (%s)" % (k, c[k], ids))
    lines += ["", "-"*80, "2. DAFTAR SELURUH IDE (MEMORY.md)", "-"*80]
    for r in rows:
        lines.append("[%s] (%s) - Status: %s | Iterasi: %s | Sync: %s | Ref: %s" % (
            r["IDEA-ID"], r["Tema"], r["Status"], r["Iterasi"], r["Sync_State"], r["Ref_Terkait"]))
        lines.append("  Judul   : %s" % r["Judul"])
        lines.append("  Konteks : %s" % r["Konteks_Masalah_Kontribusi"])
        lines.append("  Bukti   : %s" % r["Evidence_Log_Terkini"])
        lines.append("  Syarat  : %s" % r["Unblock_Trigger_Reeval_Ref"])
        lines.append("")
    lines += ["-"*80, "3. ARSIP KEGAGALAN AKTIF (MISTAKES.md)", "-"*80,
              "[MISTAKE-001 -> IDEA-001] Kategori: PROBLEM_FAILURE (Arsip: 2026-11-25)",
              "  Ringkasan    : Pemantauan kualitas udara (CO2/partikel) dan ketidaknyamanan termal ruang kelas/praktikum ber-AC untuk mencegah mahasiswa mengantuk dan turun konsentrasi.",
              "  Akar Masalah : (1) Ruang kelas/laboratorium target umumnya sudah dilengkapi AC dan ventilasi sehingga urgensi intervensi lingkungan tidak terbukti mendesak; (2) Gejala mahasiswa mengantuk dipengaruhi banyak confounding factors.",
              "  Anti-Pattern : Jangan mengaitkan gejala psikologis/fisiologis umum (seperti mengantuk di kelas) secara langsung sebagai bukti kerusakan kualitas udara pada ruangan yang sudah ber-AC tanpa pengukuran baseline aktual.",
              "  Trigger      : Tersedia data pengukuran lapangan awal (baseline audit) pada ruang kelas/praktikum spesifik yang membuktikan kadar CO2 melampaui ambang batas kenyamanan (>1000 ppm) atau kegagalan termal berulang saat kelas terisi penuh meskipun AC/ventilasi beroperasi normal.",
              "",
              "[MISTAKE-002 -> IDEA-002] Kategori: SOLUTION_FAILURE (Arsip: 2026-11-25)",
              "  Ringkasan    : Alat bantu diagnosis kesalahan rangkaian dasar praktikum mikrokontroler (hubung singkat, salah polaritas/pin, loose connection) berbasis pengukuran tegangan dan kontinuitas.",
              "  Akar Masalah : Perangkat pembelajaran rangkaian dasar (kit edukasi tombol, balok magnetik, continuity tester) sudah banyak dijual dengan harga jauh lebih murah dan kualitas mapan tanpa diferensiasi teknis pada usulan.",
              "  Anti-Pattern : Jangan mengusulkan pembuatan alat bantu praktikum dasar yang fungsinya sudah terwakili oleh kit edukasi komersial murah tanpa mendefinisikan celah teknis spesifik yang gagal ditangani alat komersial tersebut.",
              "  Trigger      : Ditemukan celah diagnostik spesifik pada modul praktikum mikrokontroler tingkat lanjut (misalnya deteksi konflik bus komunikasi atau fault injection pin mikrokontroler secara otomatis) yang tidak tersedia pada alat komersial murah, disertai bukti kebutuhan dari dosen/laboran mata kuliah terkait.",
              "",
              "[MISTAKE-008 -> IDEA-048] Kategori: PROBLEM_FAILURE (Arsip: 2026-11-26)",
              "  Ringkasan    : Pengukuran kadar air gabah berbasis IoT untuk petani kecil.",
              "  Akar Masalah : Target adopter salah: petani kecil tidak punya anggaran, penjemuran gratis, dan alat tidak mengubah konstrain modal/tenaga kerja. Aspek SOLUTION_FAILURE: tidak ada diferensiasi yang mengalahkan metode gratis.",
              "  Anti-Pattern : Jangan mengusulkan alat yang harus dibeli pengguna akhir yang tidak punya anggaran dan tidak punya kewenangan tindak lanjut; bedakan pengguna (user) dari pembayar (payer).",
              "  Trigger      : Tersedia bukti dari koperasi/BUMDes/mill tentang kebutuhan pengukuran kadar air, anggaran, dan celah spesifik dibanding moisture meter komersial; atau model layanan bersama dengan willingness-to-pay terukur.",
              "", "="*80]
    open(os.path.join(ROOT, "IDEATION_REPORT.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

# --- XLSX minimal writer ---
def cell(ref, value, style=0):
    v = escape(str(value)); s = ' s="%d"' % style if style else ""
    return '<c r="%s" t="inlineStr"%s><is><t>%s</t></is></c>' % (ref, s, v)

def col(n):
    s = ""
    while n:
        n, r = divmod(n-1, 26); s = chr(65+r) + s
    return s

def sheet_xml(rows):
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
           '<cols><col min="1" max="1" width="12" customWidth="1"/><col min="2" max="2" width="26" customWidth="1"/>'
           '<col min="3" max="3" width="70" customWidth="1"/><col min="4" max="4" width="26" customWidth="1"/>'
           '<col min="5" max="5" width="8" customWidth="1"/><col min="6" max="6" width="12" customWidth="1"/>'
           '<col min="7" max="7" width="36" customWidth="1"/><col min="8" max="8" width="60" customWidth="1"/>'
           '<col min="9" max="9" width="70" customWidth="1"/><col min="10" max="10" width="60" customWidth="1"/></cols>',
           '<sheetData>']
    for i, row in enumerate(rows, 1):
        out.append('<row r="%d">' % i)
        for j, val in enumerate(row, 1):
            out.append(cell('%s%d' % (col(j), i), val, 1 if i == 1 else 0))
        out.append('</row>')
    out.append('</sheetData></worksheet>')
    return "".join(out)

def write_xlsx(rows):
    c = counts(rows)
    dash = [["LAPORAN STATUS IDEASI TUGAS AKHIR (BRANCH: IdeJudulTA)"],
            ["Tanggal Sinkronisasi", "2026-11-26"],
            ["Repositori", "Kaoru-ko/mylastsemesteridea"],
            ["Catatan", "KEEP adalah status kerja; enum resmi mengikuti SETUPS.md."],
            [],
            ["Status Resmi", "Jumlah Ide"]]
    for k in ["DRAFT","EVALUATING","PROVISIONAL_PASS","REVISING","BLOCKED_PENDING_EVIDENCE","ON_HOLD","VALIDATED_ACTIVE","FAILED_ARCHIVED","SUPERSEDED"]:
        dash.append([k, c[k]])
    dash.append(["TOTAL IDE TERDAFTAR", len(rows)])
    idea = [["IDEA-ID","Tema","Judul","Status","Iterasi","Sync_State","Ref Terkait","Konteks Masalah & Kontribusi","Evidence_Log Terkini","Unblock_Trigger / Re-eval_Ref"]]
    for r in rows:
        idea.append([r["IDEA-ID"],r["Tema"],r["Judul"],r["Status"],r["Iterasi"],r["Sync_State"],r["Ref_Terkait"],r["Konteks_Masalah_Kontribusi"],r["Evidence_Log_Terkini"],r["Unblock_Trigger_Reeval_Ref"]])
    mistakes = [["MISTAKE-ID","IDEA-ID","Tanggal Arsip","Status Sebelum Gagal","Kategori Kegagalan","Ringkasan Ide","Akar Masalah & Bukti Penggugur","Anti-Pattern (Larangan bagi Agen)","Re-evaluation Trigger"],
        ["MISTAKE-001","IDEA-001","2026-11-25","EVALUATING","PROBLEM_FAILURE","Pemantauan kualitas udara & termal ruang kelas ber-AC untuk mencegah kantuk mahasiswa.","Banyak confounding factors dan ketiadaan baseline aktual.","Jangan mengaitkan gejala psikologis umum dengan kualitas udara tanpa baseline.","Tersedia baseline lapangan yang membuktikan CO2 >1000 ppm atau kegagalan termal berulang."],
        ["MISTAKE-002","IDEA-002","2026-11-25","EVALUATING","SOLUTION_FAILURE","Alat bantu diagnosis kesalahan rangkaian dasar praktikum mikrokontroler.","Kalah bersaing dengan kit edukasi murah tanpa diferensiasi kuat.","Jangan mengusulkan alat bantu praktikum dasar tanpa celah teknis spesifik.","Ditemukan celah diagnostik tingkat lanjut + bukti kebutuhan dosen/laboran."],
        ["MISTAKE-008","IDEA-048","2026-11-26","EVALUATING","PROBLEM_FAILURE","Pengukuran kadar air gabah berbasis IoT untuk petani kecil.","Target adopter salah: petani kecil tidak punya anggaran, penjemuran gratis, dan alat tidak mengubah konstrain modal/tenaga kerja.","Bedakan pengguna (user) dari pembayar (payer); jangan mengusulkan alat untuk pengguna tanpa anggaran/kewenangan.","Ada bukti dari koperasi/BUMDes/mill tentang kebutuhan, anggaran, dan celah vs moisture meter komersial."]]
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>'''
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''
    wb = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets><sheet name="Dashboard" sheetId="1" r:id="rId1"/><sheet name="Daftar Ide" sheetId="2" r:id="rId2"/><sheet name="Arsip Kegagalan" sheetId="3" r:id="rId3"/></sheets></workbook>'''
    wbrels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font></fonts>
<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/></cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>'''
    with zipfile.ZipFile(os.path.join(ROOT, "IDEATION_REPORT.xlsx"), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", wb)
        z.writestr("xl/_rels/workbook.xml.rels", wbrels)
        z.writestr("xl/styles.xml", styles)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml(dash))
        z.writestr("xl/worksheets/sheet2.xml", sheet_xml(idea))
        z.writestr("xl/worksheets/sheet3.xml", sheet_xml(mistakes))

def update_memory(rows):
    text = open(MEMORY, encoding="utf-8").read()
    st = short_titles()
    header = ("| IDEA-ID | Tema & Judul Singkat | Status | Iterasi | Sync_State | Ref Terkait |\n"
              "| ------ | ------ | ------ | ------ | ------ | ------ |\n")
    table = header
    for r in rows:
        short = st.get(r["IDEA-ID"])
        if not short:
            short = "[%s] %s" % (r["Tema"], r["Judul"])
        table += "| %s | %s | %s | %s | %s | %s |\n" % (
            r["IDEA-ID"], short, r["Status"], r["Iterasi"], r["Sync_State"], r["Ref_Terkait"])
    start = text.index("| IDEA-ID |")
    end = text.index("\n\n---", start)
    text = text[:start] + table.rstrip() + text[end:]
    # update IDEA-003 ledger
    s = text.index("##### IDEA-003")
    e = text.index("\n\n---", s)
    block = text[s:e]
    lines = block.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("* **Status:**"):
            lines[i] = "* **Status:** SUPERSEDED"
        elif line.startswith("* **Unblock_Trigger / Re-eval_Ref:**"):
            lines[i] = "* **Unblock_Trigger / Re-eval_Ref:** Superseded-By: IDEA-034; ruang lingkup dikunci ke rantai dingin vaksin rutin 2-8 C."
        elif line.startswith("* **Mistake_Ref:**"):
            lines.insert(i, "* **Evidence_Log:**\n  * [Iterasi 0 - SUPERSEDED]: Ruang lingkup dikunci ke IDEA-034 (rantai dingin vaksin rutin 2-8 C).")
            break
    text = text[:s] + "\n".join(lines) + text[e:]
    # append session notes
    notes = """

---

#### 3. Catatan Sesi 2026-11-26
* **Total registry:** 45 ide (001-006 dari remote + 013-051 dari pembaruan lokal). ID 007-012 tidak dipakai (gap historis).
* **Tiga judul KEEP:** jamur tiram = `IDEA-035`; kualitas daya = revisi `IDEA-027`; filamen = revisi `IDEA-019`.
* **Revisi:** `IDEA-019` dan `IDEA-027` -> `REVISING` 1/3 dengan catatan teknis (ASTM D6980 bukan Tg; ADC internal ESP32 tidak memadai).
* **Kandidat baru:** `IDEA-035`-`IDEA-047` dan `IDEA-049`-`IDEA-051`; status `BLOCKED_PENDING_EVIDENCE` atau `EVALUATING` sesuai akses. `IDEA-048` -> `FAILED_ARCHIVED` (`MISTAKE-008`).
* **Legacy:** `IDEA-013/020/028` dan `MISTAKE-005/006/007` ditandai legacy tanpa data; tidak dipakai sebagai bukti aktif; digantikan oleh `IDEA-049/050/051`.
* **Catatan bukti:** standar bertanda `(verifikasi)` belum diverifikasi edisinya; tidak ada DOI baru yang dikarang. Hitungan psikrometri, F0, propagasi error, dan resolusi gravimetri adalah hitungan sendiri dan dapat direproduksi.
"""
    text = text.rstrip() + notes + "\n"
    open(MEMORY, "w", encoding="utf-8").write(text)

def update_mistakes():
    text = open(MISTAKES, encoding="utf-8").read().rstrip()
    add = """

#### 5. Catatan Legacy
* **MISTAKE-005 (`IDEA-013`), MISTAKE-006 (`IDEA-020`), MISTAKE-007 (`IDEA-028`):** Arsip legacy tanpa kategori/trigger; tidak dipakai sebagai bukti aktif dan tidak dihapus agar riwayat tetap utuh. Digantikan oleh `IDEA-049/050/051`.

##### MISTAKE-008
* **IDEA-ID:** IDEA-048
* **Tanggal Arsip:** 2026-11-26
* **Status Sebelum Gagal:** EVALUATING
* **Kategori Kegagalan:** PROBLEM_FAILURE
* **Ringkasan Ide:** Pengukuran kadar air gabah berbasis IoT untuk petani kecil.
* **Akar Masalah & Bukti Penggugur:** Target adopter salah: petani kecil tidak punya anggaran, penjemuran gratis, dan alat tidak mengubah konstrain modal/tenaga kerja. Aspek `SOLUTION_FAILURE`: tidak ada diferensiasi yang mengalahkan metode gratis.
* **Anti-Pattern (Larangan bagi Agen):** Jangan mengusulkan alat yang harus dibeli pengguna akhir yang tidak punya anggaran dan tidak punya kewenangan tindak lanjut; bedakan pengguna (*user*) dari pembayar (*payer*).
* **Re-evaluation Trigger (Syarat Objektif Pembuka Kunci):** Tersedia bukti dari koperasi/BUMDes/mill tentang kebutuhan pengukuran kadar air, anggaran, dan celah spesifik dibanding moisture meter komersial; atau model layanan bersama dengan *willingness-to-pay* terukur.
"""
    open(MISTAKES, "w", encoding="utf-8").write(text + add + "\n")

if __name__ == "__main__":
    rows = build()
    write_csv(rows)
    write_txt(rows)
    write_xlsx(rows)
    update_memory(rows)
    update_mistakes()
    print("Merged ideas:", len(rows))
    print("Counts:", counts(rows))
