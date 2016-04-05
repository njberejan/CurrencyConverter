#CurrencyConverter objects:
#Must be initialized with a dictionary of currency codes to conversion rates
#At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and the other being the conversation rate.
    #An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that a dollar is worth 0.74 euros.
#Must be able to take a Currency object and a requested currency code that is the same currency code as the Currency object's and return a Currency object equal to the one passed in.
    #That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')
#Must be able to take a Currency object that has one currency code it knows and a requested currency code and return a new Currency object with the right amount in the new currency code.
#Must be able to be created with a dictionary of three or more currency codes and conversion rates
    #An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}
    #which implies that a dollar is worth 0.74 euros and that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
#Must be able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
#Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
from CurrencyClass import Currency

class CurrencyConverter():
    currency_dict = {'USD':1.0, 'EUR':1.14, 'JPY': 0.009}

    def __init__(self, code1, code2, amount):
        self.code1 = code1
        self.code2 = code2
        self.amount = amount

    def convert(self):
        converted_amount = self.amount * (self.currency_dict.get(self.code1) / self.currency_dict.get(self.code2))
        #multiplies resulting variables of the two keys
        return converted_amount
        #returns amount and currency code.
