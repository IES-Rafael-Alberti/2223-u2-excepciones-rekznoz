
def numeros_impares(n):
    if n < 1:
        raise ValueError("El numero debe ser un positivo")
    impares = [str(x) for x in range(1, n + 1) if x % 2 != 0]
    return ", ".join(impares)

if __name__ == '__main__':
    numeroCorrecto = False
    numeros = None
    while not numeroCorrecto:
        try:
            ent = int(input("Ingresa un numero positivo "))
            numeros = numeros_impares(ent)
            numeroCorrecto = True
        except ValueError:
            if numeros == None:
                print('Introduzce un numero.')
            else:
                print('Es numero es incorrecto')

    print("Impares desde 1 hasta", ent, ":", numeros)