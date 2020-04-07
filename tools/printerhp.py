import shodan
import datetime
import time
import os
from API_KEY import api_key


# PrinterHP
def printerhp():
    api = shodan.Shodan(api_key)
    date = datetime.datetime.today().strftime("%H-%M-%S-%d-%m")
    pages_start = int(input('[?] Start scanning from page : '))
    pages_stop = int(input('[?] Stop  scanning on   page : '))
    results_file = r'logs/ips-' + date + "-SHODAN" + '.txt'
    # Load and save results from pages
    print('[?] If you press Ctrl + C scanning will be stopped!')
    for page in range(pages_start, pages_stop, 1):
        try:
            print('[' + str(page) + '/' + str(pages_stop) + '] Loading page results... ')
            time.sleep(1)
            results = api.search('port:9100 pjl', page=page)
        except KeyboardInterrupt:
            print('\n[!] (Ctrl + C) detected.. Stopping...')
            break
        except shodan.exception.APIError as error:
            print('[EXCEPTION] ' + str(error))
            time.sleep(3)
            continue
        else:
            for result in results['matches']:
                with open(results_file, 'a') as file:
                    file.write(result['ip_str'] + '\n')

    # Display results after loading
    if os.path.exists(results_file):
        print('\n[+] Okay, all results from page ' + str(pages_start) + ' to page ' + str(pages_stop) + ', was saved to ' + results_file)
        if input('[?] Show downloaded results? (y/n) : ').lower() in ('y', 'yes', 'true', '1', '+'):
            with open(results_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.replace('\n', ''))
            print('[+] Saved ' + str(len(lines)) + ' ips')