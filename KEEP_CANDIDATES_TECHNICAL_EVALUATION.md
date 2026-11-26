# Evaluasi Teknis Tiga Kandidat KEEP

**Tanggal:** 2026-11-26  
**Status kerja:** KEEP (dipertahankan sebagai kandidat)  
**Sifat dokumen:** evaluasi teknis, bukan penggantian judul  
**Catatan status:** `KEEP` adalah status kerja, bukan enum resmi. Registry resmi tetap memakai enum `SETUPS.md` (`DRAFT`, `EVALUATING`, `PROVISIONAL_PASS`, `REVISING`, `BLOCKED_PENDING_EVIDENCE`, `ON_HOLD`, `VALIDATED_ACTIVE`, `FAILED_ARCHIVED`, `SUPERSEDED`). Dokumen ini **tidak mengubah status resmi** sampai disetujui.

---

## 0. Ringkasan Eksekutif

| Kandidat | Putusan singkat | Temuan paling penting |
|---|---|---|
| **1 — Jamur tiram** | **Layak dikembangkan**, dengan koreksi target suhu | *Direct evaporative cooling* di iklim lembap hanya mampu menurunkan **±2–5 °C** dari suhu ambient. Target suhu harus disesuaikan dengan strain tropis, atau strategi dibuat hibrida. |
| **2 — Kualitas daya** | **Layak**, tetapi ini revisi `IDEA-027`, bukan ide baru | Harus memakai sensor/IC energi eksternal (bukan ADC internal ESP32), mendeklarasikan kelas pengukuran, dan mematuhi K3 panel. |
| **3 — Filamen** | **Layak secara teknik**, tetapi ada kesalahan atribusi standar | `ASTM D6980` adalah metode **kadar air by loss in weight**, bukan metode Tg. Tg diukur dengan DSC (`ASTM D3418`/`E1356`). Judul perlu direvisi atau Tg diukur di lab mitra. Ini revisi `IDEA-019`. |

**Prinsip yang dipakai:** judul asli dipertahankan; kritik diberikan spesifik; revisi judul hanya diusulkan sebagai alternatif, bukan pengganti otomatis; kompleksitas tidak otomatis dianggap alasan gugur.

---

## 1. Metode Evaluasi

### 1.1 Empat Tes Kegagalan
1. **PROBLEM_FAILURE** — masalah tidak nyata, tidak mendesak, atau bias oleh faktor lain.
2. **SOLUTION_FAILURE** — solusi tidak menjawab akar masalah, atau tidak punya diferensiasi nyata.
3. **FEASIBILITY_FAILURE** — tidak realistis dalam waktu, biaya, daya, akses, atau keselamatan.
4. **HALLUCINATED_SOLUTION** — klaim tanpa dasar teknis/empiris.

### 1.2 Label bukti
- **[F]** Fakta/standar yang dapat dirujuk. Edisi terbaru tetap perlu diverifikasi.
- **[H]** Hasil hitung penulis (reproducible, rumus dicantumkan).
- **[A]** Asumsi yang masih perlu diuji.
- **[R]** Risiko implementasi.
- **[V]** Perlu verifikasi sumber primer/edisi standar.

### 1.3 Keterbatasan sesi ini
Pencarian literatur daring langsung tidak tersedia pada sesi ini. Karena itu:
- Angka psikrometri dan ketidakseimbangan fasa dihitung dari prinsip fisika dan dapat direproduksi.
- Standar yang disebut adalah standar yang dikenal; **edisi, nomor bagian, dan nilai presisi belum diverifikasi ulang** dan ditandai `[V]` bila relevan.
- Tidak ada DOI atau sitasi baru yang dikarang.

---

# KANDIDAT 1 — Monitoring dan Pengendalian Lingkungan Budidaya Jamur

## 1.1 Identitas dan Judul Asli

**Judul asli (dipertahankan):**
> Pengendalian Suhu, Kelembapan & Sirkulasi Ruang Jamur Tiram

**Status kerja:** KEEP  
**Domain:** IoT/ kontrol lingkungan budidaya  
**Usulan registry (belum dijalankan):** `IDEA-035`, status awal `DRAFT` → `EVALUATING`.

## 1.2 Deskripsi Permasalahan

Budidaya jamur tiram membutuhkan lingkungan yang relatif stabil: suhu tidak terlalu tinggi, kelembapan tinggi, dan sirkulasi udara yang cukup. Di iklim tropis lembap, suhu siang dapat melampaui rentang nyaman untuk pembentukan tubuh buah, sementara kelembapan alami sudah tinggi. Petani kecil sering hanya mengandalkan kumbung terbuka dan penyemprotan manual, sehingga:
- suhu siang tidak terkendali;
- kelembapan fluktuatif;
- sirkulasi udara buruk;
- risiko kontaminasi meningkat saat kelembapan berlebih dan ventilasi kurang.

**Yang harus dibuktikan, bukan diasumsikan:** bahwa fluktuasi suhu/kelembapan di lokasi target benar-benar berada di luar rentang optimum, dan bahwa intervensi alat memberi perbaikan yang terukur (yield, waktu pinhead, kontaminasi).

## 1.3 Latar Belakang Teknis

### 1.3.1 Kebutuhan lingkungan jamur tiram
Literatur budidaya umumnya membedakan:
- **Fase miselium:** suhu lebih hangat (sekitar 24–28 °C).
- **Fase tubuh buah:** suhu lebih rendah (sekitar 15–24 °C, tergantung strain), RH sekitar 80–90%, dan CO₂ rendah.

Angka di atas adalah **rentang literatur budidaya** `[V]`; strain tropis (`Pleurotus pulmonarius`, `P. djamor`) umumnya lebih toleran suhu hangat daripada `P. ostreatus`. **Konsekuensi desain:** target suhu harus ditetapkan per strain, bukan generik “jamur tiram”.

### 1.3.2 Batas fisika evaporative cooling
Pada *direct evaporative cooling*, suhu udara keluar secara teoretis mendekati **wet-bulb** udara masuk. Semakin tinggi RH ambient, semakin kecil penurunan suhu yang mungkin.

**Hitungan [H]** menggunakan aproksimasi Stull untuk wet-bulb:

