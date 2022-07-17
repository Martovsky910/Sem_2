# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
n = int(input('Введите число: '))

def sequence(n):
    num = 0
    res_list = []
    for n in range(1, n+1):
        num = (1 + 1 / n)**n
        res_list.append(num)
    return(res_list)

sums = sequence(n)
print(sums)

print(sum(sums))

