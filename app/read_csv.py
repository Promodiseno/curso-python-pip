import csv

def read_csv(path):
    with open(path,'r') as csvfile: #recuerda que con with abres y cierras el archivo sin necesidad de hacerlo manual
        reader = csv.reader(csvfile, delimiter = ',') #iterable y sabemos que la primer fila es el nombre de las columnas  y podemos recorrer una fila por fila 
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            #print('***'*5)maps
            #print(list(iterabe))
            #country_dict = {key:value for key,value in iterable}# forma convencional
            country_dict = dict(iterable)# forma dictionary comprenhension
            data.append(country_dict)
        return data

if __name__ == '__main__':#recuerda que lo que este dentro de este apartado si se mandan a llamar las funciones de este modulo, lo que este dentro de este if no se ejecutara
    data = read_csv('./app/data.csv')
    #print(data[0])
    print(data)