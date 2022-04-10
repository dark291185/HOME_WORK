## Задание №1
def convert_time(duration: int) -> str:
    day = duration // (24 * 3600)
    sec = duration % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if day > 0:
        i = "{} дн {} ч {} мин {} сек".format(day, hour, min, sec)
    elif hour > 0:
        i = "{} ч {} мин {} сек".format(hour, min, sec)
    elif min > 0:
        i = "{} мин {} сек".format(min, sec)
    else:
        i = "{} сек".format(sec)
    return i

duration = int(input('Введите промежуток времени в секундах: '))
if duration < 0:
    print('Число не должно быть отрицательным!')
else:
    result = convert_time(duration)
    print(result)