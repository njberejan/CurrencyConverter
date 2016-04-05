#Objects in class:
#be able to create Currency object with amount and currency code (ex: USD or EUR)
#must equal another Currency object with the same amount and currency code (dollar == dollar)
#must NOT equal another Currency object with different amount or currency code (dollar != dollar, dollar != euro)
#must be able to be added to another Currency object with the same currency code (dollar + dollar)
#must be able to be subtracted by another Currency object with the same currency code (dollar - dollar)
#must raise DifferentCurrencyCodeError when you try to add or substract two currency objects with different codes (dollar - euro, dollar + euro)
#must be able to be multiplied by an int or float and return another Currency object
#Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" and figure out the correct currency code.
    #It can also take two arguments, one being the amount and the other being the currency code.

from CurrencyConverter import ConverterClass
class Currency():

    def __init__(self, code, amount):
        self.code = code
        self.amount = amount

    def __str__(self):
        return str(self.amount) + ' ' + self.code

    def is_code(self, code):
        if self.code == code:
            return True
        else:
            return False
    def __eq__(self, code, amount):
        if self.code == code and self.amount == amount:
            return True
        else:
            return False
    def __add__(self, code, amount):
        if is_code(self, code):
            added = self.amount + amount
            return added
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def subtract(self, code, amount):
        if is_code(self, code):
            subtracted = self.amount - amount
            return subtracted
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def multiply(self, code, amount, number):
        if is_code(self, code):
            multiplied = self.amount * float(number)
            return multiplied
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def which_code(self, code):
        code_dict = {'$':'USD', '€':'EUR', '¥':'JPY'}
        if '$' in code_dict.keys():
            code = 'USD'
        elif '€' in code_dict.keys():
            code = 'EUR'
        elif '¥' in code_dict.keys():
            code = 'JPY'
        else:
            None
