# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024
# Deskripsi: Menkonversi angka romawi menjadi integer

# KAMUS
# romawi = string/list of character
# konversi = integer
# roman = mapping string-integer

# ALGORITMA
# Input
romawi = str(input())
konversi = 0
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Proses
for i in range(len(romawi)):
    if i > 0 and roman[romawi[i]] > roman[romawi[i-1]]:
        konversi += roman[romawi[i]] - 2 * roman[romawi[i-1]]
    else:
        konversi += roman[romawi[i]]

# Output
print(konversi)