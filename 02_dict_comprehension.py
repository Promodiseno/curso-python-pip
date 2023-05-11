'''
dict = {}
for i in range(1,5):
    dict[i] = i *2
print(dict)

dict2 = { i:i*2 for i in range(1,5)}
print(dict2)

import random
countries = ['col','mex','bol','pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

population2 = {country: random.randint(1,100) for country in countries}
print(population2)
'''
names = ['nico','gris','hassen']
ages = [9,11,12]
#print(list(zip(names, ages)))

datos = {name: age for (name,age) in zip(names,ages)}
#print(datos)

persona = {
    'nombre':'david',
    'edad': 30,
    'ciudad': 'Mexico'
}
persona['telefono']= '12345678'
print(persona)
diccionario = { dato : len(dato) for dato in persona}
print(diccionario.items())
a={1,2}
b={2,3}
print(a&b)

n = [i-1 for i in range(1,6) if i<=2]
print(n)
names2 = {'nicolas','miguel','juan','nicolas'}
print(names2)