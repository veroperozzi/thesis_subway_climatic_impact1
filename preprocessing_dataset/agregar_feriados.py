# abrir el csv de feriados   ---> csv.reader
# abrir uno de molinetes
import csv


##
def form_csv_to_diccionario_feriados(reader):
    diccionario = {}
    fila_i = 0
    for fila in reader:
        if fila_i != 0:
            # estoy viendo los headers
            clave = fila[0]
            if clave not in diccionario:
                diccionario[clave] = fila[1]
        fila_i = fila_i + 1
    return diccionario


## agrega la columna de feriados a cada columna del csv de molinetes
def agregar_feriados(reader, dict_feriados):
    contador_fila = 0
    filas_nuevas = []
    headers = []
    for fila in reader:
        if contador_fila == 0:  # estoy viendo los headers
            headers = fila
            headers.append("FERIADO")
            headers.append("RAZON DEL FERIADO")
        else:
            valor_fila = fila
            fecha = fila[0]
            if fecha in dict_feriados:
                valor_fila.append(str(1))
                valor_fila.append(dict_feriados[fecha])
            else:
                valor_fila.append(str(0))
                valor_fila.append(" no es feriado ")

            filas_nuevas.append(valor_fila)

        contador_fila = contador_fila + 1

    return headers, filas_nuevas


def escribir_csv(headers, list_of_list, file_name):
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        # Use writerows() not writerow()
        writer.writerows(list_of_list)


def open_file(file_name):
    file = open(file_name, 'r')
    # returns a csv_reader object
    return csv.reader(file, delimiter=',', quotechar='\n')


reader_clima = open_file('feriados.csv')  ## el nombre del de clima
feriados = form_csv_to_diccionario_feriados(reader_clima)

reader = open_file('molinetes_2018_full.csv')
h, fn = agregar_feriados(reader, feriados)
escribir_csv(h, fn, 'molinetes_2018_con_feriados.csv')
