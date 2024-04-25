n = -1
letter = []

def procedureL():
    bigLetter = -1
    biggusLetter = 'a'
    for i in range (len(letter)):
        if ord('A') <= ord(letter[i]) <= ord('Z'):
            bigLetter = i
            biggusLetter = letter[i]
            return (f'{bigLetter+1} {biggusLetter}')
    if bigLetter == -1:
        return('Tidak ada huruf besar')

def procedureS():
    smallLetter = -1
    smallusLetter = 'a'
    for i in range (n):
        if ord('a') <= ord(letter[i]) <= ord('z'):
            smallLetter = i
            smallusLetter = letter[i]
            return(f'{smallLetter+1} {smallusLetter}')
    if smallLetter == -1:
        return('Tidak ada huruf kecil')


def procedureX():
    notLetter = -1
    nottusLetter = 'a'
    for i in range (n):
        if not(ord('a') <= ord(letter[i]) <= ord('z')) and not(ord('A') <= ord(letter[i]) <= ord('Z')):
            notLetter = i
            nottusLetter = letter[i]
            return(f'{notLetter+1} {nottusLetter}')
    if notLetter == -1:
        return('Semua huruf')
    


while not(0 < n <= 100):
    n = int(input())
    if not(0 < n <= 100):
        print('Masukan salah. Ulangi!')

for i in range (n):
    asup = input()
    letter.append(asup)

functionDictionary = {}
functionDictionary['L'] = procedureL
functionDictionary['l'] = procedureL
functionDictionary['S'] = procedureS
functionDictionary['s'] = procedureS
functionDictionary['X'] = procedureX
functionDictionary['x'] = procedureX

function = input()
if function in functionDictionary:
    print(functionDictionary[function]())
else:
    print('Tidak diproses')
