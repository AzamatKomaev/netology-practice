"""
The example structure of variables
PRODUCTS = ['сметана', 'колбаса']
PRICES = {
    'пятерочка': {
        'сметана': 40,
        'колбаса': 30
    },
    'магнит': {
        'сметана': 60,
        'колбаса': 20
    }
}
output: Shop пятерочка is the most cheapest. Price of all products is 70.
"""

PRODUCTS = []
PRICES = {}


def input_products(products):
    print("If you want to finish entering products, write END")
    while True:
        product_name = input("Enter products: ")
        if product_name == "END":
            return
        products.append(product_name)
        

def input_shops_with_product_prices(prices):
    print("If you want to finish entering shops/prices, write END")
    while True:
        shop_name = input("Enter shop name: ")
        if shop_name == "END":
            return
        
        prices[shop_name] = {}

        while True:
            inp = input("Enter (<product_name>: <price>): ")
            if inp == "END":
                break
            prices[shop_name][inp.split()[0]] = int(inp.split()[1])


def calculate_the_cheapest_shop(products, prices):
    total_priceses = {}
    for shop_name, prices in prices.items():
        total_priceses[shop_name] = 0
        for product in products:
            total_priceses[shop_name] += prices[product]

    cheapest_shop = min(total_priceses, key=total_priceses.get)
    cheapest_price = total_priceses[cheapest_shop]
    return f"Shop {cheapest_shop} is the most cheapest. Price of all products is {cheapest_price}."
        

input_shops_with_product_prices(PRICES)
input_products(PRODUCTS)
result = calculate_the_cheapest_shop(PRODUCTS, PRICES)
print(result)