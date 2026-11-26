#!/usr/bin/env python3
# Append IDEA-052 (Smart Dryer Brem) and regenerate CSV/TXT/XLSX.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge_remote_ideation as m

rows = m.read_csv(m.REMOTE_CSV)
rows = [r for r in rows if r["IDEA-ID"] != "IDEA-052"]
rows.append({
    "IDEA-ID": "IDEA-052",
    "Tema": "Pangan / Pengeringan",
    "Judul": "Rancang Bangun Smart Dryer Brem Berbasis ESP32 dengan Pengendalian Suhu dan Monitoring Penurunan Massa untuk Menjaga Konsistensi Kadar Air Produk",
    "Status": "BLOCKED_PENDING_EVIDENCE",
    "Iterasi": "0/3",
    "Sync_State": "SYNCED",
    "Ref_Terkait": "Metode oven (AOAC/SNI, verifikasi); SNI brem (verifikasi)",
    "Konteks_Masalah_Kontribusi": "Pengeringan brem yang konsisten; kadar air memengaruhi tekstur, daya simpan, dan risiko jamur. Sistem mengendalikan suhu dan memantau penurunan massa untuk endpoint kadar air.",
    "Evidence_Log_Terkini": "Konsep teknis jelas; butuh baseline produsen (metode & variasi kadar air saat ini), spesifikasi produk (brem padat Madiun vs bentuk lain), dan akses oven untuk validasi.",
    "Unblock_Trigger_Reeval_Ref": "(1) Baseline kadar air & variasi produk dari produsen brem; (2) akses oven/AOAC untuk validasi; (3) definisi produk & target kadar air.",
})
rows.sort(key=lambda r: int(r["IDEA-ID"].split("-")[1]))
m.write_csv(rows)
m.write_txt(rows)
m.write_xlsx(rows)
print("Total:", len(rows))
print("Counts:", m.counts(rows))
