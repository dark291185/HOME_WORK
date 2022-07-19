import re

def convert_list_in_str():
    """Обособим каждое целое число кавычками, дополним нулём до двух целочисленных разрядов и выведем с строку"""

    new_list = []
    for i in my_list:
        if i.isdigit():
            new_list.extend(['"', f'{i.zfill(2)}', '"'])
        elif i.startswith('+'):
            new_list.extend(['"', f'{i.zfill(3)}', '"'])
        else:
            new_list.append(i)
    str_out = ' '.join(new_list)
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(convert_list_in_str())
regex = '"\s+([^"]+)\s+"'
result = re.sub(regex, '"'+r'\1'+'"', convert_list_in_str())
print(result)