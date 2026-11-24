# BRAINSTORMING.md — Prosedur Operasional Standar (SOP) Ideasi & Validasi

Dokumen ini mengatur alur kerja eksekusi dari penciptaan ide hingga keputusan akhir. Semua agen wajib mematuhi aturan perilaku pada `AGENTS.md`.

---

## 1. Siklus Status Resmi Ide (`MEMORY.md`)

| Status | Makna Operasional | Transisi Berikutnya yang Diizinkan |
| :--- | :--- | :--- |
| `DRAFT` | Ide baru dicatat setelah lolos Gate 2 dan belum selesai dikritisi. | `EVALUATING` |
| `EVALUATING` | Sedang menjalani audit 4 Tes Kegagalan & sesi kritisi. | `PROVISIONAL_PASS`, `REVISING`, `BLOCKED_PENDING_EVIDENCE`, `FAILED_ARCHIVED` |
| `PROVISIONAL_PASS` | Lolos evaluasi awal, masuk tahap pembuktian akhir. | `VALIDATED_ACTIVE`, `REVISING`, `BLOCKED_PENDING_EVIDENCE`, `FAILED_ARCHIVED`, `SUPERSEDED` |
| `REVISING` | Sedang memperbaiki celah teknis/bukti (maks. 3 iterasi). | `EVALUATING` (via *Blind Re-evaluation*), `BLOCKED_PENDING_EVIDENCE`, `ON_HOLD`, `FAILED_ARCHIVED` |
| `BLOCKED_PENDING_EVIDENCE` | Tertahan karena data/standar/bukti penting belum tersedia. | `EVALUATING` (jika `Unblock_Trigger` terpenuhi), `FAILED_ARCHIVED`, `SUPERSEDED` |
| `ON_HOLD` | Ditunda sementara atas keputusan manusia/prioritas. | `EVALUATING`, `FAILED_ARCHIVED`, `SUPERSEDED` |
| `VALIDATED_ACTIVE` | Lolos seluruh kriteria bukti dan kelayakan implementasi. | `SUPERSEDED` (jika diganti versi baru yang lebih unggul) |
| `FAILED_ARCHIVED` | Gagal dan diarsipkan. Wajib tertaut ke `MISTAKE-ID`. | *Final* (hanya boleh dibuka ulang jika `Re-evaluation Trigger` di `MISTAKES.md` terpenuhi) |
| `SUPERSEDED` | Digantikan oleh `IDEA-ID` baru yang lebih matang/valid. | *Final* |

> **Flag Operasional Transaksi (`Sync_State`):** `SYNCED` | `PENDING_SYNC`

---

## 2. Alur Eksekusi Langkah-demi-Langkah

### Gate 1: Pre-Generation Context Load (Wajib)
Sebelum menghasilkan atau mengkritisi ide, agen wajib membaca:
1. **`MISTAKES.md`:** Kumpulkan seluruh `Anti-Pattern` dan `Re-evaluation Trigger` sebagai batasan negatif (*negative constraints*).
2. **`MEMORY.md`:** Kumpulkan seluruh ide berstatus `DRAFT`, `EVALUATING`, `VALIDATED_ACTIVE`, `PROVISIONAL_PASS`, `REVISING`, dan `BLOCKED_PENDING_EVIDENCE`.

### Tahap 1: Generasi Kandidat Ide Berbasis Masalah
Setiap kandidat ide wajib dirumuskan dengan 4 komponen minimal:
1. **Masalah Nyata & Objek:** Siapa yang terdampak, di mana lokasi spesifiknya, dan apa bukti masalahnya.
2. **Mekanisme Solusi:** Bagaimana solusi menjawab akar masalah secara teknis.
3. **Nilai Tambah / Kontribusi:** Apa pembeda nyatanya dibanding alat/metode yang sudah ada di pasaran atau literatur.
4. **Pengujian yang Valid:** Metode pengujian terukur terhadap standar/alat referensi yang terkalibrasi.

### Gate 2: Pemeriksaan Duplikasi Semantik & *Zombie Idea*
Cocokkan kandidat ide dengan `MEMORY.md` dan `MISTAKES.md`. **Pengecekan dilakukan berdasarkan kesamaan Masalah, Objek Lapangan, dan Nilai Tambah—bukan sekadar kesamaan sensor atau mikrokontroler.**
- **Kasus A (Mirip entri di `MISTAKES.md` TANPA bukti/kondisi baru yang memenuhi `Re-evaluation Trigger`):**
  $\rightarrow$ **BLOKIR OTOMATIS (`Zombie Idea`)**. Jangan catat ke `MEMORY.md`, jangan dievaluasi ulang.
- **Kasus B (Mirip entri di `MISTAKES.md` DENGAN memenuhi `Re-evaluation Trigger` objektif):**
  $\rightarrow$ Izinkan masuk sebagai `IDEA-ID` baru dan cantumkan referensi `Revived-From: MISTAKE-XXX`.
- **Kasus C (Menyempurnakan ide lama di `MEMORY.md` yang berstatus `PROVISIONAL_PASS`, `ON_HOLD`, atau `VALIDATED_ACTIVE`):**
  $\rightarrow$ Catat `IDEA-ID` baru dan ubah status ide lama menjadi `SUPERSEDED` dengan referensi `Superseded-By: IDEA-YYY`.

### Tahap 2: Registrasi Awal ke `MEMORY.md`
- Buat entri baru di `MEMORY.md` dengan format `IDEA-XXX`, `Status: DRAFT`, `Iteration: 0/3`, dan `Sync_State: SYNCED`.

### Tahap 3: Evaluasi Independen & Sesi Kritisi (4 Tes Kegagalan)
Ubah status di `MEMORY.md` menjadi `EVALUATING`, lalu uji kandidat ide secara berurutan terhadap 4 pertanyaan berikut (definisi detail ada di `MISTAKES.md`):
1. **Tes 1 — Problem Failure:** Apakah masalahnya benar-benar nyata, mendesak di objek tersebut, bebas dari bias variabel lain (*confounding factors*), dan didukung bukti?
2. **Tes 2 — Solution Failure:** Apakah solusi benar-benar menjawab akar masalah dan punya pembeda nyata dibanding produk komersial murah/solusi yang sudah ada?
3. **Tes 3 — Feasibility Failure:** Apakah realistis dijalankan dalam batasan waktu skripsi/riset, biaya, akses objek lapangan, dan standar keselamatan?
4. **Tes 4 — Anti-Hallucination Test:** Apakah setiap klaim teknis dan ambang batas memiliki dasar standar/data yang dapat dipertanggungjawabkan?

**Keputusan Tahap 3:**
- **Jika gagal mutlak pada salah satu dari 4 tes:** Jalankan **Protokol Kegagalan (Tahap 6)**.
- **Jika terdapat celah teknis yang dapat diperbaiki & `Iteration < 3`:** Ubah status menjadi `REVISING`, naikkan `Iteration + 1`, dan masuk ke **Tahap 4**.
- **Jika `Iteration >= 3` atau kendalanya berupa kebutuhan standar/data spesifik lapangan yang belum tersedia:** Ubah status menjadi `BLOCKED_PENDING_EVIDENCE` (atau `ON_HOLD` untuk tinjauan manusia) dan isi `Unblock_Trigger`.
- **Jika lolos keempat tes di tingkat konseptual:** Ubah status menjadi `PROVISIONAL_PASS` dan lanjut ke **Tahap 5**.

### Tahap 4: Siklus Revisi & *Blind Re-evaluation*
1. Lakukan perbaikan spesifik pada celah yang dikritisi dan simpan seluruh temuan/bukti baru ke dalam `Evidence_Log` di `MEMORY.md`.
2. Jika selama revisi tidak ditemukan solusi nyata selain asumsi baru, **hentikan revisi** dan jalankan **Protokol Kegagalan (Tahap 6)**.
3. Sebelum masuk kembali ke **Tahap 3**, terapkan aturan **Blind Re-evaluation** (`AGENTS.md` Bagian 3B): sembunyikan label status lama, pertahankan seluruh `Evidence_Log`, lalu evaluasi ulang secara independen.

### Tahap 5: Validasi Bukti Akhir
Untuk ide berstatus `PROVISIONAL_PASS`, lakukan verifikasi bukti empiris/simulasi/literatur primer:
- **Terbukti & realistis:** Ubah status di `MEMORY.md` menjadi `VALIDATED_ACTIVE`.
- **Bukti belum tersedia (menunggu eksperimen/data):** Ubah status menjadi `BLOCKED_PENDING_EVIDENCE` dan tetapkan `Unblock_Trigger`.
- **Terbukti tidak layak / asumsi gugur:** Jalankan **Protokol Kegagalan (Tahap 6)**.

### Tahap 6: Protokol Kegagalan & Transaksi Sinkronisasi Atomik
Setiap ide yang gagal (baik langsung dari `DRAFT`/`EVALUATING` maupun setelah sempat `PROVISIONAL_PASS` atau `REVISING`) **wajib** menjalani urutan berikut secara berurutan:
1. Ubah `Sync_State` pada `IDEA-XXX` di `MEMORY.md` menjadi `PENDING_SYNC`.
2. Buat entri baru `MISTAKE-XXX` di `MISTAKES.md` lengkap dengan kategori kegagalan, bukti penggugur, *anti-pattern*, dan `Re-evaluation Trigger`.
3. Perbarui `IDEA-XXX` di `MEMORY.md`:
   - `Status: FAILED_ARCHIVED`
   - `Mistake_Ref: MISTAKE-XXX`
   - `Sync_State: SYNCED`
4. Jalankan *Self-Verification Checklist* pada `SETUPS.md` sebelum menyelesaikan respons.
