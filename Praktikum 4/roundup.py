# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: Program menerima sebuah integer N yang harus berada di antara 0 sampai dengan 100, kemudian membuat sebuah array dengan elemen sebanyak N. Lalu, program menerima sebuah input X dan program mengoutput bilangan terkecil kedua yang lebih besar dari X, bila tidak ada program mengoutput -1

# KAMUS
# min, min2 = float
# n, x, output = integer
# a = array of integer

# ALGORITMA

# Buat fungsi untuk menentukan bilangan terkecil kedua
def terkecilkedua(a, x):
    min = float('inf')
    min2 = float('inf')

    for num in a:
        if num > x:
            if num < min:
                min2 = min
                min = num
            elif num < min2:
                min2 = num
    
    if min2 == float('Inf'):
        return -1
    else:
        return min2


# Input
n = int(input())
valid = True

# Tentukan apakah n valid, bila valid maka inisialisasi array
if 0 < n <= 100:
    a = list(map(int, input("").split()))
    valid = True
else:
    print('Tidak valid')
    valid = False

if valid:
    x = int(input())
    output = terkecilkedua(a,x)
    print(output)
    