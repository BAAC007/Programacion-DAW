import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadaw",
    password="Accesoadatos2526$",
    database="empresadaw"
)
cursor = conexion.cursor()
cursor.execute('''
    SELECT * FROM clientes;
  );
''')

filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
cursor.close()
conexion.close()