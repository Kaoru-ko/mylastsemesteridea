# SETUPS.md — Konfigurasi Tunggal (Single-Layer Setup) & Protokol Verifikasi Mandiri

Dokumen ini adalah **satu-satunya lapis aktivasi** untuk seluruh ekosistem ideasi (`AGENTS.md`, `BRAINSTORMING.md`, `MEMORY.md`, dan `MISTAKES.md`). Tidak diperlukan skrip eksternal, *CI pipeline*, maupun folder konfigurasi tambahan.

---

## 1. Struktur Repositori Final (Flat 5-File Architecture)

```text
mylastsemesteridea/
├── SETUPS.md          # Titik masuk tunggal, blok skill AI, & checklist sinkronisasi
├── AGENTS.md          # Aturan perilaku agen, anti-bias, & kepatuhan bukti
├── BRAINSTORMING.md   # SOP alur kerja, Dual-Gate, & siklus status
├── MEMORY.md          # Single Source of Truth status seluruh IDEA-ID
└── MISTAKES.md        # Single Source of Truth arsip kegagalan & Re-evaluation Trigger
```

---

## 2. Blok Aktivasi Tunggal untuk Semua AI Agent / IDE

Gunakan blok instruksi di bawah ini sebagai *Custom Instructions*, *System Prompt*, atau referensi skill utama saat memulai sesi AI pada repositori ini:

```markdown
Baca dan patuhi seluruh aturan dalam ekosistem file berikut secara berurutan:
1. `SETUPS.md` (protokol aktivasi dan verifikasi sinkronisasi)
2. `AGENTS.md` (aturan anti-bias, larangan halusinasi solusi, dan kejujuran epistemik)
3. `BRAINSTORMING.md` (SOP Dual-Gate, 4 Tes Kegagalan, dan transisi status)
4. `MEMORY.md` (status terkini seluruh ide dan riwayat bukti)
5. `MISTAKES.md` (arsip ide gagal, anti-pattern, dan Re-evaluation Trigger)

Aturan Eksekusi Wajib:
- Sebelum menghasilkan atau mengkritisi ide, jalankan Gate 1 & Gate 2 dari `MEMORY.md` dan `MISTAKES.md`.
- Saat mengevaluasi ulang hasil revisi, terapkan Blind Re-evaluation (sembunyikan label status lama, pertahankan Evidence_Log).
- Jika ide gagal (termasuk yang awalnya layak), jalankan transaksi `PENDING_SYNC` -> tulis `MISTAKE-XXX` di `MISTAKES.md` -> ubah status `IDEA-XXX` di `MEMORY.md` menjadi `FAILED_ARCHIVED` + isi `Mistake_Ref` -> kembalikan `Sync_State: SYNCED`.
- Sebelum menutup respons atau menyimpan perubahan file `.md`, wajib lolos seluruh poin pada Self-Verification Checklist di `SETUPS.md`.
```

---

## 3. Protokol *Self-Verification Checklist* (Pengganti Skrip Eksternal)

Setiap kali agen memperbarui `MEMORY.md` atau `MISTAKES.md`, agen **wajib memeriksa 6 aturan deterministik berikut** sebelum menandai transaksi selesai:

1. **Zero Pending Sync:** Tidak ada satu pun entri di `MEMORY.md` yang tertinggal pada status `Sync_State: PENDING_SYNC`.
2. **Valid Status Enum:** Kolom `Status` pada `MEMORY.md` hanya boleh berisi salah satu dari 9 nilai resmi: `DRAFT`, `EVALUATING`, `PROVISIONAL_PASS`, `REVISING`, `BLOCKED_PENDING_EVIDENCE`, `ON_HOLD`, `VALIDATED_ACTIVE`, `FAILED_ARCHIVED`, atau `SUPERSEDED`.
3. **Referensi Silang Gagal 1-on-1 (`FAILED_ARCHIVED` $\leftrightarrow$ `MISTAKE-ID`):**
   - Setiap `IDEA-XXX` berstatus `FAILED_ARCHIVED` di `MEMORY.md` **wajib** memiliki `Mistake_Ref` yang merujuk ke `MISTAKE-XXX` yang benar-benar ada di `MISTAKES.md`.
   - Setiap `MISTAKE-XXX` di `MISTAKES.md` **wajib** merujuk balik ke `IDEA-XXX` yang berstatus `FAILED_ARCHIVED` di `MEMORY.md`.
4. **Kategori Kegagalan Valid:** Setiap entri di `MISTAKES.md` wajib menggunakan tepat satu dari 4 taksonomi resmi: `PROBLEM_FAILURE`, `SOLUTION_FAILURE`, `FEASIBILITY_FAILURE`, atau `HALLUCINATED_SOLUTION`.
5. **Kunci Kebangkitan Objektif:** Setiap entri di `MISTAKES.md` wajib memiliki `Re-evaluation Trigger` yang spesifik dan terukur (tidak boleh kosong atau `N/A`).
6. **Syarat Pembuka Blokir:** Setiap ide berstatus `BLOCKED_PENDING_EVIDENCE` atau `ON_HOLD` di `MEMORY.md` wajib memiliki `Unblock_Trigger` yang jelas mengenai data/bukti apa yang dibutuhkan untuk lanjut.
