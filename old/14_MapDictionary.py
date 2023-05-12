items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pants',
        'price': 180
    },
    {
        'product': 'tshirt',
        'price': 60
    }
]
prices = list(map(lambda item:item['price'],items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))#primero lo que quieres que le haga(add_taxes): a quien quieres que se lo haga(items)
print(new_items)