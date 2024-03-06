from flask import Flask, render_template, request

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

    column_code = []
    column_ask = []
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            column_code.append(row['code'])
            column_ask.append(row['ask'])
            
    selected_currency = None
    selected_ask = 0
    selected_amount = 0
    res = 0
    if request.method == "POST":
            selected_currency = request.form['currency']
            index_code = column_code.index(selected_currency)
            selected_ask = column_ask[index_code]
            selected_amount = request.form['count']
            res = float(selected_ask) * int(selected_amount)

            
                    
   
        
    return render_template('select.html',res=res,column_code=column_code, selected_currency=selected_currency, selected_ask=selected_ask, selected_amount=selected_amount)







if __name__ == '__main__':
    app.run(debug=True)
    app.run()