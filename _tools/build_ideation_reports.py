#!/usr/bin/env python3
# Build consistent IDEATION_REPORT.csv/.txt/.xlsx from the current registry.
# Run with: python -I _tools/build_ideation_reports.py
import csv, os, shutil, zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_DIR = os.path.join(ROOT, "IDEATION_REPORT", "csv")
TXT_DIR = os.path.join(ROOT, "IDEATION_REPORT", "txt")
XLSX_DIR = os.path.join(ROOT, "IDEATION_REPORT", "xlsx")

BASE = os.path.join(CSV_DIR, "IDEATION_REPORT03.csv")

# ---------- data ----------
def read_base():
    with open(BASE, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def update_existing(rows):
    for r in rows:
        if r["IDEA-ID"] == "IDEA-019":
            r["Status"] = "REVISING"
            r["Iterasi"] = "1/3"
            r["Ref_Terkait"] = "ASTM D6980 (kadar air), ASTM D3418/E1356 (Tg), ASTM D638"
            r["Kendala_Atau_Bukti"] = ("Re-evaluasi 2026-11-26: ASTM D6980 adalah kadar air by loss in weight, bukan Tg; "
                "Tg memerlukan DSC (ASTM D3418/E1356). Pemanasan 50 C pada ambient 30 C/70% RH hanya mencapai ~25,5% RH; "
                "dehumidifikasi wajib. Gravimetri 1 kg butuh resolusi 0,1 g untuk 0,01%.")
        if r["IDEA-ID"] == "IDEA-027":
            r["Status"] = "REVISING"
            r["Iterasi"] = "1/3"
            r["Ref_Terkait"] = "IEC 61000-4-30, NEMA MG 1, IEEE 1159"
            r["Kendala_Atau_Bukti"] = ("Re-evaluasi 2026-11-26: ADC internal ESP32 tidak memadai; perlu sensor/IC energi eksternal; "
                "deklarasikan kelas (S, bukan A); keselamatan panel wajib.")
        if r["IDEA-ID"] == "IDEA-013":
            r["Kendala_Atau_Bukti"] = "Legacy placeholder tanpa data; tidak dipakai sebagai bukti aktif. Digantikan oleh IDEA-049."
        if r["IDEA-ID"] == "IDEA-020":
            r["Kendala_Atau_Bukti"] = "Legacy placeholder tanpa data; tidak dipakai sebagai bukti aktif. Digantikan oleh IDEA-050."
        if r["IDEA-ID"] == "IDEA-028":
            r["Kendala_Atau_Bukti"] = "Legacy placeholder tanpa data; tidak dipakai sebagai bukti aktif. Digantikan oleh IDEA-051."
    return rows

NEW = [
    dict(id="IDEA-035", tema="Agrikultur / Jamur",
         judul="Pengendalian Suhu, Kelembapan & Sirkulasi Ruang Jamur Tiram Berbasis Evaporative Cooling dan Ventilasi Adaptif",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="Literatur budidaya; ISO 7726 (verifikasi)",
         note="Evaluasi teknis selesai; wet-bulb limit 2-5 C. Butuh baseline suhu/RH lokasi dan penetapan strain (P. ostreatus vs strain tropis)."),
    dict(id="IDEA-036", tema="Kesehatan / Sterilisasi",
         judul="Verifikasi Siklus Sterilisasi Autoklaf Berbasis IoT dengan Perhitungan F0 dan Audit Trail",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="ISO 17665-1, ISO 11140-1 (verifikasi)",
         note="Butuh akses autoklaf, indikator biologis/kimia, dan penempatan sensor. Contoh F0: 115 C/30 min = 7,54 min; 121 C/15 min = 15 min."),
    dict(id="IDEA-037", tema="Keselamatan Lab / Aliran",
         judul="Pemantauan Kinerja Lemari Asam (Fume Hood) Berbasis IoT Menggunakan Face Velocity dan Posisi Sash",
         status="EVALUATING", it="0/3", ref="ASHRAE 110, EN 14175 (verifikasi)",
         note="Butuh anemometer terkalibrasi dan uji tracer gas; face velocity bukan jaminan containment."),
    dict(id="IDEA-038", tema="K3 / Tekanan Panas",
         judul="Pemantauan Tekanan Panas (WBGT) Pekerja Outdoor Berbasis IoT dengan Validasi WBGT Meter Referensi",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="ISO 7243, ISO 7726 (verifikasi)",
         note="Butuh WBGT meter referensi; perawatan wet bulb dan time constant globe."),
    dict(id="IDEA-039", tema="K3 / Kebisingan",
         judul="Pemantauan Dosis Kebisingan Kerja Berbasis IoT dengan Validasi Sound Level Meter",
         status="EVALUATING", it="0/3", ref="IEC 61672-1, ISO 9612, Permenaker 5/2018 (verifikasi)",
         note="Butuh SLM kelas 1/2 dan acoustic calibrator; wind noise dan body shielding."),
    dict(id="IDEA-040", tema="Pascapanen / Silo",
         judul="Peringatan Dini Hotspot pada Silo Gabah Berbasis IoT Menggunakan Suhu Berlapis, RH, dan CO2",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="SNI 0224:2022, SNI 6128:2020 (verifikasi)",
         note="Butuh akses silo dan kalibrasi CO2; payer adalah operator silo/mill, bukan petani."),
    dict(id="IDEA-041", tema="Energi / PV",
         judul="Pelacak Kurva I-V Panel Surya Portabel Berbasis IoT untuk Deteksi Shading dan Degradasi",
         status="EVALUATING", it="0/3", ref="IEC 60904, IEC 61724-1 (verifikasi)",
         note="Butuh I-V tracer referensi/pyranometer; keselamatan DC dan koreksi iradiansi."),
    dict(id="IDEA-042", tema="Akuakultur / DO",
         judul="Pemantauan Oksigen Terlarut (DO) Kolam Budidaya Berbasis IoT dengan Kompensasi Suhu dan Validasi Winkler",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="ISO 5814 (verifikasi)",
         note="Butuh akses kolam dan sensor DO; biofouling dan kalibrasi."),
    dict(id="IDEA-043", tema="Agrikultur / Hidroponik",
         judul="Dosing Nutrisi Hidroponik Berbasis IoT dengan Kompensasi Drift Sensor EC/pH dan Validasi Laboratorium",
         status="EVALUATING", it="0/3", ref="ISO 7888 (EC) (verifikasi)",
         note="Butuh EC/pH meter lab; drift/biofouling dan kalibrasi pompa peristaltik."),
    dict(id="IDEA-044", tema="Bangunan / IAQ",
         judul="Pemantauan Kualitas Udara Dalam Ruang dan Kendali Ventilasi Berbasis IoT (CO2, PM2.5, VOC)",
         status="EVALUATING", it="0/3", ref="ASHRAE 62.1 (verifikasi)",
         note="Butuh reference monitor; fokus pada ventilasi, bukan klaim kesehatan."),
    dict(id="IDEA-045", tema="Agrikultur / Irigasi",
         judul="Irigasi Presisi Berbasis IoT Menggunakan Kelembapan Tanah Terkalibrasi dan Neraca Air",
         status="EVALUATING", it="0/3", ref="FAO 56, ISO 11274 (verifikasi)",
         note="Butuh kalibrasi gravimetrik per tekstur tanah; daya valve 12 V."),
    dict(id="IDEA-046", tema="Agrikultur / Hama",
         judul="Perangkap Cahaya Pintar Berbasis IoT untuk Monitoring Populasi Hama dengan Penghitungan Citra",
         status="EVALUATING", it="0/3", ref="Pedoman IPM (verifikasi)",
         note="Butuh hitung manual sebagai ground truth; pencahayaan malam dan image processing."),
    dict(id="IDEA-047", tema="Energi / DC",
         judul="Pemantauan Energi Sistem Surya Mandiri Tegangan Rendah Berbasis IoT Menggunakan Shunt dan Coulomb Counting",
         status="EVALUATING", it="0/3", ref="IEC 61724-1 (verifikasi)",
         note="Butuh multimeter referensi; resolusi shunt 0,75 mV pada 0,5 A; keselamatan baterai."),
    dict(id="IDEA-048", tema="Pascapanen / Gabah",
         judul="Pengukuran Kadar Air Gabah Berbasis IoT untuk Petani Kecil",
         status="FAILED_ARCHIVED", it="0/3", ref="MISTAKE-008",
         note="Gugur pada PROBLEM_FAILURE: target adopter salah; penjemuran gratis; petani kecil tidak punya anggaran/kewenangan tindak lanjut."),
    dict(id="IDEA-049", tema="Peternakan / Kandang",
         judul="Pemantauan Iklim dan Amonia Kandang Ayam Broiler Berbasis IoT dengan Kendali Ventilasi",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="Pedoman peternakan; THI (verifikasi)",
         note="Butuh akses kandang dan kalibrasi sensor NH3; fokus pada ventilasi dan THI, bukan klaim produksi."),
    dict(id="IDEA-050", tema="Peternakan / Susu",
         judul="Pemantauan Suhu dan Mutu Susu di Koperasi Berbasis IoT dengan Validasi Laboratorium",
         status="EVALUATING", it="0/3", ref="SNI susu segar (verifikasi)",
         note="Butuh akses KUD dan uji lab pH/MBRT; sensor harus food-grade dan mudah dibersihkan."),
    dict(id="IDEA-051", tema="Agrikultur / Lebah",
         judul="Pemantauan Sarang Lebah/Kelulut Berbasis IoT Menggunakan Berat, Suhu, RH, dan Suara",
         status="BLOCKED_PENDING_EVIDENCE", it="0/3", ref="Pedoman budidaya lebah (verifikasi)",
         note="Butuh akses sarang dan baseline; load cell 50 kg resolusi 10 g; jangan mengganggu koloni."),
]

def all_rows():
    rows = update_existing(read_base())
    for n in NEW:
        rows.append(dict(**{"IDEA-ID": n["id"], "Tema": n["tema"], "Judul": n["judul"],
                            "Status": n["status"], "Iterasi": n["it"], "Sync_State": "SYNCED",
                            "Ref_Terkait": n["ref"], "Kendala_Atau_Bukti": n["note"]}))
    rows.sort(key=lambda r: int(r["IDEA-ID"].split("-")[1]))
    return rows

def counts(rows):
    order = ["DRAFT","EVALUATING","PROVISIONAL_PASS","REVISING","BLOCKED_PENDING_EVIDENCE",
             "ON_HOLD","VALIDATED_ACTIVE","FAILED_ARCHIVED","SUPERSEDED"]
    c = {k:0 for k in order}
    for r in rows: c[r["Status"]] += 1
    return c

# ---------- CSV ----------
def write_csv(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["IDEA-ID","Tema","Judul","Status","Iterasi","Sync_State","Ref_Terkait","Kendala_Atau_Bukti"])
        w.writeheader(); w.writerows(rows)

# ---------- TXT ----------
def write_txt(path, rows):
    c = counts(rows)
    lines = []
    lines.append("LAPORAN IDEASI TUGAS AKHIR (BRANCH: IdeJudulTA)")
    lines.append("=" * 48)
    lines.append("Tanggal Sinkronisasi: 2026-11-26")
    lines.append("Total IDEA-ID Tercatat: %d" % len(rows))
    lines.append("")
    for k in ["BLOCKED_PENDING_EVIDENCE","EVALUATING","FAILED_ARCHIVED","DRAFT","REVISING","SUPERSEDED","VALIDATED_ACTIVE"]:
        lines.append("- %s: %d" % (k, c[k]))
    lines.append("")
    lines.append("DAFTAR IDEA-ID:")
    for r in rows:
        lines.append("[%s] (%s) %s | Ref: %s | Catatan: %s" % (r["IDEA-ID"], r["Status"], r["Judul"], r["Ref_Terkait"], r["Kendala_Atau_Bukti"]))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

# ---------- XLSX ----------
def cell(ref, value, style=0):
    v = escape(str(value))
    s = ' s="%d"' % style if style else ""
    return '<c r="%s" t="inlineStr"%s><is><t>%s</t></is></c>' % (ref, s, v)

def col(n):
    s = ""
    while n:
        n, r = divmod(n-1, 26)
        s = chr(65+r) + s
    return s

def sheet_xml(rows):
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
           '<cols><col min="1" max="1" width="12" customWidth="1"/><col min="2" max="2" width="26" customWidth="1"/>'
           '<col min="3" max="3" width="70" customWidth="1"/><col min="4" max="4" width="26" customWidth="1"/>'
           '<col min="5" max="5" width="8" customWidth="1"/><col min="6" max="6" width="12" customWidth="1"/>'
           '<col min="7" max="7" width="40" customWidth="1"/><col min="8" max="8" width="70" customWidth="1"/></cols>',
           '<sheetData>']
    for i, row in enumerate(rows, 1):
        out.append('<row r="%d">' % i)
        for j, val in enumerate(row, 1):
            out.append(cell('%s%d' % (col(j), i), val, 1 if i == 1 else 0))
        out.append('</row>')
    out.append('</sheetData></worksheet>')
    return "".join(out)

