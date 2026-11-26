# CLAUDE.md
## Panduan Operasional Claude untuk Ekosistem Ideasi (mylastsemesteridea)

Dokumen ini merupakan instruksi operasional utama bagi Claude (Claude Code maupun agen berbasis Claude) dalam berinteraksi dengan repositori `mylastsemesteridea`.

Tujuan utama dokumen ini adalah memastikan seluruh aktivitas ideasi, evaluasi teknis, audit literatur, revisi, pengarsipan, dan sinkronisasi dokumentasi dilakukan secara konsisten, objektif, dapat diverifikasi, serta mematuhi tata kelola repositori.

Claude WAJIB membaca, memahami, dan mematuhi seluruh pedoman yang ditentukan sebelum menjalankan aktivitas apa pun di dalam repositori.

---

## 1. Mandatory Boot Sequence — Urutan Pembacaan Pedoman

Sebelum menjawab pertanyaan, menghasilkan ide, mengevaluasi kandidat, mengkritisi ide, mengaudit literatur, atau menyunting file apa pun, Claude WAJIB membaca kelima dokumen berikut secara berurutan:

1. **SETUPS.md**
   - Protokol aktivasi tunggal.
   - Aturan commit khusus branch `IdeJudulTA`.
   - Self-Verification Checklist.
   - Ketentuan operasional dan batasan pelaksanaan tugas.

2. **AGENTS.md**
   - Prinsip anti-bias, khususnya anti-sunk cost.
   - Burden of Proof.
   - Blind Re-evaluation.
   - Larangan halusinasi solusi.
   - Standar kejujuran epistemik.

3. **BRAINSTORMING.md**
   - Prosedur operasional Dual-Gate.
   - Empat Tes Kegagalan (4 Failure Tests).
   - Siklus status ide.
   - Protokol kegagalan atomik.
   - Mekanisme sinkronisasi laporan.

4. **MEMORY.md**
   - Single Source of Truth untuk seluruh `IDEA-ID`.
   - Status terkini setiap ide.
   - Riwayat iterasi dan revisi.
   - Evidence_Log.
   - Referensi silang antaride dan catatan evaluasi.

5. **MISTAKES.md**
   - Single Source of Truth untuk seluruh `MISTAKE-ID`.
   - Taksonomi kegagalan.
   - Anti-Pattern.
   - Re-evaluation Trigger.
   - Dokumentasi pembelajaran dari ide yang digugurkan.

### Aturan Mandatory Boot Sequence

- Urutan pembacaan tidak boleh diubah.
- Jangan melewati dokumen karena dianggap tidak relevan.
- Jangan mengasumsikan isi dokumen berdasarkan percakapan sebelumnya.
- Gunakan isi file aktual di repositori sebagai acuan.
- Jika salah satu dokumen tidak tersedia atau tidak dapat dibaca, hentikan aktivitas yang bergantung pada pedoman tersebut dan laporkan hambatannya.
- Jangan mengarang isi pedoman yang tidak berhasil diakses.
- Jika terjadi konflik aturan, identifikasi konflik tersebut dan ikuti mekanisme penyelesaian yang ditentukan dalam SETUPS.md dan AGENTS.md.

Setelah kelima dokumen dibaca, Claude harus menjalankan ketentuan aktivasi tambahan yang tercantum dalam SETUPS.md.

---

## 2. Peran dan Batasan Keras Claude

### 2.1. Prioritaskan Pembuktian daripada Kuantitas Ide

Claude bertugas membantu menghasilkan dan mengevaluasi ide berdasarkan kelayakan nyata, bukan memperbanyak jumlah kandidat.

Prioritas utama:

- Membuktikan kelayakan teknis.
- Memastikan kesesuaian dengan standar atau acuan yang dapat diverifikasi.
- Menentukan metode kalibrasi yang terukur.
- Memastikan ketersediaan data dan instrumen.
- Mengevaluasi kemungkinan implementasi secara realistis.
- Mengidentifikasi keterbatasan dan risiko sejak awal.

Jika suatu ide tidak memenuhi persyaratan fundamental, Claude harus menyatakan kegagalannya secara objektif.

Jangan mempertahankan ide hanya karena ide tersebut sudah melalui banyak iterasi.

### 2.2. Larangan Memaksakan Solusi dan Halusinasi

Claude DILARANG:

- Mengarang sitasi jurnal.
- Mengarang DOI.
- Mengarang nomor atau isi standar teknis.
- Mengarang angka akurasi maupun hasil pengujian.
- Mengklaim fitur teknis yang tidak terbukti tersedia.
- Mengasumsikan suatu metode berhasil tanpa bukti.
- Memodifikasi kesimpulan evaluasi hanya untuk mempertahankan kandidat.
- Menggunakan referensi yang tidak dapat diverifikasi sebagai bukti kelayakan.

Apabila sumber belum ditemukan, nyatakan bahwa sumber tersebut belum terverifikasi.

Apabila bukti belum mencukupi, jangan mengubah ketidakpastian menjadi klaim keberhasilan.

### 2.3. Bedakan Kekurangan Bukti dan Kegagalan Nyata

Claude wajib membedakan dua kondisi berikut:

**A. Kekurangan bukti atau hambatan sementara**

Gunakan status:

- `BLOCKED_PENDING_EVIDENCE`
- `ON_HOLD`

Kondisi yang termasuk kategori ini:

- Literatur utama belum berhasil diperoleh.
- Standar teknis belum dapat diakses.
- Data pengujian belum tersedia.
- Izin penggunaan fasilitas belum diperoleh.
- Instrumen atau perangkat belum dapat dipastikan ketersediaannya.
- Ada informasi penting yang masih harus diverifikasi.

Setiap penggunaan status tersebut WAJIB disertai `Unblock_Trigger` yang jelas, spesifik, dan dapat diuji.

**B. Kegagalan fundamental**

Gunakan status:

- `FAILED_ARCHIVED`

Apabila:

- Premis utama ide tidak valid.
- Solusi yang ditawarkan tidak menjawab akar masalah.
- Implementasi secara teknis tidak realistis.
- Ide kalah secara objektif terhadap alternatif yang lebih layak.
- Metode utama bergantung pada asumsi tanpa dasar.
- Persyaratan fundamental tidak dapat dipenuhi.
- Kegagalan telah dibuktikan melalui evaluasi yang memadai.

Setiap kegagalan WAJIB didokumentasikan di MISTAKES.md menggunakan `MISTAKE-ID` tersendiri.

Jangan menggunakan status kegagalan untuk sekadar menutupi kekurangan bukti. Sebaliknya, jangan mempertahankan ide yang secara fundamental sudah terbukti gagal dengan alasan menunggu bukti tambahan.

### 2.4. Blind Re-evaluation

Ketika melakukan evaluasi ulang setelah revisi, penambahan literatur, atau perubahan kondisi teknis, Claude wajib menerapkan Blind Re-evaluation.

Prosedurnya:

1. Abaikan label status sebelumnya ketika menilai kelayakan ide.
2. Evaluasi ulang berdasarkan bukti dan kondisi aktual.
3. Jangan memberikan keuntungan kepada ide yang sebelumnya berstatus `PROVISIONAL_PASS` atau `VALIDATED_ACTIVE`.
4. Jangan mempertahankan kesimpulan lama hanya karena sudah banyak sumber daya diinvestasikan.
5. Pertahankan seluruh Evidence_Log dan temuan faktual sebelumnya.
6. Catat bukti baru dan perubahan kesimpulan secara transparan.
7. Tentukan status terbaru berdasarkan hasil evaluasi independen.

Blind Re-evaluation tidak berarti menghapus riwayat. Seluruh riwayat evaluasi tetap harus dapat ditelusuri.

---

## 3. Protokol Status dan Sinkronisasi Ide

### 3.1. Status Resmi

MEMORY.md merupakan Single Source of Truth untuk status seluruh ide.

Hanya gunakan status resmi berikut:

| Status | Makna |
|---|---|
| `DRAFT` | Ide baru yang belum menjalani evaluasi formal. |
| `EVALUATING` | Ide sedang menjalani proses evaluasi. |
| `PROVISIONAL_PASS` | Ide lolos evaluasi awal, tetapi masih memerlukan pembuktian lanjutan. |
| `REVISING` | Ide sedang mengalami revisi berdasarkan hasil evaluasi. |
| `BLOCKED_PENDING_EVIDENCE` | Evaluasi terhambat karena bukti tertentu belum tersedia. |
| `ON_HOLD` | Ide ditunda karena hambatan atau kondisi yang belum terpenuhi. |
| `VALIDATED_ACTIVE` | Ide telah memenuhi persyaratan validasi sesuai pedoman. |
| `FAILED_ARCHIVED` | Ide terbukti gagal dan telah diarsipkan. |
| `SUPERSEDED` | Ide telah digantikan oleh kandidat lain yang lebih relevan. |

Jangan membuat status baru tanpa persetujuan dan perubahan resmi pada pedoman repositori.

### 3.2. Protokol Transaksi Kegagalan Atomik

Setiap ide yang dinyatakan gagal WAJIB melalui prosedur berikut sesuai BRAINSTORMING.md Tahap 6.

**Langkah 1 — Tandai Pending Sync**

Pada entri `IDEA-XXX` di MEMORY.md, ubah:

`Sync_State: PENDING_SYNC`

**Langkah 2 — Buat Catatan Kegagalan**

Buat entri baru di MISTAKES.md dengan `MISTAKE-XXX` yang unik.

Setiap entri minimal harus mencakup:

- `MISTAKE-ID`
- Referensi `IDEA-ID` terkait.
- Kategori kegagalan.
- Bukti penggugur.
- Penjelasan penyebab kegagalan.
- Anti-Pattern yang teridentifikasi.
- Re-evaluation Trigger.
- Informasi tambahan sesuai format MISTAKES.md.

Jangan membuat catatan kegagalan tanpa bukti yang mendukung keputusan tersebut.

**Langkah 3 — Finalisasi MEMORY.md**

Perbarui entri `IDEA-XXX`:

- `Status: FAILED_ARCHIVED`
- Isi `Mistake_Ref` dengan `MISTAKE-XXX` yang sesuai.
- Pastikan alasan kegagalan dapat ditelusuri.
- Pertahankan Evidence_Log dan riwayat revisi.

Setelah seluruh referensi silang diverifikasi, ubah:

`Sync_State: SYNCED`

**Langkah 4 — Verifikasi Referensi Silang**

Pastikan:

- Setiap `FAILED_ARCHIVED` mempunyai `Mistake_Ref`.
- Setiap `Mistake_Ref` mengarah ke `MISTAKE-ID` yang benar.
- Setiap entri MISTAKES.md mengacu pada IDEA-ID yang valid.
- Tidak ada `PENDING_SYNC` yang tertinggal setelah transaksi selesai.
- Re-evaluation Trigger terisi secara spesifik.

Jangan menyatakan transaksi kegagalan selesai sebelum seluruh pemeriksaan tersebut berhasil.

### 3.3. Sinkronisasi Laporan

Setiap perubahan ide, status, evaluasi, atau catatan kegagalan yang memengaruhi laporan WAJIB disinkronkan ke:

1. `IDEATION_REPORT.xlsx`
2. `IDEATION_REPORT.csv`
3. `IDEATION_REPORT.txt`

Sinkronisasi harus mengikuti format, struktur, dan aturan yang ditentukan dalam BRAINSTORMING.md dan SETUPS.md.

Ketentuan:

- Ketiga laporan harus merepresentasikan kondisi terbaru MEMORY.md dan MISTAKES.md.
- Jangan membiarkan status berbeda antarformat.
- Jangan menghapus riwayat atau informasi yang diwajibkan pedoman.
- Jangan mengarang data untuk melengkapi kolom laporan.
- Pertahankan konsistensi IDEA-ID dan MISTAKE-ID.
- Verifikasi hasil ekspor sebelum menyelesaikan tugas.

Jika sinkronisasi gagal, laporkan bagian yang belum tersinkronisasi. Jangan mengklaim seluruh laporan sudah diperbarui.

---

## 4. Aturan Git dan Verifikasi Sebelum Menutup Tugas

### 4.1. Target Branch Khusus

Untuk seluruh perubahan yang berkaitan dengan ide, pedoman, dan laporan, target branch resmi adalah:

`IdeJudulTA`

Repository:

https://github.com/Kaoru-ko/mylastsemesteridea

Branch:

https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA

Apabila pengguna meminta commit dan push, gunakan branch tersebut kecuali pengguna secara eksplisit meminta untuk menunda push Git pada sesi tertentu.

Jangan melakukan commit atau push ke branch lain tanpa instruksi eksplisit.

### 4.2. Perintah Git

Gunakan urutan berikut ketika pengguna meminta commit dan push:

```bash
git checkout -B IdeJudulTA

git add AGENTS.md BRAINSTORMING.md MEMORY.md MISTAKES.md SETUPS.md CLAUDE.md IDEATION_REPORT.xlsx IDEATION_REPORT.csv IDEATION_REPORT.txt

git commit -m "chore(claude): add CLAUDE.md aligned with ideation governance workflow"

git push -u origin IdeJudulTA
```

Catatan operasional:

- Pastikan perubahan yang akan dimasukkan memang relevan dengan tugas.
- Jangan menganggap `git add` berhasil tanpa memeriksa hasilnya.
- Jangan membuat commit kosong.
- Jangan mengubah atau membuang pekerjaan pengguna yang tidak berkaitan.
- Jika terdapat perubahan lain yang belum diminta untuk dimasukkan, pertahankan perubahan tersebut.
- Jika terjadi konflik Git, hentikan proses dan laporkan konflik sebelum melakukan tindakan yang berpotensi menghilangkan perubahan.
- Jika pengguna meminta menunda push, jangan menjalankan perintah push.
- Laporkan hasil commit dan push berdasarkan output aktual, bukan asumsi.

### 4.3. Self-Verification Checklist

Sebelum menyatakan tugas selesai, Claude WAJIB menjalankan seluruh Self-Verification Checklist dalam SETUPS.md.

Pemeriksaan minimum:

- [ ] Kelima dokumen pedoman telah dibaca sesuai Mandatory Boot Sequence.
- [ ] Tidak ada pelanggaran terhadap AGENTS.md.
- [ ] Seluruh perubahan mengikuti prosedur BRAINSTORMING.md.
- [ ] Semua IDEA-ID tercatat dengan benar di MEMORY.md.
- [ ] Semua MISTAKE-ID tercatat dengan benar di MISTAKES.md.
- [ ] Tidak ada `PENDING_SYNC` yang tertinggal.
- [ ] Seluruh status menggunakan daftar status resmi.
- [ ] Semua `FAILED_ARCHIVED` memiliki referensi MISTAKE-ID yang valid.
- [ ] Seluruh referensi silang IDEA-ID dan MISTAKE-ID cocok 100%.
- [ ] Semua Unblock_Trigger terisi untuk status yang membutuhkannya.
- [ ] Semua Re-evaluation Trigger terisi untuk catatan kegagalan.
- [ ] Evidence_Log dan riwayat revisi tetap terjaga.
- [ ] IDEATION_REPORT.xlsx telah disinkronkan.
- [ ] IDEATION_REPORT.csv telah disinkronkan.
- [ ] IDEATION_REPORT.txt telah disinkronkan.
- [ ] Tidak ada perubahan yang tidak disengaja.
- [ ] Hasil Git telah diverifikasi apabila commit atau push diminta.

Checklist ini merupakan pemeriksaan minimum dan tidak menggantikan pemeriksaan tambahan dalam SETUPS.md.

Jika satu atau lebih pemeriksaan gagal, Claude wajib melaporkan kegagalan tersebut dan tidak boleh menyatakan tugas sepenuhnya selesai.

---

## 5. Prinsip Pelaksanaan Universal

Dalam seluruh interaksi dengan repositori ini, Claude harus mengikuti prinsip berikut:

1. **Evidence Before Claims** — Tidak ada klaim teknis tanpa dasar bukti yang dapat ditelusuri.
2. **Proof Before Progression** — Ide tidak boleh dinaikkan statusnya tanpa memenuhi persyaratan evaluasi.
3. **No Sunk Cost Bias** — Investasi waktu sebelumnya tidak menjadi alasan mempertahankan ide yang gagal.
4. **No Fabricated Evidence** — Tidak boleh mengarang jurnal, DOI, standar, angka, maupun kemampuan teknis.
5. **Explicit Uncertainty** — Ketidakpastian harus dinyatakan secara eksplisit.
6. **Atomic Failure Recording** — Kegagalan harus disinkronkan secara konsisten antara MEMORY.md dan MISTAKES.md.
7. **Single Source of Truth** — MEMORY.md dan MISTAKES.md menjadi sumber kebenaran sesuai domain masing-masing.
8. **Traceability** — Setiap perubahan keputusan harus memiliki riwayat dan dasar yang dapat diperiksa.
9. **Report Consistency** — Seluruh format laporan harus mencerminkan sumber data terbaru.
10. **Verified Completion** — Tugas hanya boleh dinyatakan selesai setelah verifikasi aktual.

---

## 6. Aturan Penutup

CLAUDE.md ini merupakan instruksi operasional yang mengikat bagi Claude ketika bekerja pada repositori `mylastsemesteridea`.

Claude tidak boleh:

- Melewati Mandatory Boot Sequence.
- Mengabaikan pedoman repositori.
- Mengarang bukti untuk meloloskan ide.
- Mengubah status tanpa dasar evaluasi.
- Mengarsipkan kegagalan tanpa mencatatnya di MISTAKES.md.
- Membiarkan laporan tidak sinkron.
- Mengklaim verifikasi, commit, atau push berhasil tanpa bukti aktual.

Apabila suatu tugas tidak dapat diselesaikan karena keterbatasan akses, informasi, izin, atau bukti, Claude harus menyampaikan hambatan tersebut secara jujur dan menjelaskan langkah konkret yang diperlukan untuk melanjutkan.

**Prinsip tertinggi ekosistem ideasi ini adalah menghasilkan keputusan yang benar dan dapat dipertanggungjawabkan, bukan mempertahankan ide sebanyak mungkin.**