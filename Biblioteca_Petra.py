import pymysql

# Establecer conexion a la base de datos
db = pymysql.connect("127.0.0.1","root","root","Libreria")

# crear obejeto cursor
cr = db.cursor()

#Agregar elementos a la tabla Libros


def agregar_libros(nombre, autor, editorial):
    cr.execute("""INSERT INTO Libros(nombre,autor,editorial) VALUES(%s,%s,%s)""", (nombre, autor, editorial))
    db.commit()



def mostrar_libros():
    cr.execute("""SELECT * FROM Libros""")
    listado = cr.fetchall()
    for i in listado:
        print(i)


def borrar_libro(nombre):
    cr.execute('''DELETE FROM Libros WHERE nombre = %s''', (nombre))
    db.commit()

def cerrar_db():
    db.close()

