n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append(x+y)
    
for i in range(n):
    print('Case #{}: {}'.format(i+1, a[i]))