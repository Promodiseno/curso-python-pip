import random
countries = ['col','mex','bol','pe']

population2 = {country: random.randint(1,100) for country in countries}
print(population2)
result = { country: population for (country, population) in population2.items() if population > 20}
print(result)

text = 'Hola Tengo algo que decir'
vocales = { c:c.upper() for c in text if c in 'aeiou'}
print(vocales)