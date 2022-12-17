from module_customer import *
from module_goods import *
from module_cart import *

if __name__ == '__main__':

    customer_1 = Customer('Ivanov', 'Ivan', 'ivanov***@gmail.com', '+3804466666***')
    customer_2 = Customer('Petrov', 'Petro', 'petrov***@gmail.com', '+3804455555***')
    customer_3 = Customer('Sydorov', 'Sydor', 'sydorov***@gmail.com', '+380444444***')

    generator_1 = Generators('Werk WPG3600', 'Petrol', '2.8 kW', '45 kg', 32_236.02)
    generator_2 = Generators('FOGO F3001', 'Petrol', '2.7 kW', '39 kg', 29_500.60)
    generator_3 = Generators('Alimar ALM-B-3000M', 'Petrol', '3.0 kW', '44 kg', 37_700.30)

    oil_1 = Oil('Mobil 1', '4l', 1593.90)
    oil_2 = Oil('Elf Evolution', '5l', 990.95)
    oil_3 = Oil('Lotos Synthetic', '5l', 866.65)

    fuel_1 = Fuel('5l petrol canister', 300.25)
    fuel_2 = Fuel('10l petrol canister', 55.35)
    fuel_3 = Fuel('20l petrol canister', 1100.55)

    order = Cart('Pay bill')
    order.add_order(generator_1)
    order.add_order(oil_2)
    order.add_order(oil_3)
    order.add_order(fuel_3)


print('', customer_2, '', order, sep='\n')
