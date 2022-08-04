from flask import Flask
from forex_python.converter import CurrencyRates

app = Flask(__name__)

@app.route('/')
def converterApp():
    html = """
    <html>
        <body>
            <h1>This is my currency converter.</h1>
            <p>Please enter the currency you want to convert from and the currency you want to convert to.</p>
                <form>
                    <input type="text" id="currency1" placeholder="First currency"/>
                    <input type="text" id="currency2" placeholder="Second currency"/>
                    <input type="text" id="amout" placeholder="Amount"/>
                </form>
        </body>
    </html>
    """
    return html

c = CurrencyRates()

    c.get_rate('input1', 'input2')

set FLASK_APP=app.py:app