| Ambient T (°C) | RH (%) | Wet-bulb (°C) | Maks. penurunan (°C) |
|---:|---:|---:|---:|
| 30 | 60 | 24.0 | 6.0 |
| 30 | 70 | 25.6 | 4.4 |
| 30 | 80 | 27.1 | 2.9 |
| 32 | 70 | 27.5 | 4.5 |
| 32 | 80 | 29.0 | 3.0 |
| 34 | 70 | 29.3 | 4.7 |
| 34 | 80 | 31.0 | 3.0 |

**Implikasi:**
- Jika ambient 32 °C / 80% RH, outlet teoretis hanya sekitar **29 °C**. Ini **tidak cukup** untuk strain yang butuh 20–24 °C.
- Jika ambient 30 °C / 60% RH, outlet teoretis sekitar **24 °C** — baru masuk rentang beberapa strain.
- Efektivitas nyata alat (<100%) membuat penurunan aktual lebih kecil dari tabel.

**Kesimpulan teknis:** evaporative cooling **bukan pendingin ruang yang kuat** di iklim lembap; ia lebih tepat diposisikan sebagai **pengendali kelembapan + penurun suhu moderat**. Judul tetap dipertahankan, tetapi klaim “pengendalian suhu” harus dibatasi secara jujur.

### 1.3.3 Sizing awal
**Hitungan [H]** untuk beban sensibel sederhana (`Q = ρ·cp·V̇·ΔT`, air `ρ=1,2 kg/m³`, `cp=1005 J/kg·K`):

| Volume ruang | ACH | ΔT | Beban sensibel | Air teruapkan (teoretis) |
|---:|---:|---:|---:|---:|
| 2 m³ | 10 | 4 °C | 27 W | ±39 mL/jam |
| 6 m³ | 10 | 4 °C | 80 W | ±118 mL/jam |
| 20 m³ | 10 | 4 °C | 268 W | ±394 mL/jam |

Angka ini menunjukkan bahwa untuk prototype kecil, laju mist yang dibutuhkan relatif kecil; nozzle yang terlalu besar justru berisiko membasahi ruang. Sizing nozzle harus dihitung, bukan dipilih asal.

## 1.4 Konsep dan Prinsip Kerja

1. Sensor suhu/RH membaca kondisi ruang di beberapa titik.
2. Controller membandingkan dengan setpoint (suhu dan RH per fase/strain).
3. Jika suhu tinggi dan RH belum jenuh, pompa menyalakan nozzle mist; penguapan menyerap panas (evaporative cooling).
4. Kipas exhaust membuang udara panas/lembap dan menarik udara segar; kipas sirkulasi mencampur udara.
5. Logika mencegah kelembapan berlebih: mist berhenti jika RH mendekati batas atas; exhaust aktif jika RH terlalu tinggi atau CO₂ tinggi.
6. Data dikirim ke dashboard (Wi-Fi/MQTT) dan dicatat untuk analisis.

**Prinsip yang harus dipegang:** mist **menambah** kelembapan. Di ruang yang sudah lembap, mist yang tidak teruapkan akan membasahi permukaan dan meningkatkan risiko kontaminasi. Karena itu kontrol RH dan ventilasi bukan pelengkap, melainkan bagian inti keselamatan biologis.

## 1.5 Arsitektur Sistem

```
[SHT31/SHT85 x3] [DS18B20 substrat] [CO2 opsional]
        │
        ▼
   [ESP32]──►[Relay/MOSFET]──►[Pompa mist + solenoid]
        │                └──►[Kipas exhaust PWM]
        │                └──►[Kipas sirkulasi]
        ├──►[RTC] ──►[SD card]
        ├──►[LCD/OLED]
        └──►[Wi-Fi/MQTT] ──►[Dashboard]
```

**Titik sensor:** minimal 3 titik pada ketinggian kanopi, terlindung dari semprotan langsung, dengan shield radiasi sederhana. Rata-rata dan sebaran antar-titik dilaporkan (uniformity), bukan hanya satu angka.

## 1.6 Komponen yang Diperlukan

| Kelompok | Komponen | Catatan |
|---|---|---|
| Sensor | SHT31/SHT85, DS18B20 | SHT31 lebih baik dari DHT22 untuk riset RH |
| Aktuator | Pompa diafragma, solenoid, nozzle fogger | Hitung laju mist; siapkan filter air |
| Udara | Kipas DC 12 V (exhaust + sirkulasi) | PWM; arah aliran harus benar |
| Kontrol | ESP32, relay/MOSFET, RTC | Pisahkan jalur 220 V dan 12 V |
| Keselamatan | RCD/GFCI, sekring, enclosure IP65 | Air + listrik = risiko utama |
| Data | SD card, dashboard MQTT | Log interval 1–5 menit |
| Kalibrasi | Thermohygrometer referensi | Untuk validasi sensor |

## 1.7 Metode Pengujian

### 1.7.1 Karakterisasi fisika (tanpa jamur)
- Tempatkan alat di ruang uji; rekam ambient vs outlet selama 24–72 jam.
- Bandingkan penurunan suhu aktual dengan batas wet-bulb yang dihitung.
- Ukur uniformity suhu/RH di 3–5 titik.
- Ukur konsumsi air dan listrik per °C penurunan.

### 1.7.2 Validasi sensor (apple-to-apple)
- Co-location SHT31 vs thermohygrometer referensi; sampel waktu sama.
- Laporkan bias, RMSE, dan limits of agreement.

### 1.7.3 Uji biologis (apple-to-apple)
- Substrat dan bibit dari batch yang sama; acak posisi baglog.
- Perlakuan: ruang terkontrol vs ruang kontrol (tanpa alat).
- Minimal 3 ulangan per perlakuan; catat waktu pinhead, jumlah tubuh buah, bobot panen, biological efficiency, dan kontaminasi.
- **Ground truth** adalah pengukuran manual, bukan persepsi.

**Kriteria lulus yang disarankan:**
- Sensor: RMSE suhu ≤0,5 °C; RMSE RH ≤5% RH (disesuaikan kelas sensor).
- Fisika: penurunan suhu aktual ≥70% dari batas wet-bulb teoretis pada kondisi uji.
- Biologi: perbedaan yield/contamination yang terukur dan dapat diulang, bukan hanya “tumbuh lebih baik”.

