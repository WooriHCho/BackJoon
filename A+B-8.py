n = int(input())
a = []
b = []
c = []

for i in range(n):
    x, y = map(int, input().split())
    b.append(x)
    c.append(y)
    a.append(x+y)
    
for i in range(n):
    print('Case #{}: {} + {} = {}'.format(i+1, b[i], c[i], a[i]))