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

class Currency():
    #need function to add, function to subtract, function to compare equivalent values, function to multiply, function to assign symbol to code ($ to USD)
    #NEED TO INCLUDE __str__function to change get string of input
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

class CurrencyConverter():
    currency_dict = {'USD':1.0, 'EUR':0.88}

    def __init__(self, code1, code2, amount):
        self.code1 = code1
        self.code2 = code2
        self.amount = amount

    def convert(self):
    #     print(self.currency_dict)
    # # #takes input in amount (needs to differentiate type from string IE $, € [option + shift + 2])
    #     print(self.currency_dict.get(code1))
        #for instance of code1 and code2 in dict:
        converted_amount = self.amount * (self.currency_dict.get(self.code1) / self.currency_dict.get(self.code2))
        #multiplies resulting variables of the two keys
        return converted_amount
        #returns amount and currency code.

# if Currency.code != code:


USD = Currency('USD', 1.00)
EUR = Currency('EUR', 0.88)

print(USD.code, USD.amount)
print(EUR.code, EUR.amount)

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
        else:
            print("Please enter dollars or euros only!")
            continue
    print(code1)
    print(user_amount)
    user_amount = float(user_amount)
    currency_class_variable = Currency(code1, user_amount)
    print(str(currency_class_variable))
    #assigns variables to two halves of entered string
    while True:
        code2 = input("Please enter a currency to convert to ($, €): ")
        #takes second input for conversion to another currency
        if code2 == '$':
            code2 = 'USD'
            break
        elif code2 == '€':
            code2 = 'EUR'
            break
        else:
            print("Please enter dollars or euros only!")
            continue
    print(code2)
    currency_converter = CurrencyConverter(code1, code2, user_amount)
    converted_amount = currency_converter.convert()
    print(converted_amount)

main()



#string including monetary sign, will need to seperate sign from float (sign corresponds to code, float to amount)
#enter prompt for currency convert ("How much would you like to exchange?")
#enter prompt for what you'd like to conver it to ("To which currency?")
#produce output of conversion rate ("You would receive ____ dollars to ____ yen" or whatever)
