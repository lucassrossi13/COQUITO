import clase


def menu():
    print ('1. Cargar tratamientos')
    print ('2. Mostrar resultados')
    print('Ingrese 0 para salir')

def buscar_apellido(tratamientos):
    contador = 0
    for tratamiento in tratamientos:
        if tratamiento.complejidad == 'A':
            contador += 1
            if contador == 5:
                return tratamiento.apellido
    return 'No hay suficientes tratamientos de alta complejidad.'

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
        
        

def principal():
    tratamientos = []
    op = -1
    
    while op != 0:
        menu()
        op = int(input("Ingrese el número de la opción deseada: "))
        
        if op == 1:
            tratamientos, c_tratamientos = cargar_tratamientos()
            print(f'r1.1: {c_tratamientos}')
            print(f'r1.2: {buscar_apellido(tratamientos)}')
        elif op == 2:
            pass
        
            
        
            
    
    
    

    
    

if __name__ == '__main__':
    principal()
