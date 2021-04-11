a, b = map(int, input().split())

if b < 45:
    if a == 0:
        a = 23
        b = (b+60)-45
        print(a,b)
    else:
        a = a-1
        b = (b+60)-45
        print(a, b)
elif b > 45:
    print(a, b-45)
elif b == 45:
    b = 0
    print(a, b)