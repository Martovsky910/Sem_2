# Реализуйте алгоритм перемешивания списка

# Переписал пузырьковую сортировку, которую показывали на шарпе

first_list = [3, 4, 1, 14 ,2 , 7]
print('Было: ', first_list)

def sort(first_list):
    for i in range(0, len(first_list)-1):
        for j in range(len(first_list)-1):
            if(first_list[j] > first_list[i]):
                swap = first_list[j]
                first_list[j] = first_list[j + 1]
                first_list[j + 1] = swap
    return(first_list)

print('Стало: ', sort(first_list))