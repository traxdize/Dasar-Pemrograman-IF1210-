# NAMA/NIM: Kenneth Alexander Jim's/16523186
# TANGGAL: 26 April 2024
# DESKRIPSI: Program menentukan bilangan terkecil apa yang tidak berada dalam array dan tidak dapat dibentuk dengan penjumlahan dua angka

# KAMUS
# a, sums = list of integer
# lanjut, find = boolean
# i = integer

# ALGORITMA

lanjut = True
a = []
sums = []

while lanjut:
    number = int(input())
    if number == -9999:
        break
    else:
        a.append(number)

for i in range (len(a)):
    for j in range (len(a)):
        if i == j:
            continue
        else:
            sums.append(abs(a[i]+a[j]))

find = True
i = 1
while find:
    if i not in a and i not in sums:
        answer = i
        find = False
    else:
        i += 1

print(answer)