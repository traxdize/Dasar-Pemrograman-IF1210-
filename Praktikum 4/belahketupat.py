# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: Program bikin belah ketupat

# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan:

# KAMUS
# spaces, bintang, n = integer

# ALGORITMA

def GambarBelahKetupat(n):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
    # Belah ketupat
    for i in range (n):
        spaces = abs(n//2 - i)
        bintang = n - 2 * spaces

        print(" " * spaces, end="")
        print("*" * bintang)
    
def IsValid(n):
# menghasilkan true jika N positif dan ganjil, false jika tidak
    if n > 0 and n % 2 != 0:
        return True
    else:
        return False

n = int(input())

# Output
if IsValid(n):
    GambarBelahKetupat(n)
else:
    print("Masukan tidak valid")