import sqlite3 as sql

def insertRow(nombre, apellido, celular, email):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"INSERT INTO persona (nombre, apellido, celular, email) VALUES ('{nombre}','{apellido}','{celular}','{email}')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"SELECT * FROM persona"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def updateFields(id, nombre, apellido, celular, email):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"UPDATE persona SET nombre='{nombre}', apellido='{apellido}', celular='{celular}', email='{email}' WHERE id='{id}'"
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def deleteRow(id):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"DELETE FROM persona WHERE id='{id}'"
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def search(apellido):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"SELECT * FROM persona WHERE apellido like '%{apellido}%'"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos
