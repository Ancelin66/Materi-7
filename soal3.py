def matriks(baris, kolom):
    """
    Fungsi untuk mencetak angka berurutan dalam bentuk matriks dengan ukuran baris x kolom
    """
    nomor = 1  # mulai dari angka 1
    for i in range(baris):
        for j in range(kolom):
            print(nomor, end=" ")  # cetak angka dengan spasi
            nomor += 1  # tambah angka
        print()  # pindah ke baris baru

# meminta input dari pengguna
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

matriks(baris, kolom)  # menampilkan matriks
