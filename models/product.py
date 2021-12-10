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
