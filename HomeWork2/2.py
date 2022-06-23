## Задание №2
def convert_list_in_str(list_in: list) -> str:
    new_list = []
    for i in my_list:
        if i.isdigit():
            new_list.append(f'"{i.zfill(2)}"')
        elif i.startswith('+'):
            new_list.append(f'"{i.zfill(3)}"')
        else:
            new_list.append(i)
    str_out = ' '.join(new_list)
    print(new_list)
    return str_out
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
