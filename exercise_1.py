n = int(input("Введите число: "))

count = 0

for i in range(n):
    temp = input("Введите " + str(i + 1) + " число: ");
    if int(temp) == 0:
        count += 1

print("Количество чисел, равных нулю: ", count)
