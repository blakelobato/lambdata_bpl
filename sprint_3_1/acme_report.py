from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def adj_noun_name():
    """ returns the random choice of adjectives space nouns"""
    return choice(ADJECTIVES) + " " + choice(NOUNS)

def pricetags():
    """ random int between 5 and 100 inclusively for price"""
    return randint(5, 100)

def weightscales():
    """ random int between 5 and 100 inclusively for weight"""
    return randint(5, 100)

def flame():
    """ random float between 0 and 2.5 inclusively for flammability"""
    return uniform(0, 2.5)


def generate_products(num_products=30):
    """Create empty products list and append necessary info to each"""
    num_products = 50
    products = []
    for _ in range(0, num_products):
        products.append(Product(adj_noun_name(), pricetags(), weightscales(), flame(), randint(1000000, 9999999)))
    return products

def inventory_report(products):
    """Generates inventory report"""
    unique_adj_noun = []
    prices=0
    weights=0
    flames=0
    
    for product in products:
        if product.name not in unique_adj_noun:
            unique_adj_noun.append(product.name)
        prices += product.price
        weights += product.weight
        flames += product.flammability

    ave_p = prices/len(products)
    ave_w = weights/len(products)
    ave_f = flames/len(products)

    print('ACME CORPORAATION OFFICIAL INVENTORY REPORT')

    print(f'Number of unique product names: {len(unique_adj_noun)}')
    print(f'Average Price: {ave_p}')
    print(f'Average Weight: {ave_w}')
    print(f'Average Flammability: {ave_f}')


if __name__ == '__main__':
    inventory_report(generate_products())