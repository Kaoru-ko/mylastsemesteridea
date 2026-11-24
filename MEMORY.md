# MEMORY.md — Registry Utama Status Ide & Buku Besar Bukti

Dokumen ini adalah *Single Source of Truth* untuk **seluruh `IDEA-ID` dan status terkininya** (baik yang masih `DRAFT`, tertahan karena butuh bukti, aktif tervalidasi, maupun yang gagal dan diarsipkan).

---

## 1. Indeks Status Cepat (Quick Registry)

| IDEA-ID | Tema & Judul Singkat | Status | Iterasi | Sync_State | Ref Terkait |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `IDEA-001` | [Pendidikan] Pemantauan Kualitas Udara & Termal Ruang Kelas | `FAILED_ARCHIVED` | 0/3 | `SYNCED` | `MISTAKE-001` |
| `IDEA-002` | [Pendidikan] Alat Bantu Diagnosis Kesalahan Rangkaian Praktikum | `FAILED_ARCHIVED` | 0/3 | `SYNCED` | `MISTAKE-002` |
| `IDEA-003` | [Kesehatan] Pemantauan Suhu & Kelembapan Lemari Obat/Vaksin | `BLOCKED_PENDING_EVIDENCE` | 0/3 | `SYNCED` | - |
| `IDEA-004` | [Kesehatan] Pemantauan Sisa Volume & Kecepatan Tetesan Infus | `DRAFT` | 0/3 | `SYNCED` | - |
| `IDEA-005` | [Industri] Deteksi Dini Anomali Getaran & Suhu Motor Pompa | `DRAFT` | 0/3 | `SYNCED` | - |

---

## 2. Ledger Detail Per Ide

### IDEA-001
- **Judul:** Rancang Bangun Sistem Pemantauan Kualitas Udara dan Ketidaknyamanan Termal Ruang Kelas Berbasis Sensor Lingkungan dan Notifikasi Otomatis
- **Status:** `FAILED_ARCHIVED`
- **Sync_State:** `SYNCED`
- **Iterasi Revisi:** 0/3
- **Konteks Masalah & Kontribusi:** Pemantauan suhu dan kadar $CO_2$/partikel di ruang kelas/praktikum untuk mencegah mahasiswa cepat mengantuk, pusing, dan turun konsentrasi saat kuliah berlangsung.
- **Evidence_Log:**
  - `[Iterasi 0 - DRAFT]`: Rumusan awal menyasar ruang kelas/praktikum dengan pengujian perbandingan sensor terhadap alat terkalibrasi.
  - `[Iterasi 0 - EVALUATING -> FAILED_ARCHIVED]`: Gugur pada Tes 1 (`PROBLEM_FAILURE`). Hasil kritisi menunjukkan ruangan kampus sudah ber-AC dan berventilasi, serta rasa kantuk mahasiswa dipengaruhi variabel lain (penerangan, bangku, suara dosen, kurang istirahat, kondisi medis) tanpa bukti kuat bahwa udara adalah penyebab utama.
- **Unblock_Trigger / Re-eval_Ref:** Lihat `MISTAKE-001`
- **Mistake_Ref:** `MISTAKE-001`

---

### IDEA-002
- **Judul:** Sistem Alat Bantu Diagnosis Kesalahan Rangkaian Dasar Praktikum Mikrokontroler Berbasis Pengukuran Tegangan dan Kontinuitas
- **Status:** `FAILED_ARCHIVED`
- **Sync_State:** `SYNCED`
- **Iterasi Revisi:** 0/3
- **Konteks Masalah & Kontribusi:** Membantu mahasiswa melacak *short circuit*, salah polaritas/pin, dan *loose connection* pada breadboard praktikum mikrokontroler.
- **Evidence_Log:**
  - `[Iterasi 0 - DRAFT]`: Rumusan awal menyasar efisiensi waktu *troubleshooting* di meja praktikum mahasiswa.
  - `[Iterasi 0 - EVALUATING -> FAILED_ARCHIVED]`: Gugur pada Tes 2 (`SOLUTION_FAILURE`). Hasil kritisi menunjukkan perangkat edukasi rangkaian dasar sudah banyak tersedia di pasar daring (model buku tombol, balok magnetik, dan alat uji kontinuitas) dengan harga jauh lebih murah dan kualitas teruji, sementara usulan belum memiliki pembeda signifikan.
