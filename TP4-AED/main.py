import clase

LETRAS_ICD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' ,'V', 'W', 'X', 'Y', 'Z']

def menu():
    print ('1. Cargar afiliado')
    print ('2. Cargar tratamientos')
    print ('3. Mostrar resultados')
    print('Ingrese 0 para salir')


def buscar_mayor(lista):
    mayor = -1
    i_mayor = None
    n = len(lista)
    for i in range(n):
        if lista[i] > mayor:
            mayor = lista[i]
            i_mayor = i
    return i_mayor

def buscar_apellido(tratamientos):
    contador = 0
    for tratamiento in tratamientos:
        if tratamiento.complejidad == 'A':
            contador += 1
            if contador == 5:
                return tratamiento.apellido
    return 'No hay suficientes tratamientos de alta complejidad.'


def buscar_dni_monto_mayor_alta_complejidad(tratamientos):
    
    mayor = -1
    dni_mayor = None
    
    for tratamiento in tratamientos:
           if tratamiento.complejidad == 'A':
               if tratamiento.monto_final > mayor:
                   mayor = tratamiento.monto_final
                   dni_mayor = tratamiento.dni
    
    return dni_mayor

def cargar_afiliados():
    archivo = open('coberturas.csv','rt')
    archivo_leible = archivo.readlines()
    archivo.close()
    afiliados = []
    n = len(archivo_leible)
    

    for i in range(1, n): 
        linea = archivo_leible[i].strip().split(',') 
        dni = linea[0]
        codigo_os = linea[1]
        nivel = linea[2]
        tope = linea[3]
        nuevo = clase.Afiliado(dni, codigo_os, nivel, tope)
        

        add_in_order(afiliados,nuevo)

    return afiliados
    
def add_in_order(afiliados, nuevo):
        n = len(afiliados)
        izq,der = 0,n-1
        while izq <= der:
            c = (izq + der) // 2

            if afiliados[c].dni == nuevo.dni:
                pos = c
                break
            elif afiliados[c].dni > nuevo.dni:
                der = c-1
            else :
                izq = c +1

        if izq > der:
            pos = izq

        afiliados[pos:pos] = [nuevo]
           
def buscar_dni(afiliados, dni):
    izq = 0
    der = len(afiliados) - 1
    
    while izq <= der:
        c = (izq + der) // 2
        if afiliados[c].dni == dni:
            return afiliados[c]
        elif afiliados[c].dni < dni:
            izq = c + 1
        else:
            der = c - 1
            
    return 
    
    
def cargar_tratamientos():
    

    archivo = open('tratamientos.csv','rt')
    archivo_leible = archivo.readlines()
    archivo.close()
    tratamientos = []

    n = len(archivo_leible)
    c_tratamientos = n - 1 

    for i in range(1, n): 
        linea = archivo_leible[i].strip().split(',')
        dni = linea[0]
        nombre = linea[1]
        apellido = linea[2]
        codigo = linea[3]
        monto_base = linea[4]
        complejidad = linea[5]
        algoritmo = linea[6]
            
        tratamiento = clase.Tratamiento(dni, nombre, apellido, codigo, monto_base, complejidad, algoritmo)
        tratamientos.append(tratamiento)
    return tratamientos, c_tratamientos

def devuelve_promedio (tratamientos,n):
    suma = 0
    for tratamiento  in tratamientos:
        suma += (tratamiento.monto_final - tratamiento.monto_base)

    return round(suma/n,2) 

def contar_y_devolver_mayor(tratamientos):
    c_letras = len(LETRAS_ICD)
    contador = [0] * c_letras
    
    for tratamiento in tratamientos:
        izq = 0
        der = c_letras - 1

        while izq <= der:
            medio = (izq + der) // 2
            if tratamiento.codigo[0] == LETRAS_ICD[medio]:
                contador[medio] +=1
                break 
            elif tratamiento.codigo[0] < LETRAS_ICD[medio]:
                der = medio - 1
            else:
                izq = medio + 1

    i_mayor = buscar_mayor(contador)
    return LETRAS_ICD[i_mayor], contador[i_mayor]


def principal():
    tratamientos = []
    afiliados = []
    while True:
        menu()
        op = int(input('Ingrese opción: '))
        
        if op == 0:
            print('Muchas gracias por usar este programa. Adiós.')
            break

        elif op == 1:
            afiliados = cargar_afiliados()
           
        elif op == 2:
            tratamientos, c_tratamientos = cargar_tratamientos()
            #print(f'r1.1: {c_tratamientos}')
            #print(f'r1.2: {buscar_apellido(tratamientos)}')

        elif not tratamientos or not afiliados:
            print('Error: Debe cargar afiliados y tratamientos')
            continue
        elif op == 3:
            acum_sin_cobertura = acum_cobertura = 0
            cont_no_afiliados = cont_tope_aplicado = 0
            vector_acum_os = [0] * 20
            mayor_monto_no_cubierto = -1
            dni_mayor_monto_no_cubierto = None
            
            for tratatamiento in tratamientos:
                monto_final = tratatamiento.monto_final
                complejidad = tratatamiento.complejidad
                monto_cobertura = 0
                dni = tratatamiento.dni
                afiliado = buscar_dni(afiliados, dni)
                if afiliado:
                    if complejidad == "A":
                       
                        if afiliado.nivel_cobertura == 1:
                           monto_cobertura = monto_final * 0.4
                        elif  afiliado.nivel_cobertura == 2:
                           monto_cobertura = monto_final * 0.6
                        else:
                           monto_cobertura = monto_final * 0.8
                    
                    else:
                        if afiliado.nivel_cobertura == 1:
                            monto_cobertura = monto_final * 0.5
                        elif  afiliado.nivel_cobertura == 2:
                            monto_cobertura = monto_final * 0.7
                        else:
                            monto_cobertura = monto_final * 0.9
                    if monto_cobertura > afiliado.tope:
                        cont_tope_aplicado += 1
                        monto_cobertura = afiliado.tope
                        
                    vector_acum_os[afiliado.cod_obra_social - 1] += monto_cobertura
                else:
                    cont_no_afiliados += 1
                monto_sin_cobertura = monto_final - monto_cobertura
                acum_cobertura += monto_cobertura
                acum_sin_cobertura += monto_sin_cobertura
                
                if monto_sin_cobertura > mayor_monto_no_cubierto:
                    mayor_monto_no_cubierto = monto_sin_cobertura
                    dni_mayor_monto_no_cubierto = dni
                
                    
            cod_mayor = buscar_mayor(vector_acum_os) + 1
            
            print(f"r3.1: {acum_cobertura}")
            print(f"r3.2: {acum_sin_cobertura}")
            print(f"r3.3: {cont_tope_aplicado}")
            print(f"r3.4: {cont_no_afiliados}")
            print(f"r3.5: {cod_mayor}")
            print(f"r3.6: {dni_mayor_monto_no_cubierto}")
            
                     
        
        else:
            print('La opción ingresada no es válida. Intente de nuevo.')
            
            
if __name__ == '__main__':
    principal()