## 1.8 Risiko dan Keterbatasan

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Wet-bulb limit | Target suhu tidak tercapai di RH tinggi | Pilih strain tropis; target 26–29 °C; hybrid cooling |
| Kelembapan berlebih | Kontaminasi, pembusukan | Kontrol RH + exhaust; anti-short-cycle; sensor RH terkalibrasi |
| Nozzle clogging | Mist tidak konsisten | Filter air; nozzle mudah dibersihkan; alarm flow |
| Sensor drift | Keputusan salah | Kalibrasi berkala; sensor reference |
| Listrik + air | Keselamatan | RCD, IP65, grounding, pemisahan jalur |
| Uji biologis lama | Waktu | Mulai uji fisika lebih dulu; siapkan jadwal baglog |

**Batas klaim:** jangan mengklaim “menurunkan suhu hingga X °C” tanpa menyebut RH ambient. Penurunan suhu selalu bergantung pada wet-bulb.

## 1.9 Potensi Pengembangan

- Kontrol CO₂ dan cahaya.
- Dashboard remote + log panen.
- Modul kumbung surya.
- Kontrol per zona (multi-ruang).
- Integrasi prediksi risiko kontaminasi.

## 1.10 Catatan Evaluasi dan Keputusan

**Empat tes:**
- **PROBLEM:** lolos bersyarat. Masalah nyata, tetapi baseline lokasi target harus diukur.
- **SOLUTION:** lolos bersyarat. Solusi relevan, tetapi bukan pendingin kuat; klaim harus dibatasi.
- **FEASIBILITY:** lolos. Komponen murah dan tersedia; risiko utama adalah disiplin kontrol RH dan keselamatan listrik.
- **ANTI-HALLUCINATION:** lolos, asalkan target suhu per strain dan batas wet-bulb dinyatakan eksplisit.

**Keputusan:** **KEEP — lanjutkan**. Revisi judul **tidak diperlukan** untuk saat ini. Alternatif judul hanya jika ingin menegaskan batas fisika:
> *Pengendalian Suhu, Kelembapan & Sirkulasi Ruang Jamur Tiram Berbasis Evaporative Cooling dan Ventilasi Adaptif*

---

# KANDIDAT 2 — Monitoring Kualitas Daya Listrik

## 2.1 Identitas dan Judul Asli

**Judul asli (dipertahankan):**
> Rancang Bangun Sistem Pemantauan Kualitas Daya Listrik dan Deteksi Dini Ketidakseimbangan Beban Fasa pada Panel Distribusi Gedung Menggunakan Sensor Energi Multi-Kanal dan ESP32

**Status kerja:** KEEP  
**Domain:** IoT/ metrologi kelistrikan  
**Catatan registry:** ini **revisi lingkup `IDEA-027`**, bukan ide baru. Status resmi yang disarankan: `REVISING` (bukan `DRAFT` baru).

## 2.2 Deskripsi Permasalahan

Panel distribusi gedung dapat mengalami ketidakseimbangan beban antarfasa. Akibatnya:
- arus netral meningkat;
- rugi daya dan pemanasan tidak merata;
- umur peralatan turun;
- risiko trip/overload meningkat.

Pemantauan manual berkala tidak menangkap dinamika harian. Diperlukan pemantauan kontinu yang dapat:
- mengukur V, I, P, PF, E per fasa;
- menghitung ketidakseimbangan;
- memberi peringatan dini;
- menyimpan data untuk analisis.

**Yang harus dibuktikan:** bahwa panel target memang mengalami ketidakseimbangan yang bermakna, dan bahwa ambang alarm yang dipilih masuk akal secara teknis (bukan angka asal).

## 2.3 Latar Belakang Teknis

### 2.3.1 Definisi ketidakseimbangan
Untuk tegangan, definisi yang lazim (NEMA MG 1) adalah:

```
% unbalance = 100 × max|V_i − V_avg| / V_avg
```

**Contoh [H]:**
- 220, 230, 225 V → rata-rata 225 V; deviasi maks 5 V → **2,22%**.
- 220, 221, 219 V → rata-rata 220 V; deviasi maks 1 V → **0,45%**.

Untuk arus, prinsip yang sama dapat dipakai, tetapi **beban tidak seimbang adalah kondisi normal** pada instalasi gedung; yang perlu dideteksi adalah ketidakseimbangan **berlebihan/berkelanjutan**, bukan setiap selisih.

### 2.3.2 Akurasi dan arsitektur sensor
ADC internal ESP32 (12-bit, non-linear, sampling terbatas) **tidak memadai** untuk klaim kualitas daya yang serius. Tiga opsi:

| Opsi | Kelebihan | Kekurangan | Cocok untuk |
|---|---|---|---|
| **A. 3× modul energi 1 fasa** (mis. PZEM-004T) | Murah, mudah, UART | Tidak sampling simultan; akurasi kelas modul; kalibrasi terbatas | Prototype awal, pemantauan indikatif |
| **B. Modul energi 3 fasa** (Modbus, mis. kelas panel) | Akurat, simultan, siap pakai | Kurang “membangun”; biaya lebih tinggi | Tesis yang menekankan validasi & implementasi |
| **C. IC metering 3 fasa** (mis. ADE9000) | Akurasi tinggi, simultan, fleksibel | Perlu PCB, isolasi, kalibrasi | Tesis yang menekankan rekayasa hardware |

**Rekomendasi:** pilih **B** untuk kelayakan, atau **C** jika ingin kontribusi hardware yang kuat. Opsi **A** hanya untuk prototipe dan harus disebut “indikatif”.

### 2.3.3 Propagasi error ketidakseimbangan
**Hitungan [H]:** dengan arus seimbang 10, 12, 8 A (imbalance 20%) dan noise per kanal 1% (standar deviasi), error indeks imbalance berada sekitar **−0,9% hingga +1,6%** (persentil 5–95). Artinya:
- Untuk alarm ambang 10%, noise 1% masih dapat diterima.
- Untuk mendeteksi perubahan halus (mis. 1–2%), diperlukan sensor kelas lebih baik dan kalibrasi.

