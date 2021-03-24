# Сложите цифры целого числа.

n = 123246369

result = 0

for i in list(str(n)):
	result += int(i)


print(result)


def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(123246369))