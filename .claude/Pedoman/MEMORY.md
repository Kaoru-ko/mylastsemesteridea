### MEMORY.md — Registry Utama Status Ide & Buku Besar Bukti
Dokumen ini adalah *Single Source of Truth* untuk **seluruh IDEA-ID dan status terkininya** (baik yang masih `DRAFT`, tertahan karena butuh bukti, aktif tervalidasi, maupun yang gagal dan diarsipkan). Setiap pembaruan wajib disinkronkan ke `IDEATION_REPORT.*` dan di-commit ke branch `IdeJudulTA` (https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA).

---

#### 1. Indeks Status Cepat (Quick Registry)
| IDEA-ID | Tema & Judul Singkat | Status | Iterasi | Sync_State | Ref Terkait |
| ------ | ------ | ------ | ------ | ------ | ------ |
| IDEA-001 | [Pendidikan] Pemantauan Kualitas Udara & Termal Ruang Kelas | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-001 |
| IDEA-002 | [Pendidikan] Alat Bantu Diagnosis Kesalahan Rangkaian Praktikum | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-002 |
| IDEA-003 | [Kesehatan] Pemantauan Suhu & Kelembapan Lemari Obat/Vaksin | SUPERSEDED | 0/3 | SYNCED | N/A |
| IDEA-004 | [Kesehatan] Pemantauan Sisa Volume & Kecepatan Tetesan Infus | DRAFT | 0/3 | SYNCED | N/A |
| IDEA-005 | [Industri] Deteksi Dini Anomali Getaran & Suhu Motor Pompa | DRAFT | 0/3 | SYNCED | N/A |
| IDEA-006 | [Pendidikan] Alat Peraga Pembelajaran Topologi dan Keamanan Jaringan Berbasis ESP32 Wi-Fi 2.4 GHz serta Aplikasi Pendamping untuk Siswa SMK TKJ dan RPL | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | N/A |
| IDEA-013 | [Arsip Gagal] Entri Arsip Kegagalan Sebelumnya | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-005 |
| IDEA-014 | [Energi / PV] Estimasi Indeks Kehilangan Daya Akibat Debu PV (Soiling Ratio) | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | IEC 61724-1:2021 Annex C |
| IDEA-015 | [Sensor / Kimia Air] Sensor Konduktivitas Empat-Elektroda Kompensasi Suhu | VALIDATED_ACTIVE | 0/3 | SYNCED | ISO 7888, ASTM D1125 |
| IDEA-016 | [Kesehatan / Biomekanika] Pemantau Fleksi Lutut & Beban Tumpuan Pasca-ACL | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | - |
| IDEA-017 | [Bangunan / Pencahayaan] Kendali Pencahayaan Hibrida Daylight-LED & Silau Tirai | VALIDATED_ACTIVE | 0/3 | SYNCED | SNI 6197:2020, SNI 7062:2019, IEEE Std 1789-2015 |
| IDEA-018 | [Proteksi Listrik] Deteksi Dini Busur Api Seri 220 VAC HFCT & Zero-Crossing | VALIDATED_ACTIVE | 0/3 | SYNCED | IEC 62606, UL 1699 |
| IDEA-019 | [Manufaktur Aditif / 3D] Pengkondisi & Pengering Filamen Delta-AH, Gravimetri, Tg | REVISING | 1/3 | SYNCED | ASTM D6980 (kadar air), ASTM D3418/E1356 (Tg), ASTM D638 |
| IDEA-020 | [Arsip Gagal] Entri Arsip Kegagalan Sebelumnya | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-006 |
| IDEA-021 | [HVAC / FDD] Diagnosis Undercharge Refrigeran & Fouling Kondensor | REVISING | 2/3 | SYNCED | ASHRAE Guideline 22, ISO 5149 |
| IDEA-022 | [NDT / Metrologi] Alat Ukur Ketebalan Lapisan Non-Konduktif Dual-Mode | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | - |
| IDEA-023 | [Pertambangan / Geoteknik] Peringatan Dini Pergeseran Dinding Terowongan | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Kepmen ESDM No. 1827K/30/MEM/2018 |
| IDEA-024 | [Kualitas Air / Optik] Turbidimeter Rasio Nefelometrik IR 860 nm | VALIDATED_ACTIVE | 0/3 | SYNCED | ISO 7027-1:2016, SNI 06-6989.25-2005 |
| IDEA-025 | [Kontrol / Mekatronika] Kendali Posisi & Kompensasi Backlash Lead-Screw | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | - |
| IDEA-026 | [Baterai / Second-Life] Karakterisasi SoH & DCIR HPPC 4-Kawat Kelvin Li-Ion | VALIDATED_ACTIVE | 0/3 | SYNCED | IEC 61960-3:2017, USABC HPPC |
| IDEA-027 | [Kualitas Daya Listrik] Pemantauan Kualitas Daya & Ketidakseimbangan Fasa ESP32 | REVISING | 1/3 | SYNCED | IEC 61000-4-30, NEMA MG 1, IEEE 1159 |
| IDEA-028 | [Arsip Gagal] Entri Arsip Kegagalan Sebelumnya | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-007 |
| IDEA-029 | [Pembangkit Pikohidro / ELC] ELC Biner Zero-Crossing SEIG Pikohidro | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | - |
| IDEA-030 | [Kesehatan / Rantai Dingin Darah] Pemantauan Suhu & Getaran Transportasi Darah | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Permenkes No. 91 Tahun 2015 |
| IDEA-031 | [Kesehatan Kerja / Getaran] Pemantauan Dosis Getaran Lengan-Tangan MEMS Wh | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | ISO 5349, ISO 8041, Permenaker No. 5/2018 |
| IDEA-032 | [Energi Terbarukan / Biogas] Pemantauan Laju Biogas STP & Komposisi NDIR | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | VDI 4630 |
| IDEA-033 | [Termofisika / Isolasi Termal] Alat Ukur Konduktivitas Termal Guarded Hot Plate | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | ASTM C177, ISO 8302, NIST |
| IDEA-034 | [Kesehatan / Cold Chain Vaksin] Pemantauan Rantai Dingin Vaksin Rutin 2-8 C | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Revived/Locked from IDEA-003; Permenkes No. 12/2017, WHO PQS E006 |
| IDEA-035 | [Agrikultur / Jamur] Pengendalian Suhu, Kelembapan & Sirkulasi Ruang Jamur Tiram | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Literatur budidaya; ISO 7726 (verifikasi) |
| IDEA-036 | [Kesehatan / Sterilisasi] Verifikasi Siklus Autoklaf F0 | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | ISO 17665-1, ISO 11140-1 (verifikasi) |
| IDEA-037 | [Keselamatan Lab] Pemantauan Kinerja Fume Hood | EVALUATING | 0/3 | SYNCED | ASHRAE 110, EN 14175 (verifikasi) |
| IDEA-038 | [K3 / Tekanan Panas] WBGT Pekerja Outdoor | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | ISO 7243, ISO 7726 (verifikasi) |
| IDEA-039 | [K3 / Kebisingan] Dosis Kebisingan Kerja | EVALUATING | 0/3 | SYNCED | IEC 61672-1, ISO 9612, Permenaker 5/2018 (verifikasi) |
| IDEA-040 | [Pascapanen / Silo] Hotspot Silo Gabah | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | SNI 0224:2022, SNI 6128:2020 (verifikasi) |
| IDEA-041 | [Energi / PV] Pelacak Kurva I-V Panel Surya | EVALUATING | 0/3 | SYNCED | IEC 60904, IEC 61724-1 (verifikasi) |
| IDEA-042 | [Akuakultur / DO] Oksigen Terlarut Kolam | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | ISO 5814 (verifikasi) |
| IDEA-043 | [Agrikultur / Hidroponik] Dosing Nutrisi EC/pH | EVALUATING | 0/3 | SYNCED | ISO 7888 (EC) (verifikasi) |
| IDEA-044 | [Bangunan / IAQ] Kualitas Udara & Ventilasi | EVALUATING | 0/3 | SYNCED | ASHRAE 62.1 (verifikasi) |
| IDEA-045 | [Agrikultur / Irigasi] Irigasi Presisi | EVALUATING | 0/3 | SYNCED | FAO 56, ISO 11274 (verifikasi) |
| IDEA-046 | [Agrikultur / Hama] Light Trap Pintar | EVALUATING | 0/3 | SYNCED | Pedoman IPM (verifikasi) |
| IDEA-047 | [Energi / DC] Monitoring Surya Mandiri Tegangan Rendah | EVALUATING | 0/3 | SYNCED | IEC 61724-1 (verifikasi) |
| IDEA-048 | [Pascapanen / Gabah] Pengukuran Kadar Air Gabah untuk Petani Kecil | FAILED_ARCHIVED | 0/3 | SYNCED | MISTAKE-008 |
| IDEA-049 | [Peternakan / Kandang] Iklim & Amonia Kandang Broiler + Kendali Ventilasi | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Pedoman peternakan; THI (verifikasi) |
| IDEA-050 | [Peternakan / Susu] Suhu & Mutu Susu di Koperasi | EVALUATING | 0/3 | SYNCED | SNI susu segar (verifikasi) |
| IDEA-051 | [Agrikultur / Lebah] Sarang Lebah/Kelulut: Berat, Suhu, RH, Suara | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Pedoman budidaya lebah (verifikasi) |
| IDEA-052 | [Pangan / Pengeringan] Smart Dryer Brem ESP32: Suhu + Penurunan Massa | BLOCKED_PENDING_EVIDENCE | 0/3 | SYNCED | Metode oven (AOAC/SNI, verifikasi); SNI brem (verifikasi) |

