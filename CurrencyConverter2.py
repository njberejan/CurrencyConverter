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
    def __mul__(self, code, amount, number):
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


def main():
    #takes input in amount (needs to differentiate type from string IE $, € [option + shift + 2])
    while True:
        user_amount = input("Please enter an amount to convert: ")
        if '$' in user_amount:
            code1 = 'USD'
            user_amount = user_amount.replace('$', '')
            break
        elif '€' in user_amount:
            code1 = 'EUR'
            user_amount = user_amount.replace('€', '')
            break
        elif '¥' in user_amount:
            code1 = 'JPY'
            user_amount = user_amount.replace('¥', '')
            break
        else:
            print("Please enter dollars, euros, or yen only!")
            continue

    user_amount = float(user_amount)
    currency_class_variable = Currency(code1, user_amount)
    print(str(currency_class_variable))
    while True:
        code2 = input("Please enter a currency to convert to ($, €, ¥): ")
        #takes second input for conversion to another currency
        if code2 == '$':
            code2 = 'USD'
            break
        elif code2 == '€':
            code2 = 'EUR'
            break
        elif code2 == '¥':
            code2 = 'JPY'
            break
        else:
            print("Please enter dollars, euros, or yen only!")
            continue
    print(code2)
    currency_converter = CurrencyConverter(code1, code2, user_amount)
    converted_amount = currency_converter.convert()
    print("The converted amount is: {} {}".format((float("{0:.2f}".format(converted_amount))), code2))

if __name__ == '__main__':
    main()