### 2.3.4 Keselamatan
Pengukuran pada panel distribusi melibatkan tegangan berbahaya. Wajib:
- izin dan pengawasan teknisi berlisensi;
- CT dan voltage tap yang sesuai;
- isolasi, sekring, enclosure;
- PPE, LOTO, prosedur kerja;
- uji di panel simulator/bench dulu.

## 2.4 Konsep dan Prinsip Kerja

1. CT memasang pada tiap fasa; voltage tap mengambil tegangan fasa-netral/fasa-fasa.
2. Sensor energi mengukur V, I, P, PF, E, frekuensi per fasa.
3. ESP32 membaca data, menghitung rata-rata dan indeks imbalance.
4. Logika deteksi: ambang + durasi (persistence) + tren; alarm jika melewati batas selama N menit.
5. Data disimpan (SD/RTC) dan dikirim ke dashboard.
6. Alarm lokal (buzzer/LED) dan/atau notifikasi.

**Prinsip:** alarm harus **tahan noise** dan **tidak membuat panik**. Gunakan moving average, hysteresis, dan pencatatan snapshot sebelum/sesudah alarm.

## 2.5 Arsitektur Sistem

```
[CT x3] [Voltage tap x3] ──► [Sensor energi 3 fasa / IC metering]
                                      │ (SPI/UART/Modbus)
                                      ▼
                                  [ESP32]
                                   ├──► [RTC + SD]
                                   ├──► [LCD/OLED + buzzer]
                                   └──► [Wi-Fi/MQTT] ──► [Dashboard]
```

**Isolasi:** gunakan modul dengan isolasi galvani; jangan menghubungkan tegangan panel langsung ke GPIO.

## 2.6 Komponen yang Diperlukan

| Kelompok | Komponen | Catatan |
|---|---|---|
| Sensor | 3 fasa energy meter / ADE9000 / 3× PZEM | Pilih sesuai klaim akurasi |
| CT | CT kelas 0,5/1, rasio sesuai arus | Burden harus cocok |
| Proteksi | Sekring, MOV/TVS, isolasi | Jangan kompromi |
| Kontrol | ESP32, RTC, SD | Watchdog + logging |
| Tampilan | LCD/OLED, buzzer/LED | Alarm lokal |
| Kalibrasi | Power meter/PQ analyzer referensi | Untuk apple-to-apple |
| Keselamatan | PPE, enclosure, label, LOTO | Wajib |

## 2.7 Metode Pengujian

### 2.7.1 Uji bench (apple-to-apple)
- Sumber 3 fasa / panel simulator dengan beban resistif.
- Skenario: seimbang, tidak seimbang ringan, tidak seimbang berat.
- Bandingkan V, I, P, PF, E, dan indeks imbalance dengan **power meter referensi** pada titik dan waktu yang sama.
- Laporkan bias, RMSE, dan error maksimum per parameter.

### 2.7.2 Uji panel nyata
- Dengan izin dan pengawasan; pasang CT/tap pada panel target.
- Bandingkan dengan analyzer referensi selama periode yang sama.
- Uji alarm: simulasi beban tidak seimbang (jika aman) atau analisis data historis.

### 2.7.3 Kriteria lulus yang disarankan
- V/I: error ≤1–2% dari referensi (sesuai kelas sensor).
- P/PF: error ≤2–3%.
- Imbalance: error absolut ≤1–2 poin persentase.
- Alarm: tidak ada false alarm berlebihan pada beban normal; alarm muncul pada kondisi uji yang disengaja.

## 2.8 Risiko dan Keterbatasan

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Keselamatan panel | Cedera/kerusakan | Bench dulu; teknisi berlisensi; LOTO; PPE |
| Akurasi sensor murah | Klaim berlebihan | Pilih kelas sensor; kalibrasi; deklarasikan batas |
| Tidak sampling simultan | Error pada beban non-linear | Gunakan IC/modul 3 fasa simultan |
| EMI | Data kacau | Shield, filter, grounding |
| Akses panel | Proyek terhenti | Surat izin; panel simulator |
| Alarm fatigue | Alarm diabaikan | Ambang + durasi + hysteresis |

**Batas klaim:** jika hanya mengukur V, I, P, PF, E, dan imbalance, sebut sebagai **pemantauan kualitas daya fundamental**, bukan “power quality analyzer kelas A”. Harmonisa/transien memerlukan perangkat dan metode tambahan.

## 2.9 Potensi Pengembangan

- Harmonisa/THD jika hardware mendukung.
- Analisis beban (load disaggregation).
- Deteksi anomali berbasis tren.
- Integrasi cloud dan laporan otomatis.
- Kontrol beban otomatis (load shedding).

## 2.10 Catatan Evaluasi dan Keputusan

**Empat tes:**
- **PROBLEM:** lolos bersyarat. Perlu data awal panel target.
- **SOLUTION:** lolos. Solusi relevan; diferensiasi ada pada pemantauan kontinu + alarm + logging.
- **FEASIBILITY:** lolos dengan catatan keselamatan; bench wajib sebelum panel nyata.
- **ANTI-HALLUCINATION:** lolos jika kelas pengukuran dan batas akurasi dinyatakan.

**Keputusan:** **KEEP — lanjutkan sebagai revisi `IDEA-027`**. Judul asli dipertahankan. Alternatif judul (bukan pengganti otomatis) untuk menegaskan batas:
> *… Menggunakan Sensor Energi Tiga Fasa dan ESP32: Pemantauan Kualitas Daya Fundamental dan Deteksi Ketidakseimbangan Beban*

---

# KANDIDAT 3 — Pengkondisian dan Pengeringan Filamen Polimer

## 3.1 Identitas dan Judul Asli

**Judul asli (dipertahankan):**
> Rancang Bangun Sistem Pengkondisi dan Pengering Filamen Polimer Higroskopis Otomatis Berbasis Kendali Dew-Point (Delta-AH), Gravimetri In-Situ, dan Profil Suhu Transisi Gelas Tg (ASTM D6980)

**Status kerja:** KEEP  
**Domain:** IoT/ kontrol proses + karakterisasi material  
**Catatan registry:** ini **revisi `IDEA-019`**, bukan ide baru. Status resmi yang disarankan: `REVISING`.

## 3.2 Deskripsi Permasalahan