def write_xlsx(path, idea_rows):
    c = counts(idea_rows)
    dash = [["LAPORAN STATUS IDEASI TUGAS AKHIR (BRANCH: IdeJudulTA)"],
            ["Tanggal Sinkronisasi", "2026-11-26"],
            ["Repositori", "Kaoru-ko/mylastsemesteridea"],
            ["Catatan", "KEEP adalah status kerja; enum resmi mengikuti SETUPS.md."],
            [],
            ["Status Resmi", "Jumlah Ide"]]
    for k in ["DRAFT","EVALUATING","PROVISIONAL_PASS","REVISING","BLOCKED_PENDING_EVIDENCE","ON_HOLD","VALIDATED_ACTIVE","FAILED_ARCHIVED","SUPERSEDED"]:
        dash.append([k, c[k]])
    dash.append(["TOTAL IDE TERDAFTAR", len(idea_rows)])

    idea = [["IDEA-ID","Tema","Judul","Status","Iterasi","Sync_State","Ref Terkait","Kendala / Bukti"]]
    for r in idea_rows:
        idea.append([r["IDEA-ID"],r["Tema"],r["Judul"],r["Status"],r["Iterasi"],r["Sync_State"],r["Ref_Terkait"],r["Kendala_Atau_Bukti"]])

    mistakes = [["MISTAKE-ID","IDEA-ID","Tanggal Arsip","Status Sebelum Gagal","Kategori Kegagalan","Ringkasan Ide","Akar Masalah & Bukti Penggugur","Anti-Pattern","Re-evaluation Trigger"],
        ["MISTAKE-001","IDEA-001","2026-11-25","EVALUATING","PROBLEM_FAILURE","Pemantauan kualitas udara & termal ruang kelas ber-AC untuk mencegah kantuk mahasiswa.","Banyak confounding factors dan ketiadaan baseline aktual.","Jangan mengaitkan gejala psikologis umum dengan kualitas udara tanpa baseline.","Tersedia baseline lapangan yang membuktikan CO2 >1000 ppm atau kegagalan termal berulang."],
        ["MISTAKE-002","IDEA-002","2026-11-25","EVALUATING","SOLUTION_FAILURE","Alat bantu diagnosis kesalahan rangkaian dasar praktikum mikrokontroler.","Kalah bersaing dengan kit edukasi murah tanpa diferensiasi kuat.","Jangan mengusulkan alat bantu praktikum dasar tanpa celah teknis spesifik.","Ditemukan celah diagnostik tingkat lanjut + bukti kebutuhan dosen/laboran."],
        ["MISTAKE-005","IDEA-013","Tidak tersedia","FAILED_ARCHIVED","Legacy","Arsip legacy tanpa data.","Tidak dipakai sebagai bukti aktif; digantikan IDEA-049.","Tidak tersedia.","Tidak tersedia."],
        ["MISTAKE-006","IDEA-020","Tidak tersedia","FAILED_ARCHIVED","Legacy","Arsip legacy tanpa data.","Tidak dipakai sebagai bukti aktif; digantikan IDEA-050.","Tidak tersedia.","Tidak tersedia."],
        ["MISTAKE-007","IDEA-028","Tidak tersedia","FAILED_ARCHIVED","Legacy","Arsip legacy tanpa data.","Tidak dipakai sebagai bukti aktif; digantikan IDEA-051.","Tidak tersedia.","Tidak tersedia."],
        ["MISTAKE-008","IDEA-048","2026-11-26","EVALUATING","PROBLEM_FAILURE","Pengukuran kadar air gabah berbasis IoT untuk petani kecil.","Target adopter salah: petani kecil tidak punya anggaran, penjemuran gratis, dan alat tidak mengubah konstrain modal/tenaga kerja.","Bedakan pengguna (user) dari pembayar (payer); jangan mengusulkan alat untuk pengguna tanpa anggaran/kewenangan.","Ada bukti dari koperasi/BUMDes/mill tentang kebutuhan, anggaran, dan celah vs moisture meter komersial."],
    ]

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
<sheets>
<sheet name="Dashboard" sheetId="1" r:id="rId1"/>
<sheet name="Daftar Ide" sheetId="2" r:id="rId2"/>
<sheet name="Arsip Kegagalan" sheetId="3" r:id="rId3"/>
</sheets></workbook>'''
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

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", wb)
        z.writestr("xl/_rels/workbook.xml.rels", wbrels)
        z.writestr("xl/styles.xml", styles)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml(dash))
        z.writestr("xl/worksheets/sheet2.xml", sheet_xml(idea))
        z.writestr("xl/worksheets/sheet3.xml", sheet_xml(mistakes))

# ---------- main ----------
if __name__ == "__main__":
    rows = all_rows()
    # backup old canonical files (only once)
    for src, dst in [
        (os.path.join(CSV_DIR, "IDEATION_REPORT.csv"), os.path.join(CSV_DIR, "IDEATION_REPORT_legacy_2026-11-24.csv")),
        (os.path.join(XLSX_DIR, "IDEATION_REPORT.xlsx"), os.path.join(XLSX_DIR, "IDEATION_REPORT_legacy_2026-11-24.xlsx")),
    ]:
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
    # new versioned + canonical
    write_csv(os.path.join(CSV_DIR, "IDEATION_REPORT04.csv"), rows)
    write_csv(os.path.join(CSV_DIR, "IDEATION_REPORT.csv"), rows)
    write_txt(os.path.join(TXT_DIR, "IDEATION_REPORT004.txt"), rows)
    write_txt(os.path.join(TXT_DIR, "IDEATION_REPORT.txt"), rows)
    write_xlsx(os.path.join(XLSX_DIR, "IDEATION_REPORT005.xlsx"), rows)
    write_xlsx(os.path.join(XLSX_DIR, "IDEATION_REPORT.xlsx"), rows)
    print("Wrote %d ideas." % len(rows))
    print("Counts:", counts(rows))
