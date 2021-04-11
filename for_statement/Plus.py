import sys 
Number = int(sys.stdin.readline().rstrip())
sum  = 0
for i in range(Number+1):
    sum = sum + i
print(sum)