class Generators:
    def __init__(self, model, type, power, weight, price):
        self.model = model
        self.type = type
        self.power = power
        self.weight = weight
        self.price = price

        if self.price <= 0:
            raise ValueError('The price is less than zero. Check the price of the generator!')
    def __str__(self):
        return f'{self.model} {self.type} {self.power} {self.weight} {self.price}'

class Oil:
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price

        if self.price <= 0:
            raise ValueError('The price is less than zero. Check the price of the oil!')
    def __str__(self):
        return f'{self.name} {self.volume} {self.price}'


class Fuel:
    def __init__(self, volume, price):
        self.volume = volume
        self.price = price

        if self.price <= 0:
            raise ValueError('The price is less than zero. Check the price of the fuel!')
    def __str__(self):
        return f'{self.volume} {self.price}'