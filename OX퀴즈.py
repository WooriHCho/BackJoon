a = int(input())
x = []

for i in range(a):
    tmp = input()
    sum = 0
    num = 0
    for j in range(len(tmp)):
        if tmp[j] == 'O':
            num += 1
        else:
            num = 0
        sum += num
    x.append(sum)

for i in range(len(x)):
    print(x[i])