from estudiante import Estudiante

estudiantes = []
n = int(input('Cantidad de estudiantes: '))

for i in range(n):
    nombre = str(input('Ingrese el nombre: '))
    apellido = str(input('Ingrese el apellido: '))
    codigo = str(input('Ingrese el código: '))
    email = str(input('Ingrese el email: '))

    est = Estudiante(nombre, apellido, codigo, email)
    estudiantes.append(est)

for est in estudiantes:
    print (est)



