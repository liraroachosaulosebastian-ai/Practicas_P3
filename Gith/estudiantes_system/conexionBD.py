import mysql.connector

try:

    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_estudiantes"
    )

    cursor = conexion.cursor(buffered=True)

    print(" Conexión exitosa con la base de datos")

except Exception as e:

    print(
        " No fue posible conectarse a la base de datos"
    )

    print(e)