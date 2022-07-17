# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число: '))

def cal_factorial(n):
    fact = 1
    fact_list = []
    for i in range(1, n+1):
        fact *=i
        fact_list.append(fact)
    return(fact_list)
print(cal_factorial(n))