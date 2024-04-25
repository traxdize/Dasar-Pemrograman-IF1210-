def validateX (array, x):
    search_at = 0
    search_result = False
    while search_at < len(array) and search_result == False:
        if array[search_at] == x:
            search_result = True
        else:
            search_at += 1
    return search_result

def maximumX (array, x):
    count = 0
    for i in range (n):
        if x > array[i]:
            count = 1
        else:
            count = 0
            break
    if count == 1:
        return True
    else:
        return False

def minimumX (array, x):
    count = 0
    for i in range (n):
        if x < array[i]:
            count = 1
        else:
            count = 0
            break
    if count == 1:
        return True
    else:
        return False
            


n = int(input())
array = []

for i in range (n):
    num = int(input())
    array.append(num)

x = int(input())

if validateX(array, x):
    if maximumX (array, x):
        print('maksimum')
    if minimumX (array, x):
        print('minimum')
    if not(maximumX(array,x)) and not(minimumX(array,x)):
        print('N#A')
else:
    print(f'{x} tidak ada')
