h,m = map(int, input().split())

if m < 45:
    if h<1:
        h = 23
    else:
        h -= 1
    m += 15
else:
    m -=45
    
print(h, m)