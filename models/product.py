class Product:

    def __init__(self, item, description, category, stock_quantity, buying_cost, selling_price, manufacturer, id=None):
        self.item = item
        self.description = description
        self.category = category
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id

    def check_stock_status(self):
        if int(self.stock_quantity) == 0:
            return "Out of stock"
        elif int(self.stock_quantity) < 5:
            return "Low stock"
        else:
            return "In stock"

    def mark_up(self):
        mark_up = (self.selling_price -
                   self.buying_cost) / (self.buying_cost) * 100
        return "{:.2f}".format(mark_up)
