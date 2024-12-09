import pandas as pd

def cheque(price_list, **kwargs):
    products = []
    prices = []
    numbers = []

    for product, number in kwargs.items():
        if product in price_list:
            products.append(product)
            prices.append(price_list[product])
            numbers.append(number)

    df = pd.DataFrame({
        'product': products,
        'price': prices,
        'number': numbers,
    })

    df['cost'] = df['price'] * df['number']
    df = df.sort_values(by='product').reset_index(drop=True)
    return df

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=4, milk=2, cream=1)
print(result)
