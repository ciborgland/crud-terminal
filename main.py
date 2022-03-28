import controller as c
import os
import platform
import calendar

ancho = os.get_terminal_size().columns
largo = os.get_terminal_size().lines

titulo = '\33[0;30;31m'
cierre = '\33[0m'
numero = '\33[0;40;32m'

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mitad_del_ancho():
    mitad = ancho/2
    return mitad

def titulo_principal():
    limpiar_pantalla()
    calculo = int(mitad_del_ancho() - 9) 
    print(ancho*'=')
    print(str(calculo*' ') + titulo + 'CRUD EN PYTHON3' + cierre)
    print(ancho*'=')

def titulo_secundario():
    limpiar_pantalla()
    print(ancho*'-')

def crear():
    nombre = str(input('Ingrese su nombre: '))
    apellido = str(input('Ingrese su apellido: '))
    celular = str(input('Ingrese su celular: '))
    email = str(input('Ingrese su email: '))
    c.insertRow(nombre, apellido, celular, email)

def tablas():
    valor_ant_a = 0
    valor_ant_b = 0
    valor_ant_c = 0
    for i in c.readRows(): 
        for j in c.readRows():
            valor = int(len(j[1]))
            if(valor_ant_a<valor):
                valor_ant_a = valor
        imprimir_01 = int(valor_ant_a - len(i[1])) + 1
        for k in c.readRows():
            valor = int(len(k[2]))
            if(valor_ant_b<valor):
                valor_ant_b = valor
        imprimir_02 = int(valor_ant_b - len(i[2])) + 1
        for l in c.readRows():
            valor = int(len(l[3]))
            if(valor_ant_c<valor):
                valor_ant_c = valor
        imprimir_03 = int(valor_ant_c - len(i[3])) + 1
        print(' '+'|'+' '+i[1]+imprimir_01*' '+'|'+' '+i[2]+imprimir_02*' '+'|'+' '+i[3]+imprimir_03*' '+'|'+' '+i[4])

def actualizar():
    id = input('Ingrese el ID a modificar: ')
    nombre = input('Ingresar nombre: ')
    apellido = input('Ingresar apellido: ')
    celular = input('Ingresar celular: ')
    email = input('Ingresar email: ')
    c.updateFields(id, nombre, apellido, celular, email)

def eliminar():
    id = input('Ingrese el ID a eliminar: ')
    c.deleteRow(id)

def buscar():
    apellido = input('Ingrese el Apellido a buscar: ')
    print('')
    for i in c.search(apellido):
        print('Id : '+str(i[0]))
        print('Nombre : '+i[1])
        print('Apellido : '+i[2])
        print('Celular : '+i[3])
        print('Email : '+i[4])

def calendario():
    anio = int(input('Ingrese el año: '))
    sepracion_horiz = 1
    separacion_vert = 1
    calle = 3
    meses_por_fila = 3
    calendar.prcal(anio, sepracion_horiz, separacion_vert, calle, meses_por_fila)    

def menu():
    while True:
        titulo_principal()
        print(numero +'[1]' + cierre + ' Insertar registro')
        print(numero +'[2]' + cierre + ' Listar registros')
        print(numero +'[3]' + cierre + ' Actualizar registro')
        print(numero +'[4]' + cierre + ' Eliminar registro')
        print(numero +'[5]' + cierre + ' Buscar registro')
        print(numero +'[6]' + cierre + ' Calendario')
        print(numero +'[7]' + cierre + ' Salir')
        print(ancho*'=')

        try:
            opcion = int(input('Seleccionar una opcion: '))
            if(opcion == 1):
                i = 0
                while i < 1:
                    titulo_secundario()
                    crear()
                    print('Insertados!.')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 2):
                i = 0
                while i < 1:
                    limpiar_pantalla()
                    titulo_secundario()
                    tablas()
                    print('')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 3):
                i = 0
                while i < 1:
                    limpiar_pantalla()
                    titulo_secundario()
                    actualizar()
                    print('Datos actualizados!.')
                    print('')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 4):
                i = 0
                while i < 1:
                    limpiar_pantalla()
                    titulo_secundario()
                    eliminar()
                    print('Registro eliminado!.')
                    print('')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 5):
                i = 0
                while i < 1:
                    limpiar_pantalla()
                    titulo_secundario()
                    buscar()
                    print('')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 6):
                i = 0
                while i < 1:
                    limpiar_pantalla()
                    titulo_secundario()
                    calendario()
                    print('')
                    tecla = input('Presione tecla para salir: ')
                    if(tecla == 's' or 'S'):
                        i = 1
                    else:
                        i = 1
            elif(opcion == 7):
                limpiar_pantalla()
                break
        except:
            print('Error en elegir las opciones')

if __name__ == '__main__':
    menu()
