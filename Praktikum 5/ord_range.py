# NAMA/NIM: Kenneth Alexander Jim's/16523186
# TANGGAL: 26 April 2024
# DESKRIPSI: Program menentukan jarak ord terpendek antara 2 huruf

# KAMUS
# a,b = string
# jarak = integer

# ALGORITMA

a = str(input())
b = str(input())

def validasiKapital(a,b):
    if (ord('A') <= ord(a) <= ord('Z')) and (ord('A') <= ord(b) <= ord('Z')):
        return True
    else:
        return False
    
if validasiKapital(a,b):
    if ord (a) > ord(b):
        if ord(a) - ord(b) > 13:
            jarak = 26 - ((ord(a) - ord(b)))
        else:
            jarak = ord(a) - ord(b)
    else:
        if ord(b) - ord(a) > 13:
            jarak = 26 - (ord(b) - ord(a))
        else:
            jarak = (ord(b)-64) - (ord(a)-64)
    print(jarak)
else:
    print('Tidak valid')

