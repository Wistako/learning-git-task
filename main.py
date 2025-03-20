shop_list = {
    'piekarnia': ['chleb', 'bulki', 'paczek'],
    'warzywniak': ['marchew', 'seler', 'rukole'],
    'miesny': ['lopatka', 'kosci', 'udka']
}

prod_len = 0
for shop in shop_list:
    prod_len += len(shop_list[shop])
    shop_name = shop[0].upper() + shop[1:]
    products_from_shop = [product[0].upper() + product[1:] for product in shop_list[shop]]
    print(f"Idę do {shop_name} i kupuję tam {products_from_shop}")
print(f"W sumie kupuje {prod_len} produktów.")