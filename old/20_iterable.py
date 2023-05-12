for i in range(1,11):
    print(i)

my_iter = iter(range(1,11)) #ejecuta un ciclo a la vez en vez de el recorrido completo como la opcion de arriba pero manualmente
print(next(my_iter))
print(next(my_iter))
