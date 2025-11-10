#importamos la base de datos
import mysql.connector

#Conexion y cursor:
conexion = mysql.connector.connect(
  host="localhost",
  user="Bryan",
  password="123",
  database="portafolioexamen"
  )
cursor = conexion.cursor()

#Comenzamos:
print("Bienvenidos a la aplicacion")

#Creamos el bucle infinito:
while True:
    print("Selecciona una opcion:")
    print("1.-Crear un registro")
    print("2.-Listar registros")
    print("3.-Actualiar registro")
    print("4.-Eliminar registro")

    opcion = int(input("Elige tu opcion: "))

    #Creamos if - elif:
    if opcion == 1:
        #Insertamos:
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        categoria_id = input("Introduce el id de la categoria: ")
        cursor.execute('''
        INSERT INTO piezasportafolio VALUES (
        NULL,
        "'''+titulo+'''",
        "'''+descripcion+'''",
        "'''+fecha+'''",
        '''+categoria_id+'''
        );
        ''')
        conexion.commit()
    elif opcion == 2:
        #seleccionamos:
        cursor = conexion.cursor()
        cursor.execute('''SELECT * FROM piezasportafolio;''')
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
    elif opcion == 3:
        #Actualizamos:
        identificador = input("Introduce el id a actualizar: ")
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        categoria_id = input("Introduce el id de la categoria: ")
        cursor.execute('''
        UPDATE piezasportafolio SET 
        titulo = "'''+titulo+'''",
        descripcion = "'''+descripcion+'''",
        fecha = "'''+fecha+'''",
        categoria_id = '''+categoria_id+'''
        WHERE identificador = '''+identificador+''';
        ''')
        conexion.commit()
    elif opcion == 4:
        #Eliminamos:
        identificador = input("Introduce el id a eliminar: ")
        cursor.execute('''
        DELETE FROM piezasportafolio
        WHERE identificador = '''+identificador+'''
        ''')
        conexion.commit()