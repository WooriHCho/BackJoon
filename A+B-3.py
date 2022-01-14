num = int(input())

a = []
b = []

for i in range(num):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    
for i in range(num):
    print(a[i] + b[i])