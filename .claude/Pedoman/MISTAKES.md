### MISTAKES.md — Ledger Kegagalan, Anti-Pattern & Syarat Evaluasi Ulang
Dokumen ini adalah *Single Source of Truth* untuk seluruh riwayat kegagalan ide. Kegagalan tidak dihapus agar agen tidak mengulang kesalahan yang sama, namun dikunci dengan `Re-evaluation Trigger` yang objektif. Setiap pembaruan wajib disinkronkan ke `IDEATION_REPORT.*` dan di-commit ke branch `IdeJudulTA` (https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA).

---

#### 1. Taksonomi 4 Kategori Kegagalan (Wajib Dipilih Salah Satu)
1. **PROBLEM_FAILURE** Permasalahan awal ternyata tidak nyata, tidak mendesak, salah sasaran, bias oleh faktor lain (*confounding factors*), atau tidak didukung bukti lapangan.
2. **SOLUTION_FAILURE** Masalahnya nyata dan valid, tetapi solusi yang ditawarkan tidak menjawab akar masalah tersebut atau tidak memiliki pembeda/nilai tambah dibanding alat komersial murah yang sudah ada.
3. **FEASIBILITY_FAILURE** Masalah dan solusi masuk akal secara teori, tetapi implementasinya tidak realistis dalam batasan waktu, biaya, daya, sumber daya, atau akses kondisi lapangan penelitian.
4. **HALLUCINATED_SOLUTION** Solusi terlihat menarik di atas kertas, tetapi tidak memiliki dasar teknis, bukti kebutuhan, atau mekanisme kerja yang dapat dipertanggungjawabkan (berbasis asumsi/karangan AI).

---

#### 2. Matriks Keputusan Pencatatan ke `MISTAKES.md`
| Kondisi Akhir Ide | Masuk `MISTAKES.md`? | Status Akhir di `MEMORY.md` | Keterangan |
| ------ | ------ | ------ | ------ |
| Ditolak/gugur pada evaluasi awal atau kritisi masalah | **Ya** | `FAILED_ARCHIVED` | Mencatat alasan penolakan awal agar tidak diulang. |
| Sempat `PROVISIONAL_PASS`, tetapi gagal validasi bukti | **Ya** | `FAILED_ARCHIVED` | Penilaian konseptual awal terbukti belum cukup kuat. |
| Masuk `REVISING`, tetapi tidak ditemukan solusi nyata | **Ya** | `FAILED_ARCHIVED` | Mencegah pemaksaan solusi saat jalan buntu. |
| Revisi hanya menghasilkan solusi berbasis asumsi | **Ya** | `FAILED_ARCHIVED` | Dikategorikan sebagai `HALLUCINATED_SOLUTION`. |
| Solusi menuntut teknologi/biaya tidak realistis | **Ya** | `FAILED_ARCHIVED` | Dikategorikan sebagai `FEASIBILITY_FAILURE`. |
| Tertahan karena standar/data lapangan belum diperoleh | **Tidak** | `BLOCKED_PENDING_EVIDENCE` | Belum terbukti gagal; menunggu `Unblock_Trigger`. |
| Berhasil direvisi dan lolos validasi bukti | **Tidak** | `VALIDATED_ACTIVE` | Riwayat revisi disimpan di `MEMORY.md`. |

---

#### 3. Skema Standar Entri Kegagalan
```markdown
### MISTAKE-XXX
- **IDEA-ID:** IDEA-XXX
- **Tanggal Arsip:** YYYY-MM-DD
- **Status Sebelum Gagal:** DRAFT / EVALUATING / PROVISIONAL_PASS / REVISING
- **Kategori Kegagalan:** PROBLEM_FAILURE / SOLUTION_FAILURE / FEASIBILITY_FAILURE / HALLUCINATED_SOLUTION
- **Ringkasan Ide:** Deskripsi singkat masalah dan solusi yang diajukan.
- **Akar Masalah & Bukti Penggugur:** Hasil kritisi, fakta teknis, atau temuan lapangan yang menggugurkan ide.
- **Anti-Pattern (Larangan bagi Agen):** Pola pendekatan spesifik yang tidak boleh diusulkan kembali tanpa perubahan syarat.
- **Re-evaluation Trigger (Syarat Objektif Pembuka Kunci):** Kondisi atau bukti baru spesifik yang wajib ada sebelum ide serupa boleh dievaluasi ulang.
```

---

#### 4. Arsip Kegagalan Aktif
##### MISTAKE-001
* **IDEA-ID:** IDEA-001
* **Tanggal Arsip:** 2026-11-25
* **Status Sebelum Gagal:** EVALUATING
* **Kategori Kegagalan:** PROBLEM_FAILURE
* **Ringkasan Ide:** Pemantauan kualitas udara (CO2/partikel) dan ketidaknyamanan termal ruang kelas/praktikum ber-AC untuk mencegah mahasiswa mengantuk dan turun konsentrasi.
* **Akar Masalah & Bukti Penggugur:** (1) Ruang kelas/laboratorium target umumnya sudah dilengkapi AC dan ventilasi sehingga urgensi intervensi lingkungan tidak terbukti mendesak; (2) Gejala mahasiswa mengantuk di kelas dipengaruhi banyak variabel lain (*confounding factors*) seperti pencahayaan, ergonomi bangku, intonasi/metode penyampaian dosen, kurang tidur, serta kondisi medis individu—bukan semata kualitas udara.
* **Anti-Pattern (Larangan bagi Agen):** Jangan mengaitkan gejala psikologis/fisiologis umum (seperti mengantuk di kelas) secara langsung sebagai bukti kerusakan kualitas udara pada ruangan yang sudah ber-AC tanpa pengukuran baseline aktual.
* **Re-evaluation Trigger (Syarat Objektif Pembuka Kunci):** Tersedia data pengukuran lapangan awal (baseline audit) pada ruang kelas/praktikum spesifik yang membuktikan kadar CO2 melampaui ambang batas kenyamanan (>1000 ppm) atau kegagalan termal berulang saat kelas terisi penuh meskipun AC/ventilasi beroperasi normal.

##### MISTAKE-002
* **IDEA-ID:** IDEA-002
* **Tanggal Arsip:** 2026-11-25
* **Status Sebelum Gagal:** EVALUATING
* **Kategori Kegagalan:** SOLUTION_FAILURE
* **Ringkasan Ide:** Alat bantu diagnosis kesalahan rangkaian dasar praktikum mikrokontroler (hubung singkat, salah polaritas/pin, *loose connection*) berbasis pengukuran tegangan dan kontinuitas.
* **Akar Masalah & Bukti Penggugur:** Perangkat pembelajaran rangkaian dasar (seperti kit edukasi tombol, balok magnetik, *continuity tester*, dan modul pelatihan dasar) sudah banyak dijual di pasaran dengan harga jauh lebih murah dan kualitas mapan. Usulan tidak membuktikan diferensiasi teknis atau keunggulan diagnostik yang tidak bisa dipenuhi oleh produk komersial yang sudah ada.
* **Anti-Pattern (Larangan bagi Agen):** Jangan mengusulkan pembuatan alat bantu praktikum dasar yang fungsinya sudah terwakili oleh kit edukasi komersial murah tanpa mendefinisikan celah teknis spesifik yang gagal ditangani alat komersial tersebut.
* **Re-evaluation Trigger (Syarat Objektif Pembuka Kunci):** Ditemukan celah diagnostik spesifik pada modul praktikum mikrokontroler tingkat lanjut (misalnya deteksi konflik bus komunikasi atau *fault injection* pin mikrokontroler secara otomatis) yang tidak tersedia pada alat komersial murah, disertai bukti kebutuhan dari dosen/laboran mata kuliah terkait.

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

