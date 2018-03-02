class Duck:

    def __init__(self, name=None, reg_price=None, sale_price=None):
        self.name = name
        self.reg_price = reg_price
        self.sale_price = sale_price

    def __repr__(self):
        return '%s:%s:%s' % (self.name, self.reg_price, self.sale_price)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and \
               (self.reg_price is None or other.reg_price is None or self.reg_price == other.reg_price) and \
               (self.sale_price is None or other.sale_price is None or self.sale_price == other.sale_price)
