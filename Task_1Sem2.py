#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = int(input('Введите число: '))

def sum_num(x: int):
    sum = 0
    while(x > 0):
        div = x % 10
        sum = sum + div
        x //= 10
    return(sum)
print(sum_num(x))