---

#### 2. Ledger Detail Per Ide
##### IDEA-001
* **Judul:** Rancang Bangun Sistem Pemantauan Kualitas Udara dan Ketidaknyamanan Termal Ruang Kelas Berbasis Sensor Lingkungan dan Notifikasi Otomatis
* **Status:** FAILED_ARCHIVED
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Pemantauan suhu dan kadar CO2/partikel di ruang kelas/praktikum untuk mencegah mahasiswa cepat mengantuk, pusing, dan turun konsentrasi saat kuliah berlangsung.
* **Evidence_Log:**
  * [Iterasi 0 - DRAFT]: Rumusan awal menyasar ruang kelas/praktikum dengan pengujian perbandingan sensor terhadap alat terkalibrasi.
  * [Iterasi 0 - EVALUATING -> FAILED_ARCHIVED]: Gugur pada Tes 1 (`PROBLEM_FAILURE`). Hasil kritisi menunjukkan ruangan kampus sudah ber-AC dan berventilasi, serta rasa kantuk mahasiswa dipengaruhi variabel lain (penerangan, bangku, suara dosen, kurang istirahat, kondisi medis) tanpa bukti kuat bahwa udara adalah penyebab utama.
* **Unblock_Trigger / Re-eval_Ref:** Lihat `MISTAKE-001`
* **Mistake_Ref:** MISTAKE-001

