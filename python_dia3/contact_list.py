# Crear: Agregar nuevos contactos: cada contacto debe tener: Nombre, Teléfono, Email.
# Leer: Listar todos los contactos. Permitir la búsqueda de un contacto por Nombre.
# Actualizar: Actualizar el número de teléfono o el email de un contacto dado su nombre.
# Eliminar: Eliminar un contacto usando su nombre.
# El nombre del contacto debe ser único dentro de la agenda.
# Al actualizar o eliminar, primero se debe verificar que el contacto exista.

name = ""
phone = ""
email = ""
contact_list = {}

def create_contact(name, phone, email):
  name = input("Ingrese un nombre ").lower()
  phone = input("Ingrese un número de telefono ").lower()
  email = input("Ingrese un email ").lower()

  contact_list[name] = {"phone": phone, "email": email}
  print(contact_list)

create_contact(name, phone, email)

def read_contact(phone, email):
  search_name = input("Ingrese el nombre del contacto que desea buscar ").lower()
  if search_name in  contact_list:
    phone = contact_list[search_name]["phone"]
    email = contact_list[search_name]["email"]
    print("Nombre: ", search_name)
    print("Telefono: ", phone)
    print("email: ", email)
  else:
    print("No se encontró el contacto en la libreta de contactos")

read_contact(phone, email)

def update_contact():
  search_name = input("Ingrese el nombre del contacto que desea cambiar ").lower()
  if search_name in  contact_list:
    choice = input("¿Que desea cambiar? [t] telefono [e] email")
    match choice:
      case "t":
        phone = input("Ingresa el nuevo número de teléfono" )
        contact_list[search_name]["phone"] = phone
        print(f"El nuevo número de telefono es: {phone}")
      case "e":
        email = input("Ingresa el nuevo correo ")
        contact_list[search_name]["email"] = email
        print(f"El nuevo correo es: {email}")
  else:
    print("No se encontró el contacto en la libreta de contactos")

update_contact()

def delete_contact():
  search_name = input("Ingrese el nombre del contacto que desea cambiar ").lower()
  if search_name in  contact_list:
    contact_list.pop(search_name)
    print(f"Contacto: {search_name} eliminado con éxito")
  else:
    print("No se encontró el contacto en la libreta de contactos")

delete_contact()