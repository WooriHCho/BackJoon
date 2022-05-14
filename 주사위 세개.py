x, y, z = map(int, input().split())
rslt = 0

if x==y and y==z:
    rslt =  10000 + x*1000
elif x==y:
    if x != z:
        rslt = 1000 + x*100
elif y==z:
    if x != y:
        rslt = 1000 + y*100
elif x ==z:
    if x != y:
        rslt = 1000 + x*100
else:
    max = max(x, y, z)
    rslt = max*100

print(rslt)