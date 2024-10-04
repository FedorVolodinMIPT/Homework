import math 
f = open('text.txt','r')
c = f.readlines()
print(c[0].split())
a = list(map(int,c[0].split()))
b = c[1][0]
if b == "+":
    print(sum(a))
if b == "-":
    print(a[0]-sum(a[1:]))
if b == "*":
    print(math.prod(a))
