# README
## Monitoring Kualitas Sinyal / SNR
**Kelompok B – Telekomunikasi**

**Nama:** M.Juan Aghatian  
**NIM:** 03041382631151

### 1. Deskripsi Masalah
Program ini dibuat untuk melihat kualitas sinyal berdasarkan nilai Signal to Noise Ratio (SNR) dalam satuan dB. Setiap nilai SNR akan dikelompokkan menjadi tiga kategori, yaitu RENDAH, BAIK, dan SANGAT BAIK. Dengan program ini, hasil pengamatan sinyal bisa dibaca dan dibandingkan dengan lebih mudah.

### 2. Input, Process, dan Output
- **Input:** 20 data SNR, terdiri dari 15 data inti dari soal dan 5 data tambahan.
- **Process:** Program memeriksa kategori setiap nilai, menghitung jumlah data pada tiap kategori, lalu mencari rata-rata, nilai maksimum, dan minimum.
- **Output:** Menampilkan seluruh nilai SNR beserta kategorinya dan ringkasan hasil pengolahan.

Aturan kategori yang digunakan:
- SNR < 10 dB = RENDAH
- 10 ≤ SNR < 20 dB = BAIK
- SNR ≥ 20 dB = SANGAT BAIK

### 3. Function yang Digunakan
1. `kualitas_sinyal(snr)`  
   Menentukan kategori kualitas sinyal dari satu nilai SNR. Parameter: `snr`. Return: nama kategori.

2. `hitung_kategori(data)`  
   Menghitung jumlah data untuk kategori RENDAH, BAIK, dan SANGAT BAIK. Parameter: `data`. Return: jumlah masing-masing kategori.

3. `rata_rata(data)`  
   Menghitung rata-rata dari seluruh nilai SNR. Parameter: `data`. Return: nilai rata-rata.

4. `main()`  
   Menjalankan program, menampilkan data satu per satu, dan mencetak ringkasan hasil.

### 4. Decision dan Loop
Percabangan `if`, `elif`, dan `else` dipakai untuk menentukan kategori berdasarkan batas nilai SNR. Perulangan `for` digunakan untuk memproses semua data dan menampilkan hasilnya satu per satu.

### 5. Hasil Pengolahan
Berdasarkan 20 data yang diproses, hasilnya adalah:
- Total data: 20
- RENDAH: 5 data
- BAIK: 8 data
- SANGAT BAIK: 7 data
- Rata-rata: 16,10 dB
- Maksimum: 35 dB
- Minimum: 0 dB

### 6. Lima Data Tambahan
Lima nilai tambahan yang dipakai adalah **10, 19, 20, 0, dan 35 dB**. Nilai 10 dan 19 dipilih untuk menguji batas kategori BAIK. Nilai 20 menguji awal kategori SANGAT BAIK. Nilai 0 mewakili kondisi sinyal yang sangat rendah, sedangkan 35 digunakan untuk melihat variasi nilai SNR yang tinggi. Lima data inti dari soal tetap dipertahankan sehingga jumlah keseluruhan tepat 20 data.

### 7. Cara Menjalankan
Pastikan Python 3 sudah tersedia. Simpan file dengan nama `main.py`, lalu jalankan perintah berikut pada terminal:

```bash
python main.py
```
