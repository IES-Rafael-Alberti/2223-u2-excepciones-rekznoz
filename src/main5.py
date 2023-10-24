
def verificar_pass(password):
    seguridad = "pass123"
    if password != seguridad:
        raise NameError("Incorrect Password!!")

if __name__ == "__main__":
    try:
        passwd = input("Escribe la contraseña ")
        verificar_pass(passwd)
        print("Contraseña correcta !!")

    except NameError as e:
        print(e)