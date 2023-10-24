
def verificar_edad(edad:int) -> int:
    if edad < 0:
        raise ValueError('Edad incorrecta ' + str(edad))
    return edad

if __name__ == '__main__':
    numeroCorrecto = False
    edad = None
    while not numeroCorrecto:
        try:
            ent = int(input("Ingresa tu edad "))
            edad = verificar_edad(ent)
            numeroCorrecto = True
        except ValueError:
            if edad == None:
                print('Introduzce un numero.')
            else:
                print('Es numero es incorrecto')

    for i in range(1, edad + 1):
        print(i)
