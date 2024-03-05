import requests
import csv


response = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()
data_rates = data.pop()
rates = data_rates['rates']




with open('data.csv','w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=['currency', 'code', 'bid', 'ask'])

    writer.writeheader()
    for i in list(rates):
        writer.writerow({'currency': i['currency'], 'code': i['code'], 'bid': i['bid'], 'ask': i['ask']})
        
