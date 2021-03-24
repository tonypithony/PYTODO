# При заданном целом числе n посчитайте n + nn + nnn.

n = 123

nn = int(str(n) + str(n))

nnn = int(str(nn) + str(n))

result = n + nn + nnn

print(result)
print(123 + 123123 + 123123123)

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(123)