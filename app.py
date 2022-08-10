from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import requests

rates = CurrencyRates()
codes = CurrencyCodes()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    currency1 = request.form.get('input1')
    currency2 = request.form.get('input2')
    amount = request.form.get('amount')
    unimportantvariable = codes.get_symbol(currency1)
    Symbol = codes.get_symbol(currency2)
    if unimportantvariable is None:
        return render_template('home.html', error="Currency 1 is invalid, please make sure a valid currency code is entered.")
    elif Symbol is None:
        return render_template('home.html', error="Currency 2 is invalid, please make sure a valid currency code is entered.")
    elif unimportantvariable != None:
        try:
            amount = int(amount)
        except Exception as e:
            return render_template('home.html', error="Amount is invalid, please make sure it is a positive whole number.")
        if amount < 0:
            return render_template('home.html', error="Amount is a negative, please change it to a positive whole number.")
        elif amount is 0:
            return render_template('home.html', error="Amount is 0, 0 will always convert to 0. Try a positive whole number.")
        else:
            try:
                result = rates.convert(currency1, currency2, amount)
                result = round(result, 2)
                return render_template('convert.html', currency1=currency1, currency2=currency2, amount=amount, result=result, Symbol=Symbol)

            except Exception as e:
                return render_template('home.html', error="Please verify you are using valid currencies from the link below.")