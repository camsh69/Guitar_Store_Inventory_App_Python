import unittest
from models.product import Product
from models.manufacturer import Manufacturer


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.manufacturer1 = Manufacturer('Fender', True)

        self.product1 = Product('Stratocaster', 'Six string, Sunburst',
                                'Electric Guitar', 4, 450, 500, self.manufacturer1)
        self.product2 = Product('Telecaster', 'Six string, Black',
                                'Electric Guitar', 0, 850, 1100, self.manufacturer1)
        self.product3 = Product('Telecaster', 'Six string, Blonde',
                                'Electric Guitar', 5, 850, 1100, self.manufacturer1)

    def test_low_stock(self):
        self.assertEqual(
            "Low stock", self.product1.check_stock_status())

    def test_out_of_stock(self):
        self.assertEqual("Out of stock", self.product2.check_stock_status())

    def test_in_stock(self):
        self.assertEqual("In stock", self.product3.check_stock_status())
