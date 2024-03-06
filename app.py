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
            
    selected_option = None
    if request.method == "POST":
            selected_option = request.form['currency']
            print(selected_option)
                    
   
        
    return render_template('select.html',column_code=column_code, selected_option=selected_option)







if __name__ == '__main__':
    app.run(debug=True)
    app.run()