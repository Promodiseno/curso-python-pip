#funcion que llama funciones
def increment(x):
    return x + 1

incrementa = lambda x: x+1# nota de entrada (x) : nota de salida (x+1)

def high_ord_func(x,func):
    return x + func(x)

hof = lambda x,func: x + func(x)#recuerda lamda notas de entrada : notas de salida
resultado = hof(2,incrementa)

result = high_ord_func(2,increment) #la funcion en este caso sin llamarla solo ejecutarla (sin parentesis)
#2 + ( 2 + 1 )
print(result)
print(resultado)

result2 = high_ord_func(2,lambda x:x+2) #la funcion en este caso sin llamarla solo ejecutarla (sin parentesis)
print(result2)
