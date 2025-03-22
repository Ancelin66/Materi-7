def hitung_faktorial(n):
    """
    Fungsi untuk menghitung faktorial tanpa menggunakan import
    """
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def cetak_deret(angka):
    """
    fungsi untuk menampilkan pola faktorial yang berkurang
    """
    for nilai in range(angka, 0, -1):
        hasil_faktorial = hitung_faktorial(nilai)  # menghitung faktorial secara manual
        deret_angka = " ".join(map(str, range(nilai, 0, -1)))  # membuat deret dari nilai hingga 1
        print(f"{hasil_faktorial} {deret_angka}")

# meminta input pengguna
angka = int(input("Masukkan angka: "))  # pengguna memasukkan angka untuk pola

cetak_deret(angka)  # menampilkan pola faktorial yang berkurang
