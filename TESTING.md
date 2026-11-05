# TESTING
## Pengujian Program Monitoring Kualitas Sinyal / SNR

**Nama:** M.Juan Aghatian  
**NIM:** 03041382631151  
**Kelompok:** B – Telekomunikasi

Pengujian dilakukan untuk memastikan batas kategori SNR sudah sesuai dengan ketentuan pada soal.

| No. | Input (dB) | Expected Output | Actual Output | Hasil |
|---:|---:|---|---|---|
| 1 | 9 | RENDAH | RENDAH | PASS |
| 2 | 10 | BAIK | BAIK | PASS |
| 3 | 11 | BAIK | BAIK | PASS |
| 4 | 19 | BAIK | BAIK | PASS |
| 5 | 20 | SANGAT BAIK | SANGAT BAIK | PASS |
| 6 | 21 | SANGAT BAIK | SANGAT BAIK | PASS |
| 7 | 5 | RENDAH | RENDAH | PASS |
| 8 | 30 | SANGAT BAIK | SANGAT BAIK | PASS |

### Kesimpulan Pengujian
Dari delapan nilai yang diuji, hasil kategori yang diperoleh sudah sesuai dengan output yang diharapkan. Nilai 10 dan 19 masuk kategori BAIK, sedangkan nilai 20 sudah masuk kategori SANGAT BAIK. Dengan demikian, fungsi penentuan kategori dapat bekerja sesuai batas yang ditentukan.
