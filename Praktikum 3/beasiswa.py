# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024

# KAMUS
# ip, pot = float
# kategori = string

# ALGORITMA
# Input

ip = float(input())
pot = float(input())

# Proses dan Output
if ip >= 3.5:
    print('4')
elif pot < 1 and ip < 3.5:
    print('1')
elif 1 <= pot < 5 and ip < 3.5:
    if ip >= 2.0:
        print('3')
    else:
        print('2')
else:
    print('0')