Filamen polimer higroskopis (PLA, PETG, TPU, PA/nylon, PC, PVA) menyerap uap air dari udara. Filamen basah menyebabkan:
- gelembung/uap saat ekstrusi;
- stringing dan permukaan kasar;
- penurunan kekuatan antarlapisan;
- variasi dimensi.

Pengeringan berbasis timer/suhu saja tidak mengetahui kapan filamen benar-benar kering. Diperlukan sistem yang:
- mengukur kondisi udara (dew point/ΔAH);
- memantau perubahan massa filamen secara in-situ;
- membatasi suhu pengeringan terhadap Tg material;
- mencatat proses untuk audit.

**Yang harus dibuktikan:** bahwa kadar air awal filamen di lokasi target cukup tinggi untuk menimbulkan masalah cetak, dan bahwa pengeringan terkontrol memberi perbaikan terukur dibanding dryer komersial/oven.

## 3.3 Latar Belakang Teknis

### 3.3.1 ASTM D6980 — apa yang sebenarnya diukur
`ASTM D6980` adalah **Standard Test Method for Determination of Moisture in Plastics by Loss in Weight** `[F][V]`. Metode ini mengukur **kehilangan massa** sampel plastik saat dipanaskan dalam moisture analyzer; hasilnya adalah kadar air (loss on drying), bukan Tg.

**Konsekuensi:** frasa “Profil Suhu Transisi Gelas Tg (ASTM D6980)” **salah atribusi**. Tg diukur dengan:
- **DSC** — `ASTM D3418` atau `ASTM E1356` `[F][V]`;
- **DMA** — `ASTM D7028` `[F][V]` (jika ingin sifat mekanik dinamis).

Ini bukan alasan menggugurkan judul; ini alasan **merevisi klaim** atau **menyediakan akses DSC**.

### 3.3.2 Dew point dan Delta-AH
Kelembapan absolut (AH) menentukan kandungan uap air di udara. Pengeringan efektif terjadi ketika AH udara pengering lebih rendah dari AH kesetimbangan filamen. ΔAH = AH ambient − AH setpoint adalah **driving force** pengeringan.

**Hitungan [H]** (ambient 30 °C/70% RH, AH ≈ 21,2 g/m³):

| Target | AH target (g/m³) | ΔAH (g/m³) | Mixing ratio (g/kg) |
|---|---:|---:|---:|
| 45 °C/15% | 9,8 | 11,4 | 9,0 |
| 50 °C/10% | 8,3 | 12,9 | 7,7 |
| 55 °C/10% | 10,5 | 10,8 | 9,9 |
| 60 °C/10% | 13,1 | 8,2 | 12,6 |

**Implikasi:** semakin tinggi suhu, semakin tinggi AH pada RH yang sama; karena itu **suhu dan RH harus dikendalikan bersama**, bukan suhu saja.

### 3.3.3 Gravimetri in-situ
**Hitungan [H]** resolusi yang dibutuhkan:

| Massa spool | 0,01% air | 0,05% | 0,1% | 0,2% |
|---:|---:|---:|---:|---:|
| 500 g | 0,05 g | 0,25 g | 0,50 g | 1,00 g |
| 1000 g | 0,10 g | 0,50 g | 1,00 g | 2,00 g |
| 2000 g | 0,20 g | 1,00 g | 2,00 g | 4,00 g |

Untuk spool 1 kg, mendeteksi 0,01% air berarti resolusi **0,1 g** pada rentang 1–2 kg (rasio 1:10.000–1:20.000). Ini mungkin dengan load cell + HX711 dan mekanika yang kaku, tetapi **drift suhu dan tara spool** adalah musuh utama. Karena itu:
- gunakan load cell dengan kapasitas tepat (jangan 5 kg untuk beban 1 kg);
- lakukan tare otomatis saat kondisi stabil;
- kompensasi suhu atau jaga suhu ruang;
- validasi terhadap ASTM D6980.

### 3.3.4 Suhu pengeringan vs Tg
Suhu pengeringan harus berada di bawah Tg material (atau mengikuti rekomendasi pabrikan) untuk menghindari deformasi spool dan perubahan sifat. Rentang tipikal (perlu verifikasi datasheet material) `[V]`:
- PLA: sekitar 45–50 °C;
- PETG: sekitar 60–65 °C;
- TPU: sekitar 40–50 °C;
- PA/nylon: sekitar 70–80 °C (perhatikan Tg kering yang rendah);
- PC: sekitar 80–100 °C;
- PVA: sekitar 45–55 °C.

**Jangan** menetapkan satu suhu untuk semua material. Profil material harus menjadi parameter sistem.

## 3.4 Konsep dan Prinsip Kerja

1. Pengguna memilih profil material (PLA/PETG/PA/…).
2. Sistem menetapkan batas suhu (di bawah Tg) dan target dew point/ΔAH.
3. Heater + fan menaikkan suhu; exhaust/vent membuang udara lembap.
4. Sensor RH/suhu menghitung dew point dan ΔAH secara kontinu.
5. Load cell memantau massa filamen; laju perubahan massa (`dm/dt`) digunakan untuk deteksi endpoint.
6. Pengeringan berhenti ketika `dm/dt` mendekati nol atau kadar air estimasi di bawah ambang.
7. Sistem mendinginkan sebelum spool dikeluarkan; log disimpan.

**Prinsip:** gravimetri adalah **ground truth internal**; dew point adalah **kondisi proses**; Tg adalah **batas keselamatan material**.

## 3.5 Arsitektur Sistem

```
[SHT31/SHT85] [PT100/MAX31865] [Load cell + HX711]
        │              │              │
        └──────────────┴──────────────┘
                       ▼
                   [ESP32]
                    ├──► [SSR/Relay] ──► [Heater]
                    ├──► [MOSFET] ────► [Fan/exhaust]
                    ├──► [RTC + SD]
                    ├──► [OLED + buzzer]
                    └──► [Wi-Fi/MQTT] ──► [Dashboard]
```

**Mekanik:** chamber terisolasi, aliran udara merata, spool holder yang tidak menambah gaya gesek, load cell terpisah dari jalur panas.

## 3.6 Komponen yang Diperlukan

