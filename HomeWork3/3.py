## Задание №3
def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        key = name[0].capitalize()
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    return dict_out
print(thesaurus("Иван", "Мария", "Петр", "Илья"))