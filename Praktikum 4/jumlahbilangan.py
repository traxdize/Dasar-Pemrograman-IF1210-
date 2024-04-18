# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: jumlahbilangan.py menentukan berapa banyak bilangan di antara input integer x dan y yang habis dibagi 3 dan atau 4

# KAMUS
# x, y, count = Integer

# ALGORITMA
# Input

x = int(input())
y = int(input())

# Proses

count = 0
while x < (y+1):
    if (x % 3 == 0) or (x % 4 == 0):
        count += 1
        x += 1
    else:
        x += 1

# Output
if count != 0:
    print(count)
else:
    print('Tidak Ada') # Ada harus kapital kalau ga salah