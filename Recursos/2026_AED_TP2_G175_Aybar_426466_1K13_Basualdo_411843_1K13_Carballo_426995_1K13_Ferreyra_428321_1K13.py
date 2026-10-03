def principal():

    def quitar_espacios(cadena):
        while cadena and (cadena[-1] == ' ' or cadena[-1] == '\n'):
            cadena = cadena[:-1]
        return cadena

    archivo = open("tratamientos.txt")

    linea_limpia = quitar_espacios(archivo.readline())

    adicional_AL = int(quitar_espacios(linea_limpia[2:8]))
    adicional_MZ = int(quitar_espacios(linea_limpia[8:14]))
    adicional_U = int(quitar_espacios(linea_limpia[14:20]))


    cant_total_tratamientos = tratamientos_A = tratamientos_B = tratamientos_C = tratamientos_E = tratamientos_P = 0

    tratamientos_cap_19 = 0
    sum_importes_tratamientos_cap_19 = 0

    paciente_mayor_importe_no_U = ""
    importe_mayor_no_U = 0

    sum_total_importes = 0

    cant_trat_alta_complejidad = 0
    cant_trat_alta_complejidad_mayores_al_promedio = 0

    letra_descriptiva_primer_tratamiento = ''
    cant_repeticiones_seguidas_letra_descriptiva_primer_tratamiento = 0
    cant_repeticiones_seguidas_max_letra_descriptiva_primer_tratamiento = 0
    anterior_es_igual_letra_descriptiva_primer_tratamiento = False


    for linea in archivo:
        linea_limpia = quitar_espacios(linea)


        if linea_limpia[0] != "#":
            if linea_limpia[-1] == "X":
                alta_complejidad = True
            else:
                alta_complejidad = False

            cant_total_tratamientos += 1

            paciente = quitar_espacios(linea_limpia[0:25])
            diagnostico = linea_limpia[25:31]
            monto_base = int(quitar_espacios(linea_limpia[31:39]))
            adicional = 0

            letra_descriptiva = diagnostico[0]
            porcentaje_ICD10 = int(quitar_espacios(diagnostico[4:6]))

            if letra_descriptiva == "A":
                tratamientos_A += 1
            elif letra_descriptiva == "B":
                tratamientos_B += 1
            elif letra_descriptiva == "C":
                tratamientos_C += 1
            elif letra_descriptiva == "E":
                tratamientos_E += 1
            elif letra_descriptiva == "P":
                tratamientos_P += 1

            if "A" <= letra_descriptiva <= "L":
                adicional = adicional_AL
            elif ("M" <= letra_descriptiva <= "Z") and letra_descriptiva != "U":
                adicional = adicional_MZ
            elif letra_descriptiva == "U":
                adicional = adicional_U


            monto_final = (monto_base + adicional) * (1 + porcentaje_ICD10 / 100)

            if alta_complejidad:
                monto_final += monto_final * 0.05

            if letra_descriptiva == "S" or letra_descriptiva == "T":
                tratamientos_cap_19 += 1
                sum_importes_tratamientos_cap_19 += monto_final

            if letra_descriptiva != "U":
                if monto_final > importe_mayor_no_U:
                    importe_mayor_no_U = round(monto_final, 2)
                    paciente_mayor_importe_no_U = paciente

            sum_total_importes += monto_final

            if cant_total_tratamientos == 1:
                letra_descriptiva_primer_tratamiento = letra_descriptiva
                anterior_es_igual_letra_descriptiva_primer_tratamiento = True

            if letra_descriptiva == letra_descriptiva_primer_tratamiento:
                cant_repeticiones_seguidas_letra_descriptiva_primer_tratamiento += 1

                if cant_repeticiones_seguidas_letra_descriptiva_primer_tratamiento > cant_repeticiones_seguidas_max_letra_descriptiva_primer_tratamiento:
                    cant_repeticiones_seguidas_max_letra_descriptiva_primer_tratamiento = cant_repeticiones_seguidas_letra_descriptiva_primer_tratamiento

            else:
                anterior_es_igual_letra_descriptiva_primer_tratamiento = False
                cant_repeticiones_seguidas_letra_descriptiva_primer_tratamiento = 0


        else:
            adicional_AL = int(quitar_espacios(linea_limpia[2:8]))
            adicional_MZ = int(quitar_espacios(linea_limpia[8:14]))
            adicional_U = int(quitar_espacios(linea_limpia[14:20]))

    if tratamientos_cap_19 > 0:
        importe_promedio_cap19 = round((sum_importes_tratamientos_cap_19 / tratamientos_cap_19), 2)
    else:
        importe_promedio_cap19 = 0

    if cant_total_tratamientos > 0:
        importe_promedio = sum_total_importes / cant_total_tratamientos
    else:
        importe_promedio = 0

    archivo.close()


    archivo = open("tratamientos.txt")

    linea_limpia = quitar_espacios(archivo.readline())

    adicional_AL = int(quitar_espacios(linea_limpia[2:8]))
    adicional_MZ = int(quitar_espacios(linea_limpia[8:14]))
    adicional_U = int(quitar_espacios(linea_limpia[14:20]))

    for linea in archivo:
        linea_limpia = quitar_espacios(linea)

        if linea_limpia[0] != "#":

            if linea_limpia[-1] == "X":

                cant_trat_alta_complejidad += 1

                diagnostico = linea_limpia[25:31]
                monto_base = int(quitar_espacios(linea_limpia[31:39]))
                adicional = 0
                letra_descriptiva = diagnostico[0]
                porcentaje_ICD10 = int(quitar_espacios(diagnostico[4:6]))

                if "A" <= letra_descriptiva <= "L":
                    adicional = adicional_AL
                elif ("M" <= letra_descriptiva <= "Z") and letra_descriptiva != "U":
                    adicional = adicional_MZ
                elif letra_descriptiva == "U":
                    adicional = adicional_U

                monto_final = ((monto_base + adicional) * (1 + porcentaje_ICD10 / 100)) * 1.05

                if monto_final > importe_promedio:
                    cant_trat_alta_complejidad_mayores_al_promedio += 1

        else:
            adicional_AL = int(quitar_espacios(linea_limpia[2:8]))
            adicional_MZ = int(quitar_espacios(linea_limpia[8:14]))
            adicional_U = int(quitar_espacios(linea_limpia[14:20]))

    if cant_trat_alta_complejidad > 0:
        porcentaje_trat_X = int(cant_trat_alta_complejidad_mayores_al_promedio * 100 / cant_trat_alta_complejidad)
    else:
        porcentaje_trat_X = 0

    archivo.close()

    r1 = cant_total_tratamientos
    r2 = tratamientos_A
    r3 = tratamientos_B
    r4 = tratamientos_C
    r5 = tratamientos_E
    r6 = tratamientos_P
    r7 = importe_promedio_cap19
    r8 = paciente_mayor_importe_no_U
    r9 = importe_mayor_no_U
    r10 = porcentaje_trat_X
    r11 = cant_repeticiones_seguidas_max_letra_descriptiva_primer_tratamiento

    print('(r1) - Cantidad de tratamientos cargados: ', r1)
    print('(r2) - Cantidad de tratamientos "A": ', r2)
    print('(r3) - Cantidad de tratamientos "B": ', r3)
    print('(r4) - Cantidad de tratamientos "C": ', r4)
    print('(r5) - Cantidad de tratamientos "E": ', r5)
    print('(r6) - Cantidad de tratamientos "P": ', r6)
    print('(r7) – Importe final promedio (capítulo 19): ', r7)
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final: ', r8)
    print('(r9) - Mayor importe pagado por ese paciente): ', r9)
    print('(r10) - Porcentaje de tratamientos de alta complejidad con coste mayor al promedio: ', r10)
    print('(r11) - Enunciado extra: ', r11)


if __name__ == '__main__':
    principal()