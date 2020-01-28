
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


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
        self.assertEqual(prod.stealability(), "Very stealable!")

class AcmeReportTests(unittest.TestCase):
    """checks acme_report.py"""
    def test_default_num_prod(self):
        """Test number of products."""
        product_list = []
        product_list = generate_products(50)
        self.assertEqual(len(product_list), 50)

    def test_legal_names(self):
        """ Tests that adjectives are in adjectives and nouns in nouns list from name variable after being split."""
        product_list = generate_products()
        for product in product_list:
            splitter = product.name.split()
            self.assertIn(splitter[0], ADJECTIVES)
            self.assertIn(splitter[1], NOUNS)




if __name__ == '__main__':
    unittest.main()