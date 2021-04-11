import sys

Case = int(input())
for i in range(Case):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)