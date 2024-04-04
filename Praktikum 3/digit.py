# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024
# Deskripsi: Menerima sejumlah integer dan menentukan jumlah digit yang ada

# KAMUS

# Input
array = []

for j in range (100):
    if (j == 0):
        array.append(int(input()))
    else:
        if array[j-1] >= 0:
            array.append(int(input()))
        else:
            del array [-1]
            break

digits = [0] * 10
for number in array:
    if number == 0:
        digits[0] += 1
    else:
        while number > 0:
            digit = number % 10
            digits[digit] += 1
            number //= 10

print(len(array))

for i in range (10):
    if digits[i] > 0:
        print(str(i) + ' : ' + str(digits[i]))
        
