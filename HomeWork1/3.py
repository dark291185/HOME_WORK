### Задание №3
def transform_string(number: int) -> str:
    i = n % 10
    if 11 <= n <= 19:
        text = f'{n} процентов'
    elif i == 1:
        text = f'{n} процент'
    elif 2 <= i <= 4:
        text = f'{n} процента'
    else:
        text = f'{n} процентов'
    return text
for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))