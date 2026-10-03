archivo = open("tratamientos.txt", "rt")


def calcular_total(monto_base, identificador, porcentaje, alta_complejidad):
    if "A" <= identificador <= "L":
        incremento = incremento_base_a_l

    elif ("M" <= identificador <= "Z") and identificador != "U":
        incremento = incremento_base_m_z

    else:
        incremento = incremento_base_u

    total = (monto_base + incremento) * (1 + porcentaje / 100)

    if alta_complejidad:
        total *= 1.05

    return round(total, 2)


def buscar_mayor(mayor_no_u, monto, nombre, paciente_maximo):

    if mayor_no_u is None or mayor_no_u < monto:
        mayor_no_u = monto
        paciente_maximo = nombre

    return mayor_no_u, paciente_maximo


nombre = codigo = ""
monto_base = None
c_tratamientos = trat_a = trat_b = trat_c = trat_e = trat_p = trat_cap_19 = 0
total_tratamientos = total_cap_19 = 0
incremento_base_a_l = incremento_base_m_z = incremento_base_u = 0
mayor_no_u = None
paciente_maximo = ""
c_alta_complejidad = alta_c_mas_promedio = 0
primera_linea = True
primer_identificador = None
c_igual_primero = 0
mayor_igual_primero = None

for linea in archivo:
    alta_complejidad = False
    if linea[0] == "#":

        incremento_base_a_l = int(linea[2:8])
        incremento_base_m_z = int(linea[8:14])
        incremento_base_u = int(linea[14:20])

    else:

        c_tratamientos += 1
        nombre = linea[0:25]
        codigo = linea[25:31]
        identificador = codigo[0]
        porcentaje = int(codigo[4:])
        monto_base = int(linea[31:39])
        alta_complejidad = "X" == linea[39]
        monto = calcular_total(monto_base, identificador, porcentaje, alta_complejidad)
        total_tratamientos += monto

        if primera_linea:
            primer_identificador = identificador
            primera_linea = False

        if identificador != "U":

            mayor_no_u, paciente_maximo = buscar_mayor(
                mayor_no_u, monto, nombre, paciente_maximo
            )


        if identificador == "Z":
            trat_cap_19 += 1
            total_cap_19 += monto

        elif identificador == "A":
            trat_a += 1
        elif identificador == "B":
            trat_b += 1
        elif identificador == "C":
            trat_c += 1
        elif identificador == "E":
            trat_e += 1
        elif identificador == "P":
            trat_p += 1

        if identificador == primer_identificador:
            c_igual_primero +=1

        else:
            auxiliar = c_igual_primero
            if mayor_igual_primero == None or auxiliar > mayor_igual_primero:
                mayor_igual_primero = auxiliar
            c_igual_primero = 0


promedio_total = total_tratamientos / c_tratamientos

archivo.seek(0)

for linea in archivo:
    if linea[0] == "#":

        incremento_base_a_l = int(linea[2:8])
        incremento_base_m_z = int(linea[8:14])
        incremento_base_u = int(linea[14:20])

    else:

        nombre = linea[0:25]
        codigo = linea[25:31]
        identificador = codigo[0]
        porcentaje = int(codigo[4:])
        monto_base = int(linea[31:39])
        alta_complejidad = "X" == linea[39]
        monto = calcular_total(monto_base, identificador, porcentaje, alta_complejidad)


        if alta_complejidad:
            c_alta_complejidad += 1
            if monto > promedio_total:
                alta_c_mas_promedio += 1




promedio_cap_19 = total_cap_19 / trat_cap_19


r1 = c_tratamientos
r2, r3, r4, r5, r6 = trat_a, trat_b, trat_c, trat_e, trat_p
r7 = f"{promedio_cap_19:.2f}"
r8, r9 = paciente_maximo, f"{mayor_no_u:.2f}"
r10 = round(alta_c_mas_promedio * 100 / c_alta_complejidad)
r11 = mayor_igual_primero

print("(r1) - Cantidad de tratamientos cargados:", r1)
print('(r2) - Cantidad de tratamientos "A":', r2)
print('(r3) - Cantidad de tratamientos "B":', r3)
print('(r4) - Cantidad de tratamientos "C":', r4)
print('(r5) - Cantidad de tratamientos "E":', r5)
print('(r6) - Cantidad de tratamientos "P":', r6)
print("(r7) – Importe final promedio (capítulo 19):", r7)
print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
print("(r9) - Mayor importe pagado por ese paciente):", r9)
print(
    "(r10) - Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:",
    r10,
)
print("(r11) - Enunciado extra:", r11)

