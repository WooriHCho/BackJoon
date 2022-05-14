rslt = set(range(1, 10001))
num = set()

for i in range(1, 10001):
    for j in str(i):
        i+= int(j)
    num.add(i)

answer = sorted(rslt - num)
for i in answer:
    print(i)
