a = []

while True:
    x, y = map(int, input().split())
    if x==0 and y==0:
        break
    a.append(x+y)
    
for i in range(len(a)):
    print(a[i])