---

##### IDEA-002
* **Judul:** Sistem Alat Bantu Diagnosis Kesalahan Rangkaian Dasar Praktikum Mikrokontroler Berbasis Pengukuran Tegangan dan Kontinuitas
* **Status:** FAILED_ARCHIVED
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Membantu mahasiswa melacak *short circuit*, salah polaritas/pin, dan *loose connection* pada breadboard praktikum mikrokontroler.
* **Evidence_Log:**
  * [Iterasi 0 - DRAFT]: Rumusan awal menyasar efisiensi waktu troubleshooting di meja praktikum mahasiswa.
  * [Iterasi 0 - EVALUATING -> FAILED_ARCHIVED]: Gugur pada Tes 2 (`SOLUTION_FAILURE`). Hasil kritisi menunjukkan perangkat edukasi rangkaian dasar sudah banyak tersedia di pasar daring (model buku tombol, balok magnetik, dan alat uji kontinuitas) dengan harga jauh lebih murah dan kualitas teruji, sementara usulan belum memiliki pembeda signifikan.
* **Unblock_Trigger / Re-eval_Ref:** Lihat `MISTAKE-002`
* **Mistake_Ref:** MISTAKE-002

---

##### IDEA-003
* **Judul:** Sistem Pemantauan Suhu dan Kelembapan Lemari Penyimpanan Sediaan Farmasi Berbasis Peringatan Ambang Batas Real-Time
* **Status:** SUPERSEDED
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Pemantauan kestabilan suhu dan kelembapan pada lemari penyimpanan obat, reagen, atau vaksin di fasilitas kesehatan (klinik/puskesmas/apotek) untuk mencegah penurunan mutu sediaan.
* **Evidence_Log:**
  * [Iterasi 0 - DRAFT]: Rumusan awal menyasar fluktuasi suhu lemari farmasi dengan skenario pintu terbuka dan beban pendinginan.
  * [Iterasi 0 - EVALUATING -> BLOCKED_PENDING_EVIDENCE]: Hasil kritisi menekankan bahwa setiap jenis obat dan vaksin memiliki rentang suhu penyimpanan yang berbeda. Ide belum terbukti gagal secara teknis, tetapi tertahan karena belum menetapkan jenis sediaan target, referensi standar medisnya, dan bukti urgensi di lokasi spesifik.
* **Unblock_Trigger / Re-eval_Ref:** Superseded-By: IDEA-034; ruang lingkup dikunci ke rantai dingin vaksin rutin 2-8 C.
* **Evidence_Log:**
  * [Iterasi 0 - SUPERSEDED]: Ruang lingkup dikunci ke IDEA-034 (rantai dingin vaksin rutin 2-8 C).
* **Mistake_Ref:** N/A

---

##### IDEA-004
* **Judul:** Rancang Bangun Sistem Pemantauan Sisa Volume dan Kecepatan Tetesan Infus Berbasis Sensor Optik dan Load Cell
* **Status:** DRAFT
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Pemantauan sisa volume cairan dan laju tetesan infus untuk mengurangi keterlambatan deteksi saat cairan hampir habis atau aliran terhenti pada skenario simulasi ruang perawatan.
* **Evidence_Log:**
  * [Iterasi 0 - DRAFT]: Ide baru dicatat. Belum menjalani sesi kritisi dan audit 4 Tes Kegagalan.
* **Unblock_Trigger / Re-eval_Ref:** Menunggu sesi kritisi awal (fokus evaluasi: komparasi dengan *infusion pump* eksisting, stabilitas pembacaan *load cell* terhadap gerakan tiang infus, dan batasan keamanan alat medis).
* **Mistake_Ref:** N/A

---

##### IDEA-005
* **Judul:** Sistem Deteksi Dini Anomali Getaran dan Suhu Motor Pompa Industri Berbasis Sensor Akselerometer dan Temperatur
* **Status:** DRAFT
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Pemantauan dini keausan *bearing*, *misalignment*, dan *overheating* pada motor induksi atau pompa utilitas/industri untuk mencegah *unplanned downtime*.
* **Evidence_Log:**
  * [Iterasi 0 - DRAFT]: Ide baru dicatat. Belum menjalani sesi kritisi dan audit 4 Tes Kegagalan.
* **Unblock_Trigger / Re-eval_Ref:** Menunggu sesi kritisi awal (fokus evaluasi: ketersediaan unit motor/pompa nyata untuk pengujian, metode simulasi *fault* tanpa merusak aset industri, dan penetapan ambang batas getaran standar ISO 10816/20816).
* **Mistake_Ref:** N/A

---

##### IDEA-006
* **Judul:** Alat Peraga Pembelajaran Topologi dan Keamanan Jaringan Berbasis ESP32 Wi-Fi 2.4 GHz serta Aplikasi Pendamping untuk Siswa SMK TKJ dan RPL
* **Status:** BLOCKED_PENDING_EVIDENCE
* **Sync_State:** SYNCED
* **Iterasi Revisi:** 0/3
* **Konteks Masalah & Kontribusi:** Alat peraga pembelajaran topologi dan keamanan jaringan berbasis node ESP32 Wi-Fi 2.4 GHz dan aplikasi pendamping untuk siswa SMK jurusan TKJ dan RPL.
* **Evidence_Log:**
  * [Iterasi 0 - EVALUATING -> BLOCKED_PENDING_EVIDENCE]: Audit awal 4 Tes menemukan: (1) Belum ada bukti masalah lapangan/kurikulum SMK target; (2) Konsep 'ESP32 seperti router' berisiko miskonsepsi routing & kalah dari simulator gratis (Packet Tracer/GNS3) maupun MikroTik (risiko `SOLUTION_FAILURE` seperti `MISTAKE-002`); (3) Risiko interferensi kanal Wi-Fi 2.4 GHz & batas SoftAP saat dipakai massal di kelas (`FEASIBILITY_FAILURE`); (4) Aspek keamanan jaringan masih bayangan mentah tanpa standar kurikulum (dicegah dari `HALLUCINATED_SOLUTION`).
  * [Iterasi 0 - UPDATE BUKTI LAPANGAN -> TETAP BLOCKED_PENDING_EVIDENCE]: Bukti lapangan baru dicatat: (a) Testimoni alumni SMKN 5 Kota Madiun (TKJ) bahwa praktik topologi & keamanan jaringan hanya menggunakan simulasi komputer & MikroTik tanpa alat peraga fisik; (b) Observasi langsung di SMK Swasta PGRI 1 Candiboko menemukan 0 alat peraga, hanya 1 lab kecil berisi 16 PC (Core i5 Gen 3, RAM 6 GB) yang tidak memadai untuk simulator virtualisasi berat (GNS3/EVE-NG), namun sekolah tersebut berjurusan RPL. Celah tersisa: (1) Risiko salah sasaran kurikulum jika objek uji hanya berjurusan RPL; (2) Belum ada silabus/CP resmi & wawancara guru; (3) Desain teknis mitigasi interferensi Wi-Fi 2.4 GHz (16+ node), eliminasi miskonsepsi 'ESP32 seperti router', dan spesifikasi modul keamanan jaringan belum ditetapkan.
* **Unblock_Trigger / Re-eval_Ref:** (1) Verifikasi kesesuaian silabus/CP SMK target (pastikan apakah materi topologi & keamanan jaringan fisik masuk CP RPL di SMK PGRI 1 Candiboko, atau tetapkan SMKN 5 Kota Madiun / SMK jurusan TKJ sebagai objek utama); (2) Wawancara terstruktur dengan guru pengampu lab mengenai kendala pemahaman siswa pada simulasi PC/MikroTik; (3) Desain arsitektur non-router yang memitigasi interferensi kanal Wi-Fi 2.4 GHz untuk skala 16-32 siswa; (4) Spesifikasi modul praktikum keamanan jaringan terukur sesuai standar kurikulum SMK.
* **Mistake_Ref:** N/A

---

#### 3. Catatan Sesi 2026-11-26
* **Total registry:** 46 ide (001-006 dari remote + 013-052 dari pembaruan lokal). ID 007-012 tidak dipakai (gap historis).
* **IDEA-052 (KEEP baru):** Smart Dryer Brem berbasis ESP32; pengendalian suhu + monitoring penurunan massa untuk konsistensi kadar air. Status `BLOCKED_PENDING_EVIDENCE`; butuh baseline produsen, definisi produk, dan akses oven.
* **Tiga judul KEEP:** jamur tiram = `IDEA-035`; kualitas daya = revisi `IDEA-027`; filamen = revisi `IDEA-019`.
* **Revisi:** `IDEA-019` dan `IDEA-027` -> `REVISING` 1/3 dengan catatan teknis (ASTM D6980 bukan Tg; ADC internal ESP32 tidak memadai).
* **Kandidat baru:** `IDEA-035`-`IDEA-047` dan `IDEA-049`-`IDEA-051`; status `BLOCKED_PENDING_EVIDENCE` atau `EVALUATING` sesuai akses. `IDEA-048` -> `FAILED_ARCHIVED` (`MISTAKE-008`).
* **Legacy:** `IDEA-013/020/028` dan `MISTAKE-005/006/007` ditandai legacy tanpa data; tidak dipakai sebagai bukti aktif; digantikan oleh `IDEA-049/050/051`.
* **Catatan bukti:** standar bertanda `(verifikasi)` belum diverifikasi edisinya; tidak ada DOI baru yang dikarang. Hitungan psikrometri, F0, propagasi error, dan resolusi gravimetri adalah hitungan sendiri dan dapat direproduksi.

