class Series():
    nombre = ""
    genero = ""
    valoracion = 0.0
    cant_temp = 0
    cant_cap = 0
    
    def __init__(self, nombre, genero, valoracion, cant_temp, cant_cap):
        self.nombre = nombre 
        self.genero = genero
        self.valoracion = valoracion
        self. cant_temp = cant_temp
        self.cant_cap = cant_cap
    
    def __getNombre__(self):
        return self.nombre
    
    def __getGenero__(self):
        return self.genero
    
    def __getValoracion__(self):
        return self.valoracion
    
    def __getCantTemp__(self):
        return self.cant_temp
    
    def __getCantCap__(self):
        return self.cant_cap
    
    def __setNombre__(self, nombre):
        self.nombre = nombre 
    
    def __setGenero__(self, genero):
        self.genero = genero 
    
    def __setValoracion__(self, valoracion):
        self.valoracion = valoracion
    
    def __setCanTemp__(self, cant_temp):
        self.cant_temp = cant_temp 
        
    def __setCanCap__(self, cant_cap):
        self.cant_cap = cant_cap 