class Price_list():
    def __init__ (self,name):
        self.name = name
        self.price = dict()
    def add_prices(self, **kwargs):
        for key in kwargs:
            self.price[key] = kwargs[key]
    def order(self, **kwargs):
        for value in kwargs:
            self.price[value] = kwargs[value]
            print(value)
a = Price_list("max")
a.order()
