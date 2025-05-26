def total_inventory_value(products):
    total_price = 0

    for _, data in products.items():
        total_price += data[0] * data[1]

    return total_price


products = {
    'p1': (2, 100),
    'p2': (3, 250),
    'p3': (10, 12),
    'p4': (6, 1000),
    'p5': (8, 20),
}

print(total_inventory_value(products))
