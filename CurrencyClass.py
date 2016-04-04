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
import ConverterClass
class Currency():
    #need function to add, function to subtract, function to compare equivalent values, function to multiply, function to assign symbol to code ($ to USD)
    #NEED TO INCLUDE __str__function to change get string of input
    def __init__(self, code, amount):
        self.code = code
        self.amount = amount
    def is_code(self, code):
        if self.code == code:
            return True
        else:
            return False
    def __eq(self, code, amount):
        if self.code == code and self.amount == amount:
            return True
        else:
            return False
    def __add(self, code, amount):
        if is_code(self, code):
            added = self.amount + amount
            return added
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def __subtract(self, code, amount):
        if is_code(self, code):
            subtracted = self.amount - amount
            return subtracted
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def __multiply(self, code, amount, number):
        if is_code(self, code):
            multiplied = self.amount * float(number)
            return multiplied
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
