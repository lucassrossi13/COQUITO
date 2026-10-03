nombre = input('Ingrese el nombre del paciente: ')
codigo = input('Ingrese el codigo ICD10: ')
monto_base = int(input('Ingrese el monto base: '))

x = codigo[0]
primeros_3 = codigo[:3]
incremento_fijo = 25000
porcentaje = int(codigo[4:])
capitulos = ("Ciertas enfermedades infecciosas y parasitarias",
             "Tumores [neoplasias]",
             "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad",
             "Enfermedades endocrinas, nutricionales y metabólicas",
             "Trastornos mentales y del comportamiento",
             "Enfermedades del sistema nervioso",
             "Enfermedades del ojo y sus anexos",
             "Enfermedades del oído y de la apófisis mastoides",
             "Enfermedades del sistema circulatorio",
             "Enfermedades del sistema respiratorio",
             "Enfermedades del sistema digestivo",
             "Enfermedades de la piel y del tejido subcutáneo",
             "Enfermedades del sistema osteomuscular y del tejido conjuntivo",
             "Enfermedades del sistema genitourinario",
             "Embarazo, parto y puerperio",
             "Ciertas afecciones originadas en el período perinatal",
             "Malformaciones congénitas, deformidades y anomalías cromosómicas",
             "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte",
             "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas",
             "Causas externas de morbilidad y de mortalidad",
             "Factores que influyen en el estado de salud y contacto con los servicios de salud",
             "Códigos para propósitos especiales",
             )

if "A" <= x <= "L":
    incremento_variable = 25000
    if x == "A" or x == "B":
        capitulo = capitulos[0]
    elif x == "C" or primeros_3 < "D49":
        capitulo = capitulos[1]
    elif x == "D" :
        capitulo = capitulos[2]
    elif x == "E" :
        capitulo = capitulos[3]
    elif x == "F" :
        capitulo = capitulos[4]
    elif x == "G" :
        capitulo = capitulos[5]
    elif primeros_3 < "H60"  :
        capitulo = capitulos[6]
    elif x == "H" :
        capitulo = capitulos[7]
    elif x == "I" :
        capitulo = capitulos[8]
    elif x == "J" :
        capitulo = capitulos[9]
    elif x == "K" :
        capitulo = capitulos[10]
    elif x == "L" :
        capitulo = capitulos[11]


elif ("M" <= x <= "Z") and x != "U" :
    incremento_variable = 40000
    if x == "M" :
        capitulo = capitulos[12]
    elif x == "N":
        capitulo = capitulos[13]
    elif x == "O" :
        capitulo = capitulos[14]
    elif x == "P" :
        capitulo = capitulos[15]
    elif x == "Q" :
        capitulo = capitulos[16]
    elif x == "R" :
        capitulo = capitulos[17]
    elif x == "S" or x == "T" :
        capitulo = capitulos[18]
    elif x == "V" or x == "W" or x == "X" or x == "Y":
        capitulo = capitulos[19]
    elif x == "Z" :
        capitulo = capitulos[20]

else:
    incremento_variable = 100000
    capitulo = capitulos[21]

monto_final = (monto_base + incremento_fijo + incremento_variable)*(1+porcentaje/100)

print("Beneficiario:", nombre)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)





