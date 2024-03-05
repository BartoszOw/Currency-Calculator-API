from flask import Flask, render_template
import requests
import csv

app = Flask(__name__)

response = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()
data_rates = data.pop()
rates = data_rates['rates']

with open('data.csv','w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=['currency', 'code', 'bid', 'ask'])

    writer.writeheader()
    for i in list(rates):
        writer.writerow({'currency': i['currency'], 'code': i['code'], 'bid': i['bid'], 'ask': i['ask']})
        


@app.route('/', methods=['GET','POST'])
def select():
    return render_template('select.html')







if __name__ == '__main__':
    app.run(debug=True)