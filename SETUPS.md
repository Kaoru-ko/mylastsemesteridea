# SETUPS.md — Konfigurasi Tunggal (Single-Layer Setup), Target Branch Git & Protokol Verifikasi

Dokumen ini adalah **satu-satunya lapis aktivasi** untuk seluruh ekosistem ideasi (`AGENTS.md`, `BRAINSTORMING.md`, `MEMORY.md`, `MISTAKES.md`, dan file laporan `IDEATION_REPORT.*`).

---

## 1. Target Repositori & Branch Wajib (Perkara Ide)

- **Repositori GitHub:** `https://github.com/Kaoru-ko/mylastsemesteridea`
- **Branch Wajib untuk Semua Urusan Ide:** `IdeJudulTA`
- **URL Branch Aktif:** `https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA`

> **Aturan Keras Git:** Setiap kali agen atau pengguna menambah ide, mengkritisi ide, merevisi, mengubah status di `MEMORY.md`, menambah arsip di `MISTAKES.md`, atau memperbarui file laporan, perubahan **wajib di-commit dan di-push ke branch `IdeJudulTA`** (bukan `main`).

```bash
git checkout -B IdeJudulTA
git add AGENTS.md BRAINSTORMING.md MEMORY.md MISTAKES.md SETUPS.md IDEATION_REPORT.xlsx IDEATION_REPORT.csv IDEATION_REPORT.txt
git commit -m "docs(ideation): update idea registry, mistakes, and reports"
git push -u origin IdeJudulTA
```

---

## 2. Struktur Repositori Final (Flat Architecture + Readable Reports)

```text
mylastsemesteridea/  (branch: IdeJudulTA)
├── SETUPS.md              # Titik masuk tunggal, blok skill AI, aturan branch IdeJudulTA & checklist
├── AGENTS.md              # Aturan perilaku agen, anti-bias, & kepatuhan bukti
├── BRAINSTORMING.md       # SOP alur kerja, Dual-Gate, siklus status & prosedur commit
├── MEMORY.md              # Single Source of Truth status seluruh IDEA-ID
├── MISTAKES.md            # Single Source of Truth arsip kegagalan & Re-evaluation Trigger
├── IDEATION_REPORT.xlsx   # Laporan Excel multi-tab (Dashboard, Daftar Ide, Arsip Kegagalan)
├── IDEATION_REPORT.csv    # Laporan CSV datar UTF-8 untuk pembacaan tabel cepat
└── IDEATION_REPORT.txt    # Laporan teks terstruktur untuk pembacaan cepat tanpa aplikasi spreadsheet
```

---

## 3. Blok Aktivasi Tunggal untuk Semua AI Agent / IDE

Gunakan blok instruksi di bawah ini sebagai *Custom Instructions*, *System Prompt*, atau referensi skill utama saat memulai sesi AI pada repositori ini:

```markdown
Baca dan patuhi seluruh aturan dalam ekosistem file berikut secara berurutan:
1. `SETUPS.md` (protokol aktivasi, aturan commit ke branch IdeJudulTA, dan checklist sinkronisasi)
2. `AGENTS.md` (aturan anti-bias, larangan halusinasi solusi, dan kejujuran epistemik)
3. `BRAINSTORMING.md` (SOP Dual-Gate, 4 Tes Kegagalan, transisi status, dan Tahap 7 commit)
4. `MEMORY.md` (status terkini seluruh ide dan riwayat bukti)
5. `MISTAKES.md` (arsip ide gagal, anti-pattern, dan Re-evaluation Trigger)

Aturan Eksekusi Wajib:
- Sebelum menghasilkan atau mengkritisi ide, jalankan Gate 1 & Gate 2 dari `MEMORY.md` dan `MISTAKES.md`.
- Saat mengevaluasi ulang hasil revisi, terapkan Blind Re-evaluation (sembunyikan label status lama, pertahankan Evidence_Log).
- Jika ide gagal (termasuk yang awalnya layak), jalankan transaksi `PENDING_SYNC` -> tulis `MISTAKE-XXX` di `MISTAKES.md` -> ubah status `IDEA-XXX` di `MEMORY.md` menjadi `FAILED_ARCHIVED` + isi `Mistake_Ref` -> kembalikan `Sync_State: SYNCED`.
- Setiap kali `MEMORY.md` atau `MISTAKES.md` diperbarui, perbarui juga `IDEATION_REPORT.xlsx`, `IDEATION_REPORT.csv`, dan `IDEATION_REPORT.txt`.
- Khusus perkara ide, wajib commit dan push perubahan ke branch `IdeJudulTA` (`https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA`).
- Sebelum menutup respons, pastikan seluruh 8 poin pada Self-Verification Checklist di `SETUPS.md` terpenuhi.
```

---

## 4. Protokol *Self-Verification Checklist* (8 Poin Wajib)

Setiap kali agen memperbarui catatan ide, agen **wajib memeriksa 8 aturan deterministik berikut** sebelum menandai tugas selesai:

1. **Zero Pending Sync:** Tidak ada satu pun entri di `MEMORY.md` yang tertinggal pada status `Sync_State: PENDING_SYNC`.
2. **Valid Status Enum:** Kolom `Status` pada `MEMORY.md` hanya berisi salah satu dari 9 nilai resmi: `DRAFT`, `EVALUATING`, `PROVISIONAL_PASS`, `REVISING`, `BLOCKED_PENDING_EVIDENCE`, `ON_HOLD`, `VALIDATED_ACTIVE`, `FAILED_ARCHIVED`, atau `SUPERSEDED`.
3. **Referensi Silang Gagal 1-on-1 (`FAILED_ARCHIVED` $\leftrightarrow$ `MISTAKE-ID`):**
   - Setiap `IDEA-XXX` berstatus `FAILED_ARCHIVED` di `MEMORY.md` **wajib** memiliki `Mistake_Ref` yang merujuk ke `MISTAKE-XXX` yang benar-benar ada di `MISTAKES.md`.
   - Setiap `MISTAKE-XXX` di `MISTAKES.md` **wajib** merujuk balik ke `IDEA-XXX` yang berstatus `FAILED_ARCHIVED` di `MEMORY.md`.
4. **Kategori Kegagalan Valid:** Setiap entri di `MISTAKES.md` wajib menggunakan tepat satu dari 4 taksonomi resmi: `PROBLEM_FAILURE`, `SOLUTION_FAILURE`, `FEASIBILITY_FAILURE`, atau `HALLUCINATED_SOLUTION`.
5. **Kunci Kebangkitan Objektif:** Setiap entri di `MISTAKES.md` wajib memiliki `Re-evaluation Trigger` yang spesifik dan terukur (tidak boleh kosong atau `N/A`).
6. **Syarat Pembuka Blokir:** Setiap ide berstatus `BLOCKED_PENDING_EVIDENCE` atau `ON_HOLD` di `MEMORY.md` wajib memiliki `Unblock_Trigger` yang jelas mengenai data/bukti apa yang dibutuhkan untuk lanjut.
7. **Sinkronisasi File Laporan:** Data pada `IDEATION_REPORT.xlsx`, `IDEATION_REPORT.csv`, dan `IDEATION_REPORT.txt` sesuai dengan status terbaru pada `MEMORY.md` dan `MISTAKES.md`.
8. **Target Branch Git Benar (`IdeJudulTA`):** Perintah atau proses commit/push diarahkan ke `https://github.com/Kaoru-ko/mylastsemesteridea/tree/IdeJudulTA` (branch `IdeJudulTA`).
