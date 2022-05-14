x, y = map(int, input().split())
z = int(input())

cnt = z+y

if cnt < 60:
    print(x, cnt)
else:
    num = cnt // 60
    tmp = cnt % 60

    if x + num >= 24:
        print((x+num)-24, tmp)
    else:
        print(x+num, tmp)