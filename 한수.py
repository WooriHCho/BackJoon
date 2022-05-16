x = int(input())

rslt = 0

for i in range(1, x+1):
    if i <= 99:
        rslt += 1
    else:
        x = i // 100
        y = (i%100)//10
        z = i%10
        if x-y == y-z:
            rslt += 1

print(rslt)