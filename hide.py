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
except Exception as e:
    print('Ошибка доступа к сайту! Проверьте правильность прокси или подключение к интернету.')
    exit()

if 'Почта' in demo_page.text:
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post('https://hidxxx.name/demo/success/', data={
        "demo_mail": f"{email}"
    }, headers=headers, proxies=proxies)

    if 'Ваш код выслан на почту' in response.text:
        confirm = input('Введите полученную ссылку для подтверждения: ')

        while True:
            try:
                response = requests.get(confirm, headers=headers, proxies=proxies)
                if 'Спасибо' in response.text:
                    print('Почта подтверждена. Код отправлен на ваш email.')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except:
                confirm = input('Ссылка невалидная, повторите попытку: ')
                continue
