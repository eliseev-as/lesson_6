x = int(input("Введите число: "))

div = 0

for i in range(1, x + 1):
    if x % i == 0:
        div += 1

print("Количество натуральных делителей числа", x, "-", div)
