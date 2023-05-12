#manipulacion de listas
#toma una lista y saca una conclusion de esa lista 
from functools import reduce #Escencial para que funcione Reduce()

numbers = [1,2,3,4]

def acumulador(counter, item):
    print(counter)
    print(item)
    return counter + item

result = reduce(lambda counter,item: counter + item, numbers)#counter entrada = 0 guarda la suma de cada iteracion, item es el dato que tien en su interior numbers los suma hasta que haga el recorrido , de que lista se trabajara
print(result)

result2 = reduce(acumulador, numbers)
print(result2)
