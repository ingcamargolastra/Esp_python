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
    while opcion == 1:
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
            
def factorial(numero):
    if (numero == 0):
        return 1
    return numero * factorial(numero - 1)



if __name__ == '__main__':
    menu()
    print('Final')

    