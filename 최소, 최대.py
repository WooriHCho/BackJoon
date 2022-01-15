import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

min = a[0]
max = a[0]
for i in range(len(a)):
    if min > a[i]:
        min = a[i]
    if max < a[i]:
        max = a[i]
        
print(min, max)