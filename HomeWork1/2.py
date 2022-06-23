# Задание №2
def sum_list_1(dataset: list) -> int:
    list_1 = []
    for i in range(1, 1001, 2):
        list_1.append(i ** 3)
    numbers_sum = 0
    for i in list_1:
        n = 0 # сумма цифр в числе
        j = i
        while i > 0:
            n += i % 10
            i //= 10
        if n % 7 == 0:
            numbers_sum += j

    return numbers_sum

def sum_list_2(dataset: list) -> int:
    list_2 = []
    for i in range(1, 1001, 2):
        list_2.append(i ** 3 + 17)
    numbers_sum = 0
    for i in list_2:
        n = 0
        j = i
        while i > 0:
            n += i % 10
            i //= 10
        if n % 7 == 0:
            numbers_sum += j

    return numbers_sum

my_list = []
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)