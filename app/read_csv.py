import csv

 #*Creamos una funcion para la lectura del archivo 
def read_csv(path):
    with open(path, 'r') as csvfile: #* Lo abrimos y solicitamos el permiso para leerlo
        reader = csv.reader(csvfile, delimiter=',') #* Especificamos como se encuentran los datos dentro del archivo
        header = next(reader) #* me genera un array solo con los nombres de las columans 
        data = [] #* genero una entrada para los datos 
        
        for  row in reader: 
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable} #* generamos un diccionario para poder tener  las columnas como llaves
            data.append(country_dict) #* agrego los datos ya transformados en diccionario a la variable, donde ya los puedo consultar 
        return data
    
#* Generamos una nueva funcion para cambiar los nombres de las columnas
            
if __name__ == '__main__':#* lo ejecutamos directamente desde la terminal 
    data = read_csv('./app/data.csv')
    print(data[0])

