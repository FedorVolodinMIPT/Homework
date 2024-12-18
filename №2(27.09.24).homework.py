step, string = input().split()
step = int(step)
reversed_string = ''
for i in range(0, len(string), step):
    group = string[i:i + step]
    group = group[::-1]
    reversed_string += group

print(reversed_string)
