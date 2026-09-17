

class Tratamiento:
    
    def __init__(self, dni, nombre, apellido, codigo, monto_base, complejidad, algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.monto_base = float(monto_base)
        self.complejidad = complejidad
        self.algoritmo = int(algoritmo)
        self.monto_final = self.calcular_final(float(monto_base), complejidad, codigo, int(algoritmo))
            
    def __str__(self):
        return f"Algoritmo: {self.algoritmo} DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, Código: {self.codigo}, Monto Base: {self.monto_base}, Complejidad: {self.complejidad}, Monto Final: {self.monto_final}"
            
    def __repr__(self):
        return f"Algoritmo: {self.algoritmo} DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, Código: {self.codigo}, Monto Base: {self.monto_base}, Complejidad: {self.complejidad}, Monto Final: {self.monto_final}"
                   
    
    def calcular_final(self, monto_base, complejidad, codigo, algoritmo):
        bloque_icd = float(codigo[1:])
        porcentaje_extra = float(codigo[4:])
        letra = codigo[0]
        suma_fija = 0
        monto_extra = 0
        monto_final = monto_base
        
        
        if algoritmo == 1:
            
            if monto_base <= 60000:
                porcentaje_extra = 0
            elif monto_base > 60000:
                if complejidad == "A" and letra != "U":
                    suma_fija = monto_base / 2
            
        elif algoritmo == 2:
            if "A" <= letra <= "P":
                pass
            else:
                if complejidad == "A":
                    porcentaje_extra *= 2  
                else:
                    porcentaje_extra = 15
                    
        elif algoritmo == 3:
            
            if complejidad == "A":
                monto_extra = monto_base * 0.30
            
            if "A" < letra < "L":
                monto_extra += 20000
            elif "M" < letra < "P":
                monto_extra += 15000 + 5000 * bloque_icd
            else:
                monto_extra += monto_base * 0.10

            if monto_extra > 60000:
                monto_extra = 60000
        
        monto_final += (monto_base * porcentaje_extra / 100) + suma_fija + monto_extra
        
        return round(monto_final, 2)
        
    
    
    