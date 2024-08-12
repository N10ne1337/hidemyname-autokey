from os import system
system('pip3 install fake-useragent requests')
import requests
from fake_useragent import UserAgent

root_url = 'https://hidxxx.name'
demo_url = root_url + '/demo/'
ua = UserAgent()
headers = {'User-Agent': ua.random}
proxy = input('Введите прокси в формате `ip:port`. Оставьте поле пустым для пропуска: ')
if proxy == '':
    proxies = None
else:
    proxies = {
        'https': f'http://{proxy}',
    }

try:
    demo_page = requests.get(demo_url, headers=headers, proxies=proxies)
    demo_page.raise_for_status()  # Проверка на успешный запрос
except requests.exceptions.RequestException as e:
    print(f'Ошибка доступа к сайту: {e}')
    exit()

if 'Почта' in demo_page.text:
    email = input('Введите электронную почту для получения тестового периода: ')

    try:
        response = requests.post('https://hidxxx.name/demo/success/', data={
            "demo_mail": f"{email}"
        }, headers=headers, proxies=proxies)
        response.raise_for_status()  # Проверка на успешный запрос
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при отправке запроса: {e}')
        exit()

    if 'Ваш код выслан на почту' в response.text:
        confirm = input('Введите полученную ссылку для подтверждения: ')

        while True:
            try:
                response = requests.get(confirm, headers=headers, proxies=proxies)
                response.raise_for_status()  # Проверка на успешный запрос
                if 'Спасибо' в response.text:
                    print('Почта подтверждена. Код отправлен на ваш email.')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except requests.exceptions.RequestException as e:
                print(f'Ошибка при подтверждении: {e}')
                confirm = input('Ссылка невалидная, повторите попытку: ')
else:
    print('Невозможно получить тестовый период')
