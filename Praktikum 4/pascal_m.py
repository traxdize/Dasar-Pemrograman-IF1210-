# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: Program menerima input N dan M di mana N adalah jumlah baris dari sebuah segitiga paskal yang akan dibuat sedangkan M adalah elemen pertamanya

# KAMUS

# ALGORITMA
n = int(input())
m = int(input())

# Membuat inisialisasi awal segitiga paskal
segitiga_paskal = []
for i in range (n):
    row = [m] * (i+1)
    segitiga_paskal.append(row)
    # Mengisi segitiga paskal
    if i > 0:
        for j in range (1, i):
            segitiga_paskal[i][j] = segitiga_paskal[i-1][j-1] + segitiga_paskal[i-1][j]

# Output
for row in segitiga_paskal:
    print(*row)