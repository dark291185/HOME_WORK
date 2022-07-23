# Сразу добавим кавычки к числовым элементам списка


def convert_list_in_str():
    """Обособим каждое целое число кавычками, дополним нулём до двух целочисленных разрядов и выведем с строку, не создавая нового списка"""

    for n, i in enumerate(my_list, 0):
        if i.isdigit():
            my_list[n] = (f'"{i.zfill(2)}"')
        elif i.startswith('+'):
            my_list[n] = (f'"{i.zfill(3)}"')
    return ' '.join(my_list)

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str()
print(result)