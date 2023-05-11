#privadas, globales,locales
price = 100 #global
def incremento(price):
    price = price +10
    return price #local

print(price)

print(incremento(10))