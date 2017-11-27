import Biblioteca_Petra
def main():
    print("Bienvenido a la Biblioteca Petra")
    while True:
        print("1.Agregar Libros: ")
        print("2.Listar Libros: ")
        print("3.Borrar Libro: ")
        print("5.Salir: ")
        opc = int(input("Escoja la opcion: "))

        if opc == 5:
           print("Adios....")
           break

        elif opc == 1:
            print("Agregue la siguiente informacion")
            nombre = input("Nombre del Libro: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            Biblioteca_Petra.agregar_libros(nombre, autor, editorial)

        elif opc == 2:
            print("Lista de Libros")
            Biblioteca_Petra.mostrar_libros()

        else:
            print("Libros disponibles")
            Biblioteca_Petra.mostrar_libros()
            nombre = input("Introduzca el id del libro que desea borrar:  ")
            Biblioteca_Petra.borrar_libro(nombre)

    Biblioteca_Petra.cerrar_db()



main()