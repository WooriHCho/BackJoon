a = []

for i in range(9):
    a.append(int(input()))
    
max = a[0]
num = 0
for i in range(9):
    if max < a[i]:
        max = a[i]
        num = i

print(max)
print(num+1)
        