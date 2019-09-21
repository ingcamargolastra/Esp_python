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
    while opcion ==1:
        print('1. Divisas')
        print('2. Factorial')
        print('3. Primo')
        print('4. Busqueda Binaria')
        print('5. Final')
        opcion = float(input('Digite la opcion: '))
        if(opcion == 1):
            run()

if __name__ == '__main__':
    menu()
    print('Final')

    