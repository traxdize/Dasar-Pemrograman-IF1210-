def increasingOrder(a):
    iniPos = a[0]
    for i in range (len(a)):
        if iniPos <= a[i]:
            iniPos = a[i]
        else:
            return False
    return True

def rotasi(a):
    n = len(a)
    temp = a[n-1]
    for i in range (n-1 , 0, -1):
        a[i] = a[i-1]
    a[0] = temp
    return

n = int(input())
a = list(map(int, input().strip().split()))

for i in range (n):
    if increasingOrder(a):
        print(i)
        exit()
    else:
        rotasi(a)
        print(a)