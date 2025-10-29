import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadaw",
    password="Accesoadatos2526$",
    database="empresadaw"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    1,
    "Bryan Alejandro",
    "Avila Castro",
    "info@Brypro.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()