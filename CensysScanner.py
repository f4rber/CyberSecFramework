import censys.certificates
import censys.ipv4
import censys.data
import datetime
import os
from API_KEY import api_id, api_secret


def censysscanner():
    date = datetime.datetime.today().strftime("%H.%M.%S-%d-%m")
    results_file = r'logs/ips-' + date + "-CENSYS" + '.txt'
    if not os.path.exists('logs'):
        os.mkdir('logs')
    try:
        records = input("How many records do you want?\nExample: 2\n")
        country = input("Enter country\nExample: Russia\n")

        c = censys.ipv4.CensysIPv4(api_id=api_id, api_secret=api_secret)

        # Запрос
        c.report(""" "welcome to" AND tags.raw: "http" """, field="80.http.get.headers.server.raw", buckets=5)

        # Метод view позволяет увидеть полный JSON для IP-адреса
        c.view('8.8.8.8')

        # Метод поиска позволяет искать в индексе
        for result in c.search("80.http.get.headers.server: Apache AND location.country: " + country, max_records=int(records)):
            print(result)

        # При желании вы можете указать, какие поля вы хотите использовать для результатов поиска
        IPV4_FIELDS = ['ip',
        'updated_at',
        '80.http.get.title',
        '443.https.get.title',
        '443.https.tls.certificate.parsed.subject_dn',
        '443.https.tls.certificate.parsed.names',
        '443.https.tls.certificate.parsed.subject.common_name',
        '443.https.tls.certificate.parsed.extensions.subject_alt_name.dns_names',
        '25.smtp.starttls.tls.certificate.parsed.names',
        '25.smtp.starttls.tls.certificate.parsed.subject_dn',
        '110.pop3.starttls.tls.certificate.parsed.names',
        '110.pop3.starttls.tls.certificate.parsed.subject_dn']

        data = list(c.search("80.http.get.headers.server: Apache AND location.country: " + country, IPV4_FIELDS, max_records=int(records)))
        print("Result was saved to logs folder")
        with open(results_file, 'a', encoding='utf-8') as file:
            file.write(str(data))

    except KeyboardInterrupt:
        print('\n[!] (Ctrl + C) detected.. Stopping...')
