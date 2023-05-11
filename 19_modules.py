import sys #pregunta sobre el SO
#print(sys.path)

import re #expresiones regulares
text = 'Mi numero de telefono es 123 546 874, el codigo de pais es 52, mi numeros de la suerte es 16'
result = re.findall('[0-9]+',text)# el mas siginifica que encuentre mas de una coincidencia
print(result)

import time

timestamp = time.time()
local = time.localtime()
print(timestamp)
print(time.asctime(local))

import collections

numbers = [1,2,2,1,2,1,3,5,2,4,21,4]
counters = collections.Counter(numbers)
print(counters)
