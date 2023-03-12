# esto va a abrir el archivo
# las fechas originalmente estan en formato mes/dia/año .
# las vamos a corregir haciendo dia/mes/año
# abrimos el csv, recorremos esas listas ( el csv se peude pensar como una lista de listas , donde cada lista tiene dos elemmetnso : fecha y precipitacion )
import csv


def open_file(file_name):
    file = open(file_name, 'r')
    # returns a csv_reader object
    return csv.reader(file, delimiter=',', quotechar='\n')


def csv_to_list(csv_reader):
    i = 0
    lista_de_listas = []
    for fila in csv_reader:
        if i == 0:
            headers = fila
            lista_de_listas.append(headers)
        else:
            fecha, precipitacion = fila[0], fila[1]
            # ahora arreglemos la fecha y generemos una lista de un unico elemento con esa fecha arreglada
            mes, dia, anio = (x for x in
                              fecha.split('/'))  # le digo como quiero dividirlos , y cual es el separador
            # genero una lista, con primer elemento fecha , y la precipation que tenia desde antes
            if len(mes) == 1:
                mes = "0" + mes
            if len(dia) == 1:
                dia = "0" + dia
            lista_de_listas.append([str(dia) + "/" + str(mes) + "/" + str(anio), precipitacion])
        i = i + 1
    return lista_de_listas


def write_to_csv(lists, file_name):
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(lists[0])
        # Use writerows() not writerow()
        writer.writerows(lists[1:])


csv_reader = open_file("clima.csv")
listas = csv_to_list(csv_reader)
write_to_csv(listas, "clima_con_fechas.csv")
