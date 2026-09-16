

class Tratamiento:
    
    def __init__(self, dni, nombre, apellido, codigo, monto_base, complejidad, algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.algoritmo = algoritmo
        self.monto_final = self.calcular_final(monto_base, complejidad, codigo, algoritmo)
            
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, Código: {self.codigo}, Monto Base: {self.monto_base}, Complejidad: {self.complejidad}, Monto Final: {self.monto_final}"
            
            
    
    def calcular_final(self, monto_base, complejidad, codigo, algoritmo):
        
        porcentaje_extra = int(codigo[4:])
        letra = codigo[0]
        monto_final = monto_base
        
        if algoritmo == 1:
            if monto_base > 60000:
                monto_final = 0
            else:
                pass
        elif algoritmo == 2:
            if "A" <= letra <= "P":
                pass
            else:
                if complejidad == "A":
                    porcentaje_extra *= 2  
                else:
                    porcentaje_extra = 15
                    
        elif algoritmo == 3:
            pass
        else:
            pass
        
        return monto_final
        
    
    
    