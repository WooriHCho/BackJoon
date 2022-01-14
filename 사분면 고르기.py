print("x좌표 입력: ")
x = int(input())
print("y좌표 입력: ")
y = int(input())

if x>0:
    if y>0:
        a=1
    else:
        a=4
else:
    if y>0:
        a=2
    else:
        a=3

print(a)
