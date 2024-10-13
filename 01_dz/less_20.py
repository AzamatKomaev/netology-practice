"""
items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34', 'price': 89.9},
 'cheese':{'name': сыр молочный 1 кг.', 'count': 12', 'price': 990.9},
 'sausage':{'name': колбаса 1 кг.', 'count': 122', 'price': 1990.9}
}
price_less_20 = {
 'milk15': False,
 'cheese': True,
 'sausage': False
}
"""

def calculate_items_with_count_less_20(items: dict):
    result = {}
    for key, item in items.items():
        result[key] = item.get("count") < 20
    return result


items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
 'cheese': {'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

print(calculate_items_with_count_less_20(items))

