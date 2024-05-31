# NAMA/NIM: Kenneth Alexander Jim's/16523186
# TANGGAL: 26 April 2024
# DESKRIPSI: Program menentukan apa elemen array yang paling banyak muncul dalam 1 array

# KAMUS
# N, answer, index = integer
# number, check, times = list of integer

# ALGORITMA

N = int(input())
number = list(map(int, input().strip().split()))

check = [number[0]]
times = [1]

if N == 1:
    answer = number[0]
elif N == 0:
    answer = 0

for i in range (1, N):
    same = False
    for j in range (len(check)):
        if number[i] == check[j]:
            same = True
            times[j] += 1
            break
    if same == False:
        check.append(number[i])
        times.append(1)

maksimum = max(times)
index = []

for i in range (len(times)):
    if times[i] == maksimum:
        index.append(check[i])
        answer = min(index)

print(answer)
