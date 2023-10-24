
def cuenta_atras(n):
    if n < 0:
        raise ValueError("El numero debe ser un positivo")
    cuenta_atras = [str(x) for x in range(n, -1, -1)]
    return ", ".join(cuenta_atras)

if __name__ == '__main__':
    numeroCorrecto = False
    numeros = None
    while not numeroCorrecto:
        try:
            ent = int(input("Ingresa un numero positivo "))
            numeros = cuenta_atras(ent)
            numeroCorrecto = True
        except ValueError:
            if numeros == None:
                print('Introduzce un numero.')
            else:
                print('Es numero es incorrecto')

    print("Impares desde 1 hasta", ent, ":", numeros)
