# Monitoring Kualitas Sinyal / SNR
# Nama  : M.Juan Aghatian
# NIM   : 03041382631151
# Kelompok B - Telekomunikasi

data_snr = [5, 8, 11, 14, 18, 22, 27, 9, 16, 24,
            12, 30, 7, 20, 15, 10, 19, 20, 0, 35]


def kualitas_sinyal(snr):
    """Menentukan kategori kualitas sinyal berdasarkan nilai SNR."""
    if snr < 10:
        return "RENDAH"
    elif snr < 20:
        return "BAIK"
    else:
        return "SANGAT BAIK"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori."""
    jumlah = {
        "RENDAH": 0,
        "BAIK": 0,
        "SANGAT BAIK": 0
    }

    for nilai in data:
        kategori = kualitas_sinyal(nilai)
        jumlah[kategori] += 1

    return jumlah


def rata_rata(data):
    """Menghitung nilai rata-rata seluruh data SNR."""
    return sum(data) / len(data)


def main():
    print("MONITORING KUALITAS SINYAL / SNR")
    print("-" * 48)
    print(f"{'No':<5}{'Nilai SNR (dB)':<20}{'Kategori'}")
    print("-" * 48)

    for nomor, nilai in enumerate(data_snr, start=1):
        print(f"{nomor:<5}{nilai:<20}{kualitas_sinyal(nilai)}")

    hasil = hitung_kategori(data_snr)

    print("\nRINGKASAN HASIL")
    print("-" * 30)
    print(f"Total data       : {len(data_snr)}")
    print(f"RENDAH           : {hasil['RENDAH']} data")
    print(f"BAIK             : {hasil['BAIK']} data")
    print(f"SANGAT BAIK      : {hasil['SANGAT BAIK']} data")
    print(f"Rata-rata        : {rata_rata(data_snr):.2f} dB")
    print(f"Maksimum         : {max(data_snr)} dB")
    print(f"Minimum          : {min(data_snr)} dB")


if __name__ == "__main__":
    main()
