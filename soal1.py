def prima(angka):
    """
    fungsi untuk mengecek apakah suatu bilangan adalah bilangan prima
    """
    if angka < 2:
        return False  # bilangan kurang dari 2 bukan bilangan prima
    for i in range(2, int(angka ** 0.5) + 1):  # cek faktor dari 2 hingga akar kuadrat dari angka
        if angka % i == 0:
            return False  # jika habis dibagi, berarti bukan bilangan prima
    return True  # jika tidak ada faktor lain, maka bilangan tersebut prima

def bilangan_prima(n):
    """
    fungsi untuk mencari bilangan prima terbesar yang lebih kecil dari n
    """
    for i in range(n - 1, 1, -1):  # Mulai dari n-1 ke bawah hingga 2
        if prima(i):
            return i  # kembalikan bilangan prima pertama yang ditemukan
    return None  # jika tidak ditemukan bilangan prima, kembalikan None

# input dari pengguna
n = int(input("Masukkan bilangan: "))  # meminta pengguna memasukkan bilangan
result = bilangan_prima(n)  # mencari bilangan prima terdekat

# menampilkan hasil
if result:
    print(f"Bilangan prima terdekat yang lebih kecil dari {n} adalah {result}")
else:
    print("Tidak ada bilangan prima yang lebih kecil dari n.")
