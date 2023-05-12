# listas que te devuelven el mismo numero de listas pero transformada

numbers = [1,2,3,4]
numbers2 = []
#proceso tipico antiguo
for i in numbers:
    numbers2.append(i*2)
    
print(numbers)
print(numbers2)

#proceso map y lambda functions
duplicar = lambda i:i*2
numbers3 = map(duplicar,numbers)# map sirve para transformar los elementos de una lista y es una HOF
print(list(numbers3))

num = [1,2,3,4]
num1 = [5,6,7]

result = map(lambda x,y : x + y , num , num1)
print(list(result))