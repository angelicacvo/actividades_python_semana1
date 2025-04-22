contraseña = input("Ingresa la contraseña ")

def verificar_contraseña():
    if contraseña == "python123":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")

verificar_contraseña()