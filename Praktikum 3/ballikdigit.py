# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024
# Deskripsi: Membalikkan digit sebuah integer

# KAMUS
# a, reverse = integer

# ALGORITMA
# Subprogram pembalik
def reverse_int(a):
    reverse = 0
    if a >= 0: # Menyimpan tanda bilangan asli
        sign = 1
    else:
        sign = -1
    a = abs(a)
    while a > 0:
        last = a % 10 # Mengambil digit terakhir
        reverse = reverse * 10 + last # Menambahkan digit terakhir
        a //= 10
    
    return sign * reverse

# Input
a = int(input())

# Proses & Ouput
print(reverse_int(a))