import requests
import re

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
r = response.text.replace(',', '.')

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    char = (' '.join(re.findall(r'<CharCode>([^<>]+)</CharCode>', r))).split()
    value = (' '.join(re.findall(r'<Value>([^<>]+)</Value>', r))).split()
    dict_code = dict(zip(char, value))
    if code in dict_code:
        result_value = float(dict_code.get(code))
        return (result_value)
    else:
        return None

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('noname'))