class Customer:
    def __init__(self, surname, name, email, contact_phone_number):
        self.surname = surname
        self.name = name
        self.email = email
        self.contact_phone_number = contact_phone_number

    def __str__(self):
        return f'{self.name} {self.surname}\n{self.email}\n{self.contact_phone_number}'


class Generators:
    def __init__(self, model, type, power, weight, price):
        self.model = model
        self.type = type
        self.power = power
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'{self.model} {self.type} {self.power} {self.weight} {self.price}'


class Oil:
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price

    def __str__(self):
        return f'{self.name} {self.volume} {self.price}'


class Fuel:
    def __init__(self, volume, price):
        self.volume = volume
        self.price = price

    def __str__(self):
        return f'{self.volume} {self.price}'


class Basket:
    def __init__(self, title):
        self.title = title
        self.goods = []
        # self.total_amount = []

    def add_order(self, generator):
        if generator not in self.goods:
            self.goods.append(generator)
            # self.total_amount.append(float(generator.price))
    def add_order(self, oil):
        if oil not in self.goods:
            self.goods.append(oil)
            # self.total_amount.append(float(oil.price))
    def add_order(self, fuel):
        if fuel not in self.goods:
            self.goods.append(fuel)
            # self.total_amount.append(float(fuel.price))

    def total_amount(self):
        sum = 0
        for index, item in enumerate(self.goods):
            sum += item.price
        return sum

    def __str__(self):
        return f"{self.title}\n{'-' * 20}\n" + '\n'.join(map(str, self.goods)) + '\n' + f"{'-' * 20}" + '\n' + \
               str('Total amount:') + f"{self.total_amount()}" + str('UAH')


if __name__ == '__main__':

    customer_1 = Customer('Ivanov', 'Ivan', 'ivanov***@gmail.com', '+3804466666***')
    customer_2 = Customer('Petrov', 'Petro', 'petrov***@gmail.com', '+3804455555***')
    customer_3 = Customer('Sydorov', 'Sydor', 'sydorov***@gmail.com', '+380444444***')

    generator_1 = Generators('Werk WPG3600', 'Petrol', '2.8 kW', '45 kg', 27_800.10)
    generator_2 = Generators('FOGO F3001', 'Petrol', '2.7 kW', '39 kg', 29_500.60)
    generator_3 = Generators('Alimar ALM-B-3000M', 'Petrol', '3.0 kW', '44 kg', 37_700.30)

    oil_1 = Oil('Mobil 1', '4l', 1593.90)
    oil_2 = Oil('Elf Evolution', '5l', 990.95)
    oil_3 = Oil('Lotos Synthetic', '5l', 866.65)

    fuel_1 = Fuel('5l petrol canister', 300.25)
    fuel_2 = Fuel('10l petrol canister', 55.35)
    fuel_3 = Fuel('20l petrol canister', 1100.55)

    order = Basket('Sales check')
    order.add_order(generator_1)
    order.add_order(oil_2)
    order.add_order(oil_3)
    order.add_order(fuel_3)


print('', customer_2, '', order, sep='\n')
