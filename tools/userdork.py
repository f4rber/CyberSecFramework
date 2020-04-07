import shodan
import datetime
import time
import os
from API_KEY import api_key


# OwnUserDork
def userdork():
    userdork = input("Enter dork for searching:")  # Переменная с дорком для Shodan
    api = shodan.Shodan(api_key)  # API ключ
    date = datetime.datetime.today().strftime("%H-%M-%S-%d-%m")  # Переменная с текущим временем
    pages_start = int(input('[?] Start scanning from page : '))  # Странница с которой сканер будет начинать
    pages_stop = int(input('[?] Stop  scanning on   page : '))  # Странница на которой сканер закончит
    results_file = r'logs/ips-' + date + "-SHODAN" + '.txt'  # Переменная с именем файла для результатов

    print('[?] If you press Ctrl + C scanning will be stopped!')
    for page in range(pages_start, pages_stop, 1):
        try:
            print('[' + str(page) + '/' + str(pages_stop) + '] Loading page results... ')
            time.sleep(1)
            results = api.search(userdork, page=page)  # Переменная с запросом для сканирования
        except KeyboardInterrupt:  # Сканирование остановиться если нажато CTRL + C
            print('\n[!] (Ctrl + C) detected.. Stopping...')  # Сообщение о том что сканирование остановлено
            break
        except shodan.exception.APIError as error:  # Если будет ошибка с API мы ее выведем
            print('[EXCEPTION] ' + str(error))
            time.sleep(3)
            continue
        else:  # Записываем результаты в txt файл
            for result in results['matches']:
                with open(results_file, 'a') as file:
                    file.write(result['ip_str'] + '\n')
    # Показывает результаты по выбору пользователя
    if os.path.exists(results_file):
        print('\n[+] Okay, all results from page ' + str(pages_start) + ' to page ' + str(pages_stop) + ', was saved to ' + results_file)
        if input('[?] Show downloaded results? (y/n) : ').lower() in ('y', 'yes', 'true', '1', '+'):
            with open(results_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.replace('\n', ''))
            print('[+] Saved ' + str(len(lines)) + ' ips')
