import csv
import datetime


# esta funcion abre el archivo

def open_file(file_name):
    file = open(file_name, 'r')
    # returns a csv_reader object
    return csv.reader(file, delimiter=',', quotechar='\n')


def convertir_string_a_entero(s):
    if isinstance(s, str):
        if s == "" or not s:
            return 0
        if s == "NA" or s == 'NA':
            return 0
        return int(s)
    return s


def calcular_nueva_acumulada(accumulada_guardada, actual_en_csv):
    if len(accumulada_guardada) == len(actual_en_csv):
        fecha = accumulada_guardada[0]
        linea = accumulada_guardada[1]
        molin = accumulada_guardada[2]
        id_estacion = accumulada_guardada[3]
        estacion = accumulada_guardada[4]
        pax_pagos = accumulada_guardada[5]
        pax_pases_pagos = accumulada_guardada[6]
        pax_freq = accumulada_guardada[7]
        total = accumulada_guardada[8]

        ## valores acumulados

        pax_pagos = pax_pagos + convertir_string_a_entero(actual_en_csv[5])
        pax_pases_pagos = pax_pases_pagos + convertir_string_a_entero(actual_en_csv[6])
        pax_freq = pax_freq + convertir_string_a_entero(actual_en_csv[7])
        total = total + convertir_string_a_entero(actual_en_csv[8])

        lista_acumulada_calculada = [fecha, linea, molin, id_estacion, estacion, pax_pagos, pax_pases_pagos, pax_freq,
                                     total]
        return lista_acumulada_calculada
    else:
        return []


def csv_to_dict_of_list(csv_reader):
    diccionario = {}
    csv_headers = []
    i = 0
    for fila_actual in csv_reader:
        if i == 0:
            csv_headers = [fila_actual[0], fila_actual[3], fila_actual[4], fila_actual[5], fila_actual[6],
                           fila_actual[7], fila_actual[8], fila_actual[9], fila_actual[10]]
        if i >= 1:
            actual_fecha = fila_actual[0]
            actual_linea = fila_actual[3]
            actual_molin = fila_actual[4]
            actual_id_estacion = convertir_string_a_entero(fila_actual[5])
            actual_estacion = fila_actual[6]
            actual_pax_pagos = convertir_string_a_entero(fila_actual[7])
            actual_pax_pases_pagos = convertir_string_a_entero(fila_actual[8])
            actual_pax_freq = convertir_string_a_entero(fila_actual[9])
            actual_total = convertir_string_a_entero(fila_actual[10])
            clave = actual_fecha + "_" + actual_linea + "_" + actual_molin + "_" + actual_estacion
            fila_actual_sin_horas = [actual_fecha, actual_linea, actual_molin, actual_id_estacion, actual_estacion,
                                     actual_pax_pagos, actual_pax_pases_pagos, actual_pax_freq, actual_total]
            if clave in diccionario:
                lista_acumulada_guardada = diccionario[clave]
                nueva_acumulada = calcular_nueva_acumulada(lista_acumulada_guardada, fila_actual_sin_horas)
                diccionario[clave] = nueva_acumulada
            else:
                acc = [actual_fecha, actual_linea, actual_molin, actual_id_estacion, actual_estacion, actual_pax_pagos,
                       actual_pax_pases_pagos,
                       actual_pax_freq, actual_total]
                diccionario[clave] = acc
        i = i + 1

    return csv_headers, diccionario


def dict_to_list(headers, dictionary):
    list_of_lists = []
    list_of_lists.append(headers)

    for key in dictionary:
        value = dictionary[key]
        list_of_lists.append(value)

    return list_of_lists


def write_to_csv(lists, file_name):
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(lists[0])
        # Use writerows() not writerow()
        writer.writerows(lists[1:])


def get_dia_de_la_semana(date_str):
    # para molinetes_2016 , las fechas son tipo : dd/mm/año
    import datetime
    date_str = date_str.replace('"', '')
    dia, mes, anio = (int(x) for x in date_str.split('/'))  # le digo como quiero dividirlos , y cual es el separador
    ans = datetime.date(dia, mes, anio)
    dia_semana = ans.strftime("%A")
    return dia_semana


def eliminar_comillas_y_agregar_dia(list, dictionario):
    listas_csv = []
    i = 0
    for l in list:
        if i == 0:
            headers = []
            for t in l:
                palabra_con_comillas = t
                headers.append(palabra_con_comillas.replace('"', ''))
            headers.append("DIA DE LA SEMANA")
            headers.append("PRECIPITACION")
            listas_csv.append(headers)

        ## ahora , cuando i es >= 1
        ## vamos a eliminar los comillas , y sólo agregar una comilla
        ## ahora tenemos asi :  """02/01/2016""","""D""","""LINEA_D_9JULIO_S_TURN02""",6,"""9 DE JULIO""",597,1,7,605
        ## queremos dejarlo asi : "02/01/2016","D","LINEA_D_9JULIO_S_TURN02",6,"9 DE JULIO",597,1,7,605

        if i >= 1:
            fecha = (l[0].replace('"', ''))

            dia, mes, anio = (int(x) for x in
                              fecha.split('/'))  # le digo como quiero dividirlos , y cual es el separador
            ans = datetime.date(anio, mes, dia)
            dia_semana = ans.strftime("%A")

            linea = l[1].replace('"', '')
            molinete = l[2].replace('"', '')
            id_estacion = l[3]
            estacion = l[4].replace('"', '')
            pagos, pases_pagos, freq, total = l[5], l[6], l[7], l[8]

            precipitacion = 0
            if fecha in dictionario:
                precipitacion = dictionario[fecha]
            new_list_sin_comillas = [fecha, linea, molinete, id_estacion, estacion, pagos, pases_pagos, freq, total,
                                     dia_semana,
                                     precipitacion
                                     ]  # el ulimo es el dia de la semana
            listas_csv.append(new_list_sin_comillas)
        i = i + 1

    return listas_csv


## llamado a funciones ( ejecucion )


def generar_dictionario_from_csv(archivo_csv):
    dictionario = {}
    for row in archivo_csv:
        dictionario[row[0]] = row[1]
    return dictionario


csv_reader_m16 = open_file("molinetes_2016.csv")
headers, listas_comprimidas = csv_to_dict_of_list(csv_reader_m16)
lists = dict_to_list(headers, listas_comprimidas)

csv_reader_clima = open_file("clima_con_fechas_ok.csv")
disctionario_de_precipitaciones = generar_dictionario_from_csv(csv_reader_clima)

lista_sin_comillas = eliminar_comillas_y_agregar_dia(lists, disctionario_de_precipitaciones)
write_to_csv(lista_sin_comillas, 'molinetes_2016_full.csv')
