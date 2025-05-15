# Contexto: Una pequeña biblioteca necesita registrar sus libros en un sistema muy simple. Tareas: Crear: Agrega nuevos libros al diccionario. Cada libro tendrá: ID, Título, Autor, Año de publicación.
# Leer: Muestra todos los libros almacenados.
# Permite buscar un libro por su ID o Título.
# Actualizar: Modifica la información de un libro dado su ID.
# Eliminar: Elimina un libro de la biblioteca usando su ID.

title = ""
author = ""
publication_year = ""
id = 000
books = {}

def create_book(id, title, author, publication_year):
  id += 1
  title = input("Ingresa el nombre del libro ")
  author = input("Ingresa el nombre del autor ")
  publication_year = input("Ingresa el año de publicación del libro ")

  books[id] = {"title" : title, "author": author, "publication_year": publication_year}
  print(books)

create_book(id, title, author, publication_year)

def read_book():
  choice = input("¿deseas buscar el libro por id o por titulo? [id/titulo] ")
  match choice:
    case "id":
      search_id = int(input("Ingresa el id que deseas buscar "))
      if search_id in books:
        title = books[search_id]['title']
        author = books[search_id]['author']
        publication_year = books[search_id]['publication_year']
        print("titulo: ", title)
        print("autor ", author)
        print("año de publicación: ", publication_year)
      else:
        print("No se encontró el libro en la base de datos")
    case "titulo":
      search_title = input("Ingrese el titulo del libro que desea buscar ")
      for i, name in books.items():
        if search_title == name["title"]:
          title = name['title']
          author = name['author']
          publication_year = name['publication_year']
          print("titulo: ", title)
          print("autor ", author)
          print("año de publicación: ", publication_year)
        else:
          print("No se encontró el libro en la base de datos")

read_book()

def update_book():
  search_id = int(input("Ingresa el id que deseas actualizar "))
  if search_id in books:
    choice = input("¿Qué desea cambiar? [t] title, [a] autor, [ap] año de publicación")
    match choice:
      case "t":
        title = input("Ingrese un nuevo título")
        books[search_id]['title'] = title
        print(f"este es el nuevo título {title}")
      case "a":
        author = input("Ingrese un nuevo autor")
        books[search_id]['author'] = author
        print(f"este es el nuevo autor {author}")
      case "ap":
        publication_year = input("Ingrese un nuevo año de publicación")
        books[search_id]['publication_year'] = publication_year
        print(f"este es el nuevo año de publicación {publication_year}")
  else:
    print("El libro no existe en la base de datos")

update_book()

def delete_book():
  search_id = int(input("Ingresa el id que deseas eliminar "))
  if search_id in books:
    books.pop(search_id)
    print("Libro eliminado con éxito")
  else:
    print("El libro no existe en la base de datos")

delete_book()
