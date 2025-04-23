invitadas = ['Juliana', 'Sofía', 'Sara', 'Camila']
nombre_usuaria = input("Ingresa tu nombre ")

def validar_invitadas():
    if nombre_usuaria in invitadas:
        print("Estás en la lista de invitadas")
    else:
        print("No estás en la lista de invitadas")
    
validar_invitadas()