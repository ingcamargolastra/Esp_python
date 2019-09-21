class Estudiante:

    def __init__(self, nombre, apellido, codigo, email):
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.email = email

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getCodigo(self):
        return self.codigo
    
    def getEmail(self):
        return self.email

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return "Nombre : %s - Apellido : %s - Codigo : %s - Email : %s" \
            %(self.nombre, self.apellido, self.codigo, self.email)