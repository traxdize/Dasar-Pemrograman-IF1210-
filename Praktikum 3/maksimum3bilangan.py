# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024
# Deskripsi: Menentukan bilangan terbesar dari 3 angka

# KAMUS
# a, b, c = integer

# ALGORITMA
# Input
a = int(input())
b = int(input())
c = int(input())

# Proses dan output
if c >= a and c >= b:
    print(c)
elif b >= a and b >= c:
    print(b)
else:
    print(a)
