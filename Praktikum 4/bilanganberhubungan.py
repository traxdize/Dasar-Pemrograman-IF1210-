# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: bilanganberhubungan.py menerima dua buah integer, misal N dan X di mana N adalah jumlah bilangan dalam suatu array of integer sedangkan X adalah bilangan yang ingin dicari relasinya

# KAMUS
# n, x, close, difmax, far = integer
# a = list of integer
# difmin = float

# ALGORITMA
# Input
n = int(input())
x = int(input())
a = list(map(int, input("").split()))

# Proses
# Menentukan relasi bilangan sama
sama = ""
for i in range (n):
    if a[i] == x:
        sama = x
        break
    else:
        sama = "TIDAK ADA"

# Menentukan bilangan dengan jarak terdekat dari x
close = None
difmin = float('inf')
for i in range (n):
    dif = abs(x - a[i])
    if dif < difmin and a[i] != x:
        close = a[i]
        difmin = dif

# Menentukan bilangan dengan jarak terjauh dari x
far = None
difmax = 0
for i in range (n):
    dif = abs(x - a[i])
    if dif > difmax:
        far = a[i]
        difmax = dif

# Output
print(sama)
print(close)
print(far)