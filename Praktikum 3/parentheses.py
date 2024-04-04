# Nama/NIM: Kenneth Alexander Jim's/16523186
# Tanggal: 4 April 2024
# Deskripsi: Mencocokan kurung

# KAMUS
# parantheses, opening, closing = string
# list = list of character

# ALGORITMA
# Defisini subprogram
def validate_parentheses(parantheses):
    list = []
    opening = "({["
    closing = "]})"
    match = {')' : '(', '}' : '{', ']' : '['} # mapping

    for char in parentheses:
        if char in opening:
            list.append(char)
        elif char in closing:
            if not list:
                return False
            if list[-1] == match[char]:
                del list [-1]
            else:
                return False
    return len(list) == 0

# Input
parentheses = input()

# Output
if validate_parentheses(parentheses):
    print('valid')
else:
    print('tidak valid')
