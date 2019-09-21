def calcular_divisas(cantidad):
    factor = float(input('Digite factor de conversión: '))
    return cantidad*factor

def run():
    print('Calculadora de divisas')
    cantidad = float(input('Digite la cantidad de dinero: '))
    resultado = calcular_divisas(cantidad)
    print('{} dolares son ${} pesos colombianos'.format(cantidad, resultado))


if __name__ == '__main__':
    run()
    print('Final')

    