import clase

LETRAS_ICD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' ,'V', 'W', 'X', 'Y', 'Z']

def menu():
    print ('1. Cargar tratamientos')
    print ('2. Mostrar resultados')
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


def cargar_tratamientos():

    archivo = open('tratamientos.csv','rt')
    archivo_leible = archivo.readlines()
    tratamientos = []

    n = len(archivo_leible)
    c_tratamientos = n - 1 
    #tratamientos = c_tratamientos * [None]

    for i in range(1, n): #Corroborar el rango (1, n)
        
        tupla_linea = tuple(archivo_leible[i].split(','))
        dni = tupla_linea[0]
        nombre = tupla_linea[1]
        apellido = tupla_linea[2]
        codigo = tupla_linea[3]
        monto_base = tupla_linea[4]
        complejidad = tupla_linea[5]
        algoritmo = tupla_linea[6]
            
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
        
        for i_letra in range(c_letras):
            if tratamiento.codigo[0] == LETRAS_ICD[i_letra]:
                contador[i_letra] += 1
                
    i_mayor = buscar_mayor(contador)
    return LETRAS_ICD[i_mayor], contador[i_mayor]
        
                    
        
def principal():
    tratamientos = []
    op = -1
    
    while op != 0:
        menu()
        op = int(input('Ingrese opción: '))
        
        if op == 1:
            tratamientos, c_tratamientos = cargar_tratamientos()
            print(f'r1.1: {c_tratamientos}')
            print(f'r1.2: {buscar_apellido(tratamientos)}')
        elif op == 2:
            letra, cantidad = contar_y_devolver_mayor(tratamientos)
            dni = buscar_dni_monto_mayor_alta_complejidad(tratamientos)
            print('r.2.1:', devuelve_promedio(tratamientos,c_tratamientos))
            print('r.2.2:', letra)
            print('r.2.3:', cantidad)
            print('r.2.4:', dni)
        
            
            
if __name__ == '__main__':
    principal()
