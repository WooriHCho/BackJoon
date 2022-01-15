n = int(input())
cnt = 0
x = n

while True:
    a=x//10
    b=x%10
    x = b*10 +((a+b)%10)
    cnt+=1
    if x==n:
        break

print(cnt)