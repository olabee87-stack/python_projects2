# Classes are blueprints to create something from
# The object is the main thing, and we create objects by using classes
# The __init__ is the constructor in python
# Inside the __init__, the 'self' has to be the first parameter passed into it
# The 'self' acts as the 'this' keyword in JavaScript
# After defining the attributes od rhe class, define the methods (aka actions)

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"""{self.brand} is calling {phone_number}... ...""")

        # In case you want to string of the objects
    #def __str__(self):
        #return f"Brand: {self.brand} " \
               #f"Price: {self.price}"


# Making a function to create new objects

def make_phone(brand, price, call):
    phone = Phone(brand, price)
    return f"""
    Brand: {phone.brand}
    Price: {phone.price}
    Number: {phone.call(call)}"""


print(make_phone('Samsung', 500, '0417406216'))
print('*************************************************')
print(make_phone('iPhone', 600, '0417500216'))



