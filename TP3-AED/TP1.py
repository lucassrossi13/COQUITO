# Entradas

beneficiario = input("Ingrese el nombre del beneficiario: ")
codigo = input("Ingrese el código ICD10 que identifica la enfermedad: ")
monto_base = int(input("Ingrese el monto base: "))


# Proceso

monto_final = 0
capitulo = ""

primera_letra = codigo[0]
bloque = codigo[1] + codigo[2]
enfermedad_especifica = int(codigo[4])

monto_fijo = 25000
monto_AL = 25000
monto_MZ = 40000
monto_U = 100000
porcentaje_extra = 1 + ( enfermedad_especifica / 100 )


if "A" <= primera_letra <= "L":
    monto_final = int((monto_base + monto_fijo + monto_AL) * porcentaje_extra)
elif ("M" <= primera_letra <= "Z") and primera_letra != "U":
    monto_final = int((monto_base + monto_fijo + monto_MZ) * porcentaje_extra)
elif primera_letra == "U":
    monto_final = int((monto_base + monto_fijo + monto_U) * porcentaje_extra)
else:
    capitulo = "La enfermedad específica no corresponde a ningún capitulo"

valor_testigo = monto_final * 0.3

if primera_letra == "A" or primera_letra == "B":
    capitulo = "Ciertas enfermedades infecciosas y parasitarias"
    if 10000 < valor_testigo <= 22000:
        monto_final -= valor_testigo
    elif 22000 < valor_testigo <= 25000:
        monto_final -= monto_final * 0.22
    else:
        monto_final = monto_final
elif primera_letra == "C" or (primera_letra == "D" and int(bloque) <= 48):
    capitulo = "Tumores [neoplasias]"
elif primera_letra == "D" and 50 <= int(bloque) <= 89:
    capitulo = "Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad"
elif primera_letra == "E" and int(bloque) <= 90:
    capitulo = "Enfermedades endocrinas, nutricionales y metabólicas"
elif primera_letra == "F":
    capitulo = "Trastornos mentales y del comportamiento"
elif primera_letra == "G":
    capitulo = "Enfermedades del sistema nervioso"
elif primera_letra == "H" and int(bloque) <= 59:
    capitulo = "Enfermedades del ojo y sus anexos"
elif primera_letra == "H" and 59 < int(bloque) <= 95:
    capitulo = "Enfermedades del oído y de la apófisis mastoides"
elif primera_letra == "I":
    capitulo = "Enfermedades del sistema circulatorio"
elif primera_letra == "J":
    capitulo = "Enfermedades del sistema respiratorio"
elif primera_letra == "K" and int(bloque) <= 93:
    capitulo = "Enfermedades del sistema digestivo"
elif primera_letra == "L":
    capitulo = "Enfermedades de la piel y del tejido subcutáneo"
elif primera_letra == "M":
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif primera_letra == "N":
    capitulo = "Enfermedades del sistema genitourinario"
elif primera_letra == "O":
    capitulo = "Embarazo, parto y puerperio"
elif primera_letra == "P" and int(bloque) <= 96:
    capitulo = "Ciertas afecciones originadas en el período perinatal"
elif primera_letra == "Q":
    capitulo = "Malformaciones congénitas, deformidades y anomalías cromosómicas"
elif primera_letra == "R":
    capitulo = "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
elif primera_letra == "S" or (primera_letra == "T" and int(bloque) <= 98):
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif ("V" <= primera_letra < "Y") or (primera_letra == "Y" and int(bloque) <= 98):
    capitulo = "Causas externas de morbilidad y de mortalidad"
elif primera_letra == "Z":
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif primera_letra == "U":
    capitulo = "Códigos para propósitos especiales"
else:
    capitulo = "La enfermedad específica no corresponde a ningún capitulo"


# Salidas

print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)