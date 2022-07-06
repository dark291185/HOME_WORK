## Задание №4
def convert_name_extract(list_in: list) -> list:


    m = []
    for i in my_list:
        m.extend(['Привет, '+i.split()[-1].title()+'!'])
    list_out = m
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)