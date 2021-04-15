while(1):
    try:
        a,b = map(int, input().split())
        a > 0 and b < 100
        print(a+b)
    except:
        break