- **Unblock_Trigger / Re-eval_Ref:** Lihat `MISTAKE-002`
- **Mistake_Ref:** `MISTAKE-002`

---

### IDEA-003
- **Judul:** Sistem Pemantauan Suhu dan Kelembapan Lemari Penyimpanan Sediaan Farmasi Berbasis Peringatan Ambang Batas Real-Time
- **Status:** `BLOCKED_PENDING_EVIDENCE`
- **Sync_State:** `SYNCED`
- **Iterasi Revisi:** 0/3
- **Konteks Masalah & Kontribusi:** Pemantauan kestabilan suhu dan kelembapan pada lemari penyimpanan obat, reagen, atau vaksin di fasilitas kesehatan (klinik/puskesmas/apotek) untuk mencegah penurunan mutu sediaan.
- **Evidence_Log:**
  - `[Iterasi 0 - DRAFT]`: Rumusan awal menyasar fluktuasi suhu lemari farmasi dengan skenario pintu terbuka dan beban pendinginan.
  - `[Iterasi 0 - EVALUATING -> BLOCKED_PENDING_EVIDENCE]`: Hasil kritisi menekankan bahwa setiap jenis obat dan vaksin memiliki rentang suhu penyimpanan yang berbeda. Ide belum terbukti gagal secara teknis, tetapi tertahan karena belum menetapkan jenis sediaan target, referensi standar medisnya, dan bukti urgensi di lokasi spesifik.
- **Unblock_Trigger / Re-eval_Ref:** (1) Menetapkan jenis sediaan farmasi spesifik (misalnya vaksin rantai dingin $2^\circ\text{C}\text{--}8^\circ\text{C}$ atau obat suhu terkendali $15^\circ\text{C}\text{--}25^\circ\text{C}$) beserta rujukan standar resmi Kemenkes/WHO/Farmakope; (2) Melampirkan data awal urgensi masalah pencatatan/fluktuasi suhu dari klinik, apotek, atau puskesmas target.
- **Mistake_Ref:** N/A

---

### IDEA-004
- **Judul:** Rancang Bangun Sistem Pemantauan Sisa Volume dan Kecepatan Tetesan Infus Berbasis Sensor Optik dan Load Cell
- **Status:** `DRAFT`
- **Sync_State:** `SYNCED`
- **Iterasi Revisi:** 0/3
- **Konteks Masalah & Kontribusi:** Pemantauan sisa volume cairan dan laju tetesan infus untuk mengurangi keterlambatan deteksi saat cairan hampir habis atau aliran terhenti pada skenario simulasi ruang perawatan.
- **Evidence_Log:**
  - `[Iterasi 0 - DRAFT]`: Ide baru dicatat. Belum menjalani sesi kritisi dan audit 4 Tes Kegagalan.
- **Unblock_Trigger / Re-eval_Ref:** Menunggu sesi kritisi awal (fokus evaluasi: komparasi dengan *infusion pump* eksisting, stabilitas pembacaan *load cell* terhadap gerakan tiang infus, dan batasan keamanan alat medis).
- **Mistake_Ref:** N/A

---

### IDEA-005
- **Judul:** Sistem Deteksi Dini Anomali Getaran dan Suhu Motor Pompa Industri Berbasis Sensor Akselerometer dan Temperatur
- **Status:** `DRAFT`
- **Sync_State:** `SYNCED`
- **Iterasi Revisi:** 0/3
- **Konteks Masalah & Kontribusi:** Pemantauan dini keausan *bearing*, *misalignment*, dan *overheating* pada motor induksi atau pompa utilitas/industri untuk mencegah *unplanned downtime*.
- **Evidence_Log:**
  - `[Iterasi 0 - DRAFT]`: Ide baru dicatat. Belum menjalani sesi kritisi dan audit 4 Tes Kegagalan.
- **Unblock_Trigger / Re-eval_Ref:** Menunggu sesi kritisi awal (fokus evaluasi: ketersediaan unit motor/pompa nyata untuk pengujian, metode simulasi *fault* tanpa merusak aset industri, dan penetapan ambang batas getaran standar ISO 10816/20816).
- **Mistake_Ref:** N/A
