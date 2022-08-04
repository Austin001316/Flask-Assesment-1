from app import app
from unittest import TestCase

class currencyConverterTestCase(TestCase):
    def test_homePage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>This is my currency converter.</h1>', html)
            
    def test_convert(self):
        with app.test_client() as client:
            res = client.post('/convert', data={
                'input1': 'USD',
                'input2': 'USD',
                'amount': 50,})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Here is your conversion</h1>', html)
            self.assertIn('<p>USD to USD in the amount of 50</p>',html)
            self.assertIn('<p>The result is $50.0</p>', html)