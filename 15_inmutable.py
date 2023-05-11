#como evitar que se modifique nuestro item original
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
    new_item = item.copy()#hace una copia de el diccionario pero sin traer la referencia
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))#primero lo que quieres que le haga(add_taxes): a quien quieres que se lo haga(items)
print(items,'\n')
print(new_items)
