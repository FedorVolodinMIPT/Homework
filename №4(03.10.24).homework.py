def evk(a, b):
    if b == 0:
        return a, 1, 0
    d, X, Y = evk(b, a % b)
    x = Y
    y = X - (a // b) * Y
    return d, x, y

a=int(input())
b=int(input())
d, x, y = evk(a, b)
print(d, x, y)
