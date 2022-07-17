# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.
n = int(input('Введите число: '))

first_list = list(range(-n, n))
print(first_list)

numbers = list(map(int,input('Введите позицию чисел через пробел: ').split()))

def get_mult(numbers, first_list):
    mult = 1
    for i in numbers:
        mult *= first_list[i]
    return mult

print(get_mult(numbers, first_list))
