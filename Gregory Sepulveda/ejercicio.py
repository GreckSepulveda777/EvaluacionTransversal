from os import system
from fun_file import *

system("cls")
peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]}

cartelera = {
'P101': [5990, 40],
'P102': [7990, 0],
'P103': [4990, 25],
'P104': [6990, 12],
'P105': [8990, 8],
'P106': [7490, 3]}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1.- Cupos por genero")
    print("2.- Busqueda de peliculas por rango de precio")
    print("3.- Actualizar Precio de Pelicula")
    print("4.- Agregar Pelicula")
    print("5.- Eliminar Pelicula")
    print("6.- Salir")
    try:
        opc = int(input(">>> "))
        match (opc):
            case 1:
                cupos_genero(peliculas,cartelera,input("genero: "))
            case 2:
                mini = ingresar_entero("Ingrese precio minimo: ")
                maxi = ingresar_entero("Ingrese precio maximo: ")
                busqueda_precio(cartelera,peliculas,mini,maxi)
            case 3:
                actualizar_precio(cartelera)
            case 4:
                agregar_pelicula(peliculas,cartelera,input("Ingrese codigo: "),input("Ingrese Titulo: "),input("Ingrese genero: "),ingresar_entero("Ingrese duracion: "),input("Ingrese calificacion (A,B o C):"),input("Ingrese idioma: "),input("Es 3d?: "),ingresar_entero("Ingrese Precio: "),ingresar_entero("Ingrese cupos: "))
            case 5:
                eliminar_pelicula(cartelera,peliculas,input("Ingrese Codigo: "))
            case 6:
                break
            case _:
                print("Debe seleccionar una opción válida")
    except:
        print("Debe seleccionar una opción válida")
    
print("Programa finalizado")