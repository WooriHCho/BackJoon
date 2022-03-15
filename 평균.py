a = int(input())
x = list(map(int, input().split()))

x.sort()

max = x[len(x)-1]

for i in range(len(x)):
    x[i] = x[i]/max*100

print(sum(x)/len(x))