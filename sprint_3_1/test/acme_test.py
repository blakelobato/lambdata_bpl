import unittest
from app.acme import Product
from app.acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability for default to be 'Very Stealable'"""
        prod = Product('Test Product', 100000, 20)
        self.assertEqual(prod.stealability(), "Very Stealable!")

class AcmeReportTests(unittest.TestCase):
    """checks acme_report.py"""
    def test_default_product_price(self):
        """Test default num of products being 30."""
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)

    def test_legal_names(self):
        product_list = generate_products()
        for product in product_list:
            splitter = product.name.split()
            self.assertIn(splitter[0], ADJECTIVES)
            self.assertIn(splitter[1], NOUNS)




if __name__ == '__main__':
    unittest.main()