| Kelompok | Komponen | Catatan |
|---|---|---|
| Sensor | SHT31/SHT85, PT100 + MAX31865 | RH/temp presisi |
| Massa | Load cell 1–2 kg + HX711 | Resolusi 0,1 g; mekanika kaku |
| Aktuator | Heater PTC/cartridge, fan, exhaust | SSR; proteksi over-temp |
| Kontrol | ESP32, RTC, SD | Watchdog; logging |
| Keselamatan | Sekring, thermal fuse, enclosure | Heater + plastik = risiko |
| Validasi | Moisture analyzer/oven (ASTM D6980), DSC | DSC untuk Tg |
| Cetak | Printer 3D + filamen uji | Untuk uji kekuatan/print quality |

## 3.7 Metode Pengujian

### 3.7.1 Validasi sensor dan gravimetri
- Co-location SHT31 vs reference; hitung bias/RMSE.
- Uji load cell dengan anak timbangan; uji drift 1–2 jam; uji repeatability.
- Bandingkan hasil gravimetri in-situ dengan **ASTM D6980** pada sampel yang sama.

### 3.7.2 Uji pengeringan apple-to-apple
- Kondisikan filamen pada RH tinggi sampai kadar air awal seragam.
- Bagi menjadi beberapa spool: (a) sistem usulan, (b) dryer komersial, (c) oven/referensi.
- Waktu dan suhu disamakan atau dijadikan variabel.
- Ukur: massa (ASTM D6980), Tg (DSC), kuat tarik (ASTM D638), dan kualitas cetak.
- Minimal 3 ulangan per kondisi.

### 3.7.3 Kriteria lulus yang disarankan
- Gravimetri: error kadar air ≤0,05–0,1% dibanding ASTM D6980.
- Endpoint: sistem berhenti pada kadar air target ±0,05%.
- Tg: tidak ada penurunan Tg signifikan akibat pengeringan (jika DSC tersedia).
- Cetak: penurunan cacat (gelembung/stringing) terukur.

## 3.8 Risiko dan Keterbatasan

| Risiko | Dampak | Mitigasi |
|---|---|---|
| ASTM D6980 salah atribusi untuk Tg | Klaim tidak valid | Revisi judul/klaim; DSC untuk Tg |
| Tidak ada akses DSC | Tg tidak terukur | Lab mitra; ganti klaim ke suhu di bawah Tg literatur |
| Load cell drift | Endpoint salah | Tare, kompensasi suhu, validasi gravimetri |
| Dryer komersial murah | Diferensiasi lemah | Fokus ke endpoint + dew point + material engineering |
| Heater + plastik | Kebakaran/leleh | Thermal fuse, over-temp cutoff, enclosure |
| Waktu uji | Lama | Mulai dari uji sensor/gravimetri |

**Batas klaim:** jika DSC tidak tersedia, jangan mengklaim “profil Tg terukur”. Klaim yang jujur: “suhu pengeringan dibatasi di bawah Tg literatur; Tg tidak diukur”.

## 3.9 Potensi Pengembangan

- Profil material otomatis (RFID/NFC).
- Multi-spool.
- Integrasi printer (menghentikan cetak jika kadar air tinggi).
- Cloud logging + predictive maintenance.
- Desiccant assist untuk iklim lembap.

## 3.10 Catatan Evaluasi dan Keputusan

**Empat tes:**
- **PROBLEM:** lolos. Filamen higroskopis memang menyerap air; dampak cetak nyata.
- **SOLUTION:** lolos bersyarat. Diferensiasi vs dryer murah harus jelas: endpoint gravimetri + dew point + profil material.
- **FEASIBILITY:** lolos bersyarat. DSC adalah dependensi; load cell 0,1 g menantang tetapi mungkin.
- **ANTI-HALLUCINATION:** **gagal pada judul saat ini** karena `ASTM D6980` bukan metode Tg. Harus direvisi.

**Keputusan:** **KEEP — lanjutkan sebagai revisi `IDEA-019`**. Judul asli dipertahankan sebagai referensi. Alternatif judul (bukan pengganti otomatis):
> *Rancang Bangun Sistem Pengkondisi dan Pengering Filamen Polimer Higroskopis Otomatis Berbasis Kendali Dew-Point (Delta-AH), Gravimetri In-Situ, dan Batas Suhu Transisi Gelas (Tg) dengan Validasi ASTM D6980 dan DSC*

---

# 4. Perbandingan Ketiga Kandidat

| Kriteria | Kandidat 1 — Jamur | Kandidat 2 — Kualitas Daya | Kandidat 3 — Filamen |
|---|---|---|---|
| **Kompleksitas** | Sedang | Sedang–Tinggi | Tinggi |
| **Kebaruan** | Sedang | Sedang | Sedang–Tinggi (jika Tg terukur) |
| **Risiko teknis** | Sedang (wet-bulb, kontaminasi) | Tinggi (keselamatan panel) | Tinggi (DSC, load cell) |
| **Biaya** | Rendah–Sedang | Sedang | Sedang |
| **Kelayakan prototipe** | Tinggi | Tinggi (dengan pengawasan) | Sedang |
| **Validasi** | Sensor + biologis | Meter referensi | ASTM D6980 + DSC |
| **Waktu pengerjaan** | Panjang (siklus jamur) | Sedang | Sedang–Panjang |
| **Dependensi akses** | Rendah | Tinggi (panel) | Tinggi (DSC) |
| **Potensi dampak** | Tinggi untuk petani jamur | Tinggi untuk gedung | Sedang (pengguna printer 3D) |

### Peringkat kelayakan untuk dikerjakan lebih dulu
1. **Kandidat 2** — paling terukur dan cepat divalidasi, asalkan keselamatan panel direncanakan.
2. **Kandidat 1** — dampak nyata, tetapi butuh waktu biologis dan koreksi target suhu.
3. **Kandidat 3** — paling rawan klaim; harus bereskan Tg/ASTM D6980 lebih dulu.

---

# 5. Keputusan dan Langkah Berikutnya

## 5.1 Status
Ketiga kandidat tetap **KEEP**. Tidak ada yang digugurkan. Tidak ada judul yang diganti secara sepihak.

## 5.2 Mapping ke registry resmi (usulan, belum dijalankan)
| Kandidat | Registry | Status resmi yang disarankan |
|---|---|---|
| 1 — Jamur | `IDEA-035` (baru) | `DRAFT` → `EVALUATING` |
| 2 — Kualitas daya | revisi `IDEA-027` | `REVISING` |
| 3 — Filamen | revisi `IDEA-019` | `REVISING` |

## 5.3 Verifikasi yang harus dilakukan sebelum lanjut
1. **Kandidat 1:** ukur baseline suhu/RH di lokasi; tetapkan strain dan target suhu; hitung wet-bulb lokasi.
2. **Kandidat 2:** dapatkan izin panel; pilih arsitektur sensor (A/B/C); siapkan meter referensi.
3. **Kandidat 3:** konfirmasi akses DSC; verifikasi edisi ASTM D6980/D3418/E1356; uji resolusi load cell.

## 5.4 Catatan epistemik
- Angka psikrometri dan propagasi error adalah hitungan sendiri, bukan klaim literatur.
- Standar yang disebut belum diverifikasi edisinya pada sesi ini.
- Tidak ada DOI baru yang dikarang.
- Status resmi belum diubah; dokumen ini adalah bahan evaluasi.

---

# Lampiran A — Deep Dive Kandidat 2 & 3 (2026-11-26)

## A.1 Kandidat 2 — Kualitas Daya: Angka dan Logika Build

### A.1.1 Apakah benar dibutuhkan?
- **Ya, untuk gedung yang belum punya pemantauan per fasa.** Banyak gedung kecil/menengah hanya punya kWh meter total; ketidakseimbangan fasa tidak terlihat.
- **Nilainya bukan pada sensor**, tetapi pada: (a) data kontinu per fasa, (b) alarm ketidakseimbangan, (c) rekomendasi redistribusi beban.
- **Jika panel target sudah punya 3-phase meter dengan Modbus/cloud**, nilai tambah alat ini turun menjadi dashboard/alarm lokal. Harus dicek sebelum build.

### A.1.2 Angka penting
Neutral current untuk beban resistif seimbang fasa (`I_N = |I_a + I_b∠−120° + I_c∠120°|`) `[H]`:

| Arus fasa (A) | Arus netral (A) |
|---|---:|
| 10, 10, 10 | 0,0 |
| 10, 12, 8 | 3,46 |
| 16, 8, 8 | 8,00 |
| 20, 20, 4 | 16,00 |

Artinya: ketidakseimbangan 20 A vs 4 A menghasilkan arus netral 16 A — cukup untuk memanaskan netral dan menurunkan kapasitas.

Propagasi error indeks imbalance (noise 1% per kanal): sekitar **−0,9% sampai +1,6%** pada persentil 5–95. Alarm ambang 10% masih aman; deteksi perubahan 1–2% butuh sensor lebih baik.

### A.1.3 Arsitektur yang paling logis
**Rekomendasi: modul energi 3 fasa (Modbus) + ESP32.**
- Meter 3 fasa tersertifikasi memberi pengukuran simultan, isolasi, dan akurasi yang bisa dipertanggungjawabkan.
- ESP32 menjadi Modbus RTU master (RS485) atau Modbus TCP.
- Tambahan: RTC, SD, OLED, buzzer, Wi-Fi/MQTT, dashboard.
- Opsi murah 3× PZEM-004T: boleh untuk prototipe, tetapi **tidak simultan** dan kelas akurasinya lebih rendah.
- Opsi ADE9000: kontribusi hardware paling kuat, tetapi risiko PCB/isolasi/kalibrasi tinggi untuk satu semester.

### A.1.4 Tahapan build
1. Tetapkan lingkup: kualitas daya **fundamental** (V, I, P, PF, E, imbalance), bukan Class A.
2. Bench: meter + ESP32 + beban bank; baca register Modbus; verifikasi V/I/P/PF/E.
3. Kalibrasi: bandingkan dengan power meter referensi; hitung error budget.
4. Algoritma: NEMA imbalance + persistence + hysteresis + snapshot.
5. Dashboard: real-time, histori, alarm.
6. Lapangan: pemasangan oleh teknisi berlisensi; koleksi data 2–4 minggu.
7. Analisis: profil imbalance, arus netral, rekomendasi redistribusi.

### A.1.5 Gate go/no-go
- **GO** jika: ada panel target yang aman diakses, meter referensi, dan teknisi berlisensi.
- **NO-GO sementara** jika: tidak ada akses panel. Alternatif: panel simulator + klaim “prototipe laboratorium”.

### A.1.6 Berguna jangka panjang?
Ya. Pemantauan energi adalah kebutuhan berkelanjutan; data dan algoritma tetap berguna meski hardware diganti. Nilai tesis ada pada integrasi, kalibrasi, dan protokol tindakan — bukan pada penemuan sensor baru.

---

## A.2 Kandidat 3 — Filamen: Angka dan Logika Build

### A.2.1 Apakah benar dibutuhkan?
- **Untuk filamen engineering (PA/nylon, PC, PVA, PETG basah): ya.** Kadar air tinggi menyebabkan gelembung, stringing, dan kekuatan antarlapis turun.
- **Untuk PLA hobbyist: tidak selalu.** Dryer komersial murah sudah cukup untuk banyak kasus.
- **Pembeli yang lebih realistis:** laboratorium 3D printing kampus atau unit produksi yang memakai filamen engineering — bukan konsumen rumahan. Ini menghindari jebakan adopsi seperti pada ide kadar air gabah.

### A.2.2 Angka penting: paradoks pemanasan
Ambient 30 °C/70% RH → AH ≈ 21,2 g/m³, dew point ≈ 23,9 °C.

Jika udara dipanaskan pada AH tetap `[H]`:

| Suhu | RH hasil pemanasan |
|---:|---:|
| 45 °C | 32,4% |
| 50 °C | 25,5% |
| 55 °C | 20,3% |
| 60 °C | 16,2% |
| 65 °C | 13,1% |
| 70 °C | 10,6% |

**Implikasi besar:** memanaskan udara saja **tidak** mencapai 10% RH pada 50 °C. Untuk mencapai dew point rendah pada suhu aman (<Tg), sistem **wajib** punya mekanisme dehumidifikasi: desiccant, condenser/cold trap, atau suplai udara kering. Tanpa itu, klaim “kendali dew-point/ΔAH” tidak terpenuhi oleh hardware.

