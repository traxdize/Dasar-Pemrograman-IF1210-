# NAMA/NIM: Kenneth Alexander Jim's/16523186
# TANGGAL: 26 April 2024
# DESKRIPSI: Program menentukan selisih terkecil dari nilai dalam array

# KAMUS
# N = integer
# a, deficits = list of integer

# ALGORITMA

N = int(input())
a = list(map(int, input().strip().split()))
deficits = []

for i in range (N):
    for j in range (len(a)):
        if i == j:
            continue
        else:
            deficits.append(abs(a[i]-a[j]))

print(min(deficits))