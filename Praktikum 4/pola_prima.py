# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 18 April 2024
# Deskripsi: Program menerima sebuah bilanan bulat n, yak benar, hanya n. Kemudian program menyusun sebuah persegi n * n yang tersusun atas deret bilangan prima sepanjang n

# KAMUS
# num, n = integer
# prima = matrix of integer

# ALGORITMA

# Definisikan sebuah fungsi untuk mengecek apakah bilangan tersebut prima
def isPrime(num):
    if num <= 1:
        return False
    for i in range (2, int(num**0.5) + 1): # Faktor sebuah bilangan prima tidak akan lebih besar dari akar kuadrat nya (ditulis sebagai **0.5 di sini), digunakan int agar dibulatkan ke atas
        if num % i == 0: # Bila sebuah bilangan habis dibagi faktor lain yang bukan 1 atau dirinya, maka bukan bil prima
            return False
    return True

# Definisikan fungsi untuk membuat deret bilangan prima
def deretPrima(n):
    prima = []
    num = 2
    while len(prima) < n:
        if isPrime(num):
            prima.append(num)
        num += 1
    return prima    

n = int(input())

prima = deretPrima(n)

# Membuat pola prima
if n < 1:
    print('Tidak valid')
else:
    for i in range (n):
        for j in range (n):
            if i >= j:
                print(prima[i - j], end='')
            else:
                print(prima[j - i], end='')
            if j != n - 1:
                print(' ', end='')
        print()

# Akhirnya beres, setelah sejibun trial and error :v
# Apaan dah spasi