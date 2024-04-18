# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: Program menerima sebuah input N yakni jumlah elemen dalam sebuah array of integer, program akan menghitung berapa operasi yang dibutuhkan agar semua element dari array tersebut menjadi satu digit dengan cara menambahkan digit-digit sebuah element

# KAMUS
# n, operation = integer
# a = array of integer

# ALGORITMA

# Definisikan fungsi penjumlah digit
def sumdigit(num):
    return sum(int(digit) for digit in str(num))

n = int(input())
a = list(map(int, input("").split()))

operation = 0
for num in a:
    while num >= 10: # Akan mengulang selama masih di atas 1 digit
        num = sumdigit(num)
        operation += 1

print(operation)