### A.2.3 Angka penting: gravimetri
| Massa spool | 0,01% air | 0,1% | 0,5% |
|---:|---:|---:|---:|
| 1.000 g | 0,10 g | 1,00 g | 5,00 g |

Untuk mendeteksi 0,01% pada spool 1 kg, dibutuhkan resolusi **0,1 g**. Load cell + HX711 bisa, tetapi drift suhu dan tara spool harus dikendalikan.

### A.2.4 Angka penting: energi pengeringan
5 g air ≈ 12,25 kJ. Pada heater 100 W, waktu teoretis ≈ 122 s; realitasnya jauh lebih lama karena difusi air di dalam filamen. Ini alasan mengapa **endpoint gravimetri** lebih bermakna daripada timer.

### A.2.5 Arsitektur yang paling logis
- Chamber terisolasi + heater PTC + fan + exhaust.
- **Dehumidifikasi**: kolom desiccant (silica gel) dengan regenerasi, atau condenser/cold trap. Ini komponen yang wajib ditambahkan.
- Sensor: SHT31/SHT85, PT100/MAX31865, load cell 1–2 kg + HX711.
- Kontrol: ESP32 + SSR + MOSFET; profil material; batas suhu di bawah Tg; endpoint `dm/dt`; cool-down.
- Validasi: ASTM D6980 (kadar air), DSC (Tg), ASTM D638 (tarik), kualitas cetak.

### A.2.6 Tahapan build
1. Perbaiki klaim: ASTM D6980 = kadar air, bukan Tg. Putuskan akses DSC.
2. Bench: heater/fan, uniformity suhu, validasi sensor RH.
3. Gravimetri: resolusi, drift, tare, validasi dengan anak timbangan dan moisture analyzer.
4. Dehumidifikasi: uji desiccant/condenser; ukur dew point tercapai pada suhu aman.
5. Closed-loop: profil material, endpoint, safety cutoff.
6. Uji material: bandingkan sistem vs dryer komersial vs oven; ukur kadar air, Tg, tarik, cetak.
7. Analisis: laju pengeringan, akurasi endpoint, kualitas.

### A.2.7 Gate go/no-go
- **GO** jika: ada akses DSC **atau** bersedia menurunkan klaim Tg menjadi “suhu di bawah Tg literatur”; ada lab pengguna nyata; dehumidifikasi dimasukkan.
- **NO-GO sementara** jika: tidak ada DSC dan tetap ingin mengklaim “profil Tg terukur”.

### A.2.8 Berguna jangka panjang?
Metodenya (endpoint gravimetri + dew point) tahan lama. Produknya niche; dryer komersial murah tetap pesaing. Nilai tesis harus diletakkan pada **metode pengukuran dan validasi**, bukan pada klaim produk komersial.

---

## A.3 Head-to-Head

| Kriteria | Kandidat 2 — Kualitas Daya | Kandidat 3 — Filamen |
|---|---|---|
| Kebutuhan nyata | Tinggi untuk gedung tanpa monitoring | Sedang; tinggi untuk lab/filamen engineering |
| Pembayar realistis | Pengelola gedung/kampus | Lab 3D printing kampus/industri |
| Risiko teknis | Keselamatan panel, akses | DSC, load cell drift, dehumidifikasi |
| Kebaruan | Rendah–sedang (integrasi) | Sedang (endpoint gravimetri) |
| Validasi | Mudah, kuantitatif | Lebih sulit, uji material |
| Waktu | 3–4 bulan | 4–6 bulan |
| Peluang selesai | Tinggi | Sedang |
| Berguna jangka panjang | Tinggi | Sedang (niche) |

**Rekomendasi:** **Kandidat 2 lebih dulu** — jalur lebih jelas, validasi lebih mudah, dan pengguna institusional lebih realistis. **Kandidat 3** layak dilanjutkan hanya jika ada DSC dan lab pengguna; jika tidak, ubah klaim menjadi “pengering gravimetri + dew point” tanpa klaim Tg terukur.

---

# KANDIDAT 4 — Smart Dryer Brem (IDEA-052)

## Identitas
**Judul:** Rancang Bangun Smart Dryer Brem Berbasis ESP32 dengan Pengendalian Suhu dan Monitoring Penurunan Massa untuk Menjaga Konsistensi Kadar Air Produk
**Status:** `BLOCKED_PENDING_EVIDENCE` — menunggu baseline produsen, definisi produk, dan akses oven.

## Masalah
Kadar air brem yang tidak konsisten memengaruhi tekstur, daya simpan, dan risiko jamur. Pengeringan konvensional bergantung pada timer/feeling, bukan kadar air aktual.

## Konsep
ESP32 + sensor suhu/RH + load cell (penurunan massa) + heater/fan. Suhu dikendalikan; endpoint pengeringan ditentukan dari laju penurunan massa (`dm/dt`) yang dikalibrasi terhadap kadar air oven.

## Angka penting
- Batch 2 kg: 0,1% air = **2 g**; load cell 5 kg resolusi 1 g memadai.
- Dari 30% ke 15% moisture (basis basah): air diuapkan ±0,35 kg; energi ±865 kJ; pada 500 W teoretis ±29 menit, realitasnya beberapa jam karena difusi.
- Suhu pengeringan harus ditentukan eksperimental (mis. 40–60 °C); jangan mengasumsikan satu suhu untuk semua formula.

## Apple-to-apple
- Split batch: pengeringan usulan vs konvensional vs oven referensi.
- Ukur kadar air oven (AOAC/SNI) pada interval; bandingkan prediksi massa vs oven; laporkan bias, RMSE, dan simpangan baku antar-batch.
- Kriteria lulus: **konsistensi** (SD lebih rendah), bukan hanya rata-rata kadar air.

## Risiko
- Load cell drift, vibrasi, dan aliran udara.
- Kehilangan massa volatil (fermentasi) tidak identik dengan air.
- Heterogenitas produk dan keselamatan pangan (heater, kontaminasi).
- Adopsi UMKM: perlu baseline dan willingness-to-pay.

## Verdict
**KEEP — konsep kuat dan jelas IoT.** Status `BLOCKED_PENDING_EVIDENCE` sampai ada baseline produsen, definisi produk, dan akses oven. Jangan klaim “kadar air” tanpa validasi oven.
