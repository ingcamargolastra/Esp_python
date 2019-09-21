pos = 0
datos = []

def calcular_divisas(cantidad):
    factor = float(input('Digite factor de conversión: '))
    return cantidad*factor

def run():
    print('Calculadora de divisas')
    cantidad = float(input('Digite la cantidad de dinero: '))
    resultado = calcular_divisas(cantidad)
    print('{} dolares son ${} pesos colombianos'.format(cantidad, resultado))

def menu():
    opcion = 1
    while opcion != 5:
        print('1. Divisas')
        print('2. Factorial')
        print('3. Primo')
        print('4. Busqueda Binaria')
        print('5. Final')
        opcion = float(input('Digite la opcion: '))
        if(opcion == 1):
            run()
        elif opcion == 2:
            n = float(input('Ingrese el número: '))
            total = factorial(n)
            print('El factorial de {} es {} '.format(n,total))
        elif opcion == 3:
            n = int(input('Ingrese el número: '))
            if primo(n):
                print('{} es un numero primo'.format(n))
            else:
                print('{} no es un numero primo'.format(n))
        elif opcion == 4:
            datos  = []
            datos = leerArray(datos)
            valor = int(input('Dato a buscar: '))
            result = busqueda_binaria(datos, valor, 0, len(datos)-1)
            if result is True:
                print('Numero encontrado en posición {}'.format(pos))
            else: 
                print('Numero no encontrado')


def factorial(numero):
    if (numero == 0):
        return 1
    return numero * factorial(numero - 1)

def primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True

def leerArray(datos):
    n = int(input('Cantidad de datos: '))
    for i in range(n):
        valor = int(input('Digitar dato: '))
        datos.append(valor)
    for i in range(len(datos)):
        print('Dato {} es {}'.format(i, datos[i]))
    datos.sort()
    print('Datos ordenados  \n')
    for i in range(len(datos)):
        print('Dato {} es {}'.format(i, datos[i]))
    return datos

def busqueda_binaria (datos, valor, i, j):
    if i>j:
        return False
    
    m = int((i+j)/2)
    if datos[m] == valor:
        pos = m
        return True
    elif datos[m] > valor:
        busqueda_binaria (datos, valor, i, m-1)
    else:
        busqueda_binaria (datos, valor, m+1,j)

if __name__ == '__main__':
    
    menu()
    print('Final')

    