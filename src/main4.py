
def strisdigit(numero):
    if not numero.isdigit():
        raise ValueError('La entrada no es correcta')
    return numero

if __name__ == '__main__':
    numeroCorrecto = False
    numero = None
    while not numeroCorrecto:
        try:
            ent = input("Ingresa un numero ")
            numero = strisdigit(ent)
            numeroCorrecto = True
        except ValueError:
            if numero == None:
                print('Introduzce un numero.')
            else:
                print('Es numero es incorrecto')
                
    print(numero)