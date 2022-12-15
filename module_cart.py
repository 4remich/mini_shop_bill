class Cart:
    def __init__(self, title):
        self.title = title
        self.goods = []

    def add_order(self, generator):
        if generator not in self.goods:
            self.goods.append(generator)

    def add_order(self, oil):
        if oil not in self.goods:
            self.goods.append(oil)

    def add_order(self, fuel):
        if fuel not in self.goods:
            self.goods.append(fuel)

    def total_amount(self):
        sum = 0
        for index, item in enumerate(self.goods):
            if item.price <= 0:
                raise ValueError('The price is less than zero. Check the price of the product!')
            sum += item.price
        return sum

    def __str__(self):
        return f"{self.title}\n{'-' * 20}\n" + '\n'.join(map(str, self.goods)) + '\n' + f"{'-' * 20}" + '\n' + \
        str('Total amount:') + f"{self.total_amount()}" + str('UAH')
