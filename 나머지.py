a = []
cnt=0

for i in range(0, 10, 1):
    a.append(int(input()) % 42)

for i in range(42):
    if i in a:
        cnt+=1
    else:
        pass
    
print(cnt)