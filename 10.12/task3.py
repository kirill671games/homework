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

def discount(cheque_df):
    discounted_df = cheque_df.copy()
    discounted_df['cost'] = discounted_df.apply(
        lambda row: row['cost'] * 0.5 if row['number'] > 2 else row['cost'],
        axis=1
    )

    return discounted_df

import pandas as pd

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)

result = cheque(price_list, soda=3, milk=2, cream=4)
with_discount = discount(result)

print(result)
print(with_discount)
