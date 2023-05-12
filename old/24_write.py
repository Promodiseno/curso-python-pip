
with open('./text.txt', 'r+') as file: #abre el archivo de la direccion establecida y la r+ es para permisos de lectura igual que con w(sobreescribe el archivo28*10)
    file.write('\nnuevas cosas en el txt')
    for line in file:
        print(line)