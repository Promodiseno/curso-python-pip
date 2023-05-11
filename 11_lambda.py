#funciones especiales que generan versatilidad
def incremet(x):#ejemplo basico de funcion
    return x+1

increment2 = lambda x : x + 1 # esto es una funcion lambda

result = incremet(10)
print(result)

result2 = increment2(30)
print(result2)

full_name = lambda name,last_name: f'Tu nombre completo es {name.title()} {last_name.title()}'
nombre = full_name('tito', 'ramirez')
print(nombre)