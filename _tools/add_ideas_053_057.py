#!/usr/bin/env python3
# Append IDEA-053..057 (five mature IoT candidates) and regenerate reports.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge_remote_ideation as m

NEW = [
    {
        "IDEA-ID": "IDEA-053",
        "Tema": "Pertanian / Benih",
        "Judul": "Rancang Bangun Smart Seed Germination Chamber Berbasis ESP32 dengan Pengendalian Suhu, RH, dan Fotoperiod untuk Meningkatkan Konsistensi Daya Berkecambah",
        "Status": "EVALUATING",
        "Iterasi": "0/3",
        "Sync_State": "SYNCED",
        "Ref_Terkait": "Uji germinasi ISTA (verifikasi); SNI benih (verifikasi)",
        "Konteks_Masalah_Kontribusi": "Pengujian daya berkecambah yang konsisten; chamber mengendalikan suhu, RH, dan fotoperiod.",
        "Evidence_Log_Terkini": "Konsep matang; butuh akses laboratorium benih/germinator standar dan lot benih untuk validasi.",
        "Unblock_Trigger_Reeval_Ref": "(1) Akses lab benih/germinator; (2) lot benih dengan viabilitas diketahui; (3) protokol ISTA/SNI.",
    },
    {
        "IDEA-ID": "IDEA-054",
        "Tema": "Pascapanen / Cold Storage",
        "Judul": "Rancang Bangun Smart Monitoring Cold Storage Sayur Berbasis ESP32 dengan Sensor Suhu, RH, dan CO2 untuk Menekan Susut Berat dan Memperpanjang Daya Simpan",
        "Status": "EVALUATING",
        "Iterasi": "0/3",
        "Sync_State": "SYNCED",
        "Ref_Terkait": "Pedoman penyimpanan sayur (verifikasi); logger terkalibrasi",
        "Konteks_Masalah_Kontribusi": "Fluktuasi suhu/RH mempercepat susut berat dan pembusukan sayur; monitoring kontinu + alarm.",
        "Evidence_Log_Terkini": "Konsep matang; butuh akses cold storage dan batch sayur untuk uji susut berat/daya simpan.",
        "Unblock_Trigger_Reeval_Ref": "(1) Akses cold storage; (2) batch sayur homogen; (3) timbangan & logger referensi.",
    },
    {
        "IDEA-ID": "IDEA-055",
        "Tema": "Akuakultur / Pakan",
        "Judul": "Rancang Bangun Smart Fish Feed Dispenser Berbasis ESP32 dengan Penjadwalan dan Monitoring Konsumsi untuk Menekan Feed Conversion Ratio",
        "Status": "EVALUATING",
        "Iterasi": "0/3",
        "Sync_State": "SYNCED",
        "Ref_Terkait": "FCR (metrik baku); pedoman budidaya (verifikasi)",
        "Konteks_Masalah_Kontribusi": "Pemberian pakan manual tidak konsisten; overfeeding meningkatkan biaya dan mencemari air.",
        "Evidence_Log_Terkini": "Konsep matang; butuh akses kolam/tank dan pengukuran berat ikan/pakan.",
        "Unblock_Trigger_Reeval_Ref": "(1) Akses kolam/tank; (2) timbangan ikan & pakan; (3) jadwal pakan.",
    },
    {
        "IDEA-ID": "IDEA-056",
        "Tema": "Peternakan / Hatchery",
        "Judul": "Rancang Bangun Smart Egg Candling dan Penghitung Fertilitas Telur Berbasis ESP32 dengan Pengolahan Citra untuk Mengurangi Kesalahan Manual di Hatchery",
        "Status": "EVALUATING",
        "Iterasi": "0/3",
        "Sync_State": "SYNCED",
        "Ref_Terkait": "Candling manual (ground truth); pedoman hatchery (verifikasi)",
        "Konteks_Masalah_Kontribusi": "Candling dan penghitungan telur manual memakan waktu dan tidak konsisten.",
        "Evidence_Log_Terkini": "Konsep jelas; risiko image processing (warna/bercak kerabang); butuh akses hatchery.",
        "Unblock_Trigger_Reeval_Ref": "(1) Akses hatchery/tray telur; (2) candling manual sebagai ground truth; (3) dataset citra.",
    },
    {
        "IDEA-ID": "IDEA-057",
        "Tema": "Akuakultur / Aquaponics",
        "Judul": "Rancang Bangun Smart Aquaponics Berbasis ESP32 dengan Monitoring DO, pH, EC, dan Suhu untuk Menjaga Kestabilan Air dan Meningkatkan Yield",
        "Status": "EVALUATING",
        "Iterasi": "0/3",
        "Sync_State": "SYNCED",
        "Ref_Terkait": "Winkler/ISO 5814 (DO, verifikasi); pedoman akuaponik (verifikasi)",
        "Konteks_Masalah_Kontribusi": "Keseimbangan air akuaponik rapuh; pengujian manual terlambat.",
        "Evidence_Log_Terkini": "Konsep kuat; cakupan lebar; butuh akses sistem akuaponik dan pembatasan komoditas.",
        "Unblock_Trigger_Reeval_Ref": "(1) Akses sistem akuaponik; (2) pembatasan komoditas ikan/sayur; (3) alat uji DO/pH referensi.",
    },
]

rows = m.read_csv(m.REMOTE_CSV)
ids = {n["IDEA-ID"] for n in NEW}
rows = [r for r in rows if r["IDEA-ID"] not in ids]
rows.extend(NEW)
rows.sort(key=lambda r: int(r["IDEA-ID"].split("-")[1]))
m.write_csv(rows)
m.write_txt(rows)
m.write_xlsx(rows)
print("Total:", len(rows))
print("Counts:", m.counts(rows))
