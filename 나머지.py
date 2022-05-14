from re import A


x = int(input())
y = int(input())

a = x * (y%10)
b = x * ((y//10)%10)
c = x * (y//100)
d = a + b*10 + c*100

print(a)
print(b)
print(c)
print(d)
