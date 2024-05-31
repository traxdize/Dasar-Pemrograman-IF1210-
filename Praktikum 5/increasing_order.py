# NAMA/NIM: Kenneth Alexander Jim's/16523186
# TANGGAL: 26 April 2024
# DESKRIPSI: Program menentukan apakah array dapat terurut menaik dengan melakukan sejumlah operasi

# KAMUS

# ALGORITMA

def increasingOrder(a):
    iniPos = a[0]
    for j in range (len(a)):
        if iniPos <= a[j]:
            iniPos = a[j]
        else:
            return False
    return True

def rotasi(a):
    n = len(a)
    temp = a[n-1]
    for i in range (n-1 , 0, -1):
        a[i] = a[i-1]
    a[0] = temp
    return

n = int(input())
a = list(map(int, input().strip().split()))

for i in range (n):
    if increasingOrder(a):
        print(i)
        exit()
    else:
        rotasi(a)

print('Tidak')