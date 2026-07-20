def ingresar_entero(propmt):
    while True:
        try:
            entero = int(input(propmt))
            return entero
        except:
            print("Error, ingrese entero")

def validar_codigo(dicc,codigo):
    errores = 0
    while True:
        caracteres = "1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
        if (caracteres not in codigo):
                errores += 1
        for j in dicc:
            if (codigo == j):
                errores += 1
        if (errores == 0):
            return True
        else:
            return False

def validar_texto(texto):
    caracteres = "1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
    if (caracteres not in texto):
        return False
    else:
        return True


def cupos_genero(dicc,dicc2,genero):
    for i in dicc:
        lista = dicc[i]
        if lista[1] == genero.lower():
            pelicula = i
            for j in dicc2:
                if (j == i):
                    cupos = dicc2[j]
                    print(f"hay {cupos[1]} cupos disponibles")

def busqueda_precio(dicc,dicc2,p_min, p_max):
    for i in dicc:
        lista = dicc[i]
        if (p_min <= lista[0] <= p_max):
            pelicula = i
            for j in dicc2:
                if (j ==i):
                    if (lista[1] != 0):
                        peli_titulo = dicc2[j]
                        peli_precio = lista[0]
                        print(f"Titulo: {peli_titulo[0]}, Precio: {peli_precio}")

def buscar_codigo(dicc,codigo):
    for i in dicc:
            if (codigo == i):
                return True
            else:
                return False

def actualizar_precio(dicc):
    while True:
        codigo = input("Ingrese Codigo: ")
        nuevo_precio = ingresar_entero("Ingrese Precio: ")
        for i in dicc:
                if (codigo == i):
                    lista = dicc[i]
                    lista[0] = nuevo_precio                  
        print("¿Desea actualizar otro precio? (s/n)")
        op = input(">> ")
        match op:
            case "n":
                return True
            case "s":
                print("Nueva actualizacion:")

def agregar_pelicula(dicc,dicc2,codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,
precio, cupos):
    codigo_valido = validar_codigo(dicc2,codigo)
    titulo_valido = validar_texto(titulo)
    genero_valido = validar_texto(genero)
    if (duracion >0):
        duracion_valida = True
    else:
        duracion_valida = False
    if (clasificacion != "A") or (clasificacion != "B") or (clasificacion != "C"):
        clasificacion_valida = False
    else:
        clasificacion_valida = True
    
    idioma_valido = validar_texto(idioma)
    if (es_3d == "Si" or es_3d == "si"):
        es_3d_final = True
    else:
        es_3d_final = False
    if (codigo_valido == True) and (titulo_valido == True) and (genero_valido == True) and (duracion_valida == True) and (clasificacion_valida == True) and (idioma_valido == True):
        #dicc 1 pelicula
        dicc[codigo] = [titulo,genero,duracion,clasificacion,idioma,es_3d]
        #dicc2 cartelera
        dicc2[codigo] = [precio,cupos]
    
def eliminar_pelicula(dicc,dicc2,codigo):
    for i in dicc2:
        if codigo == i:
            ind = dicc2.index(i)
            dicc2.pop(ind)
            ind2 = dicc.index(i)
            dicc.pop(ind2)
            return True
        else:
            print("Codigo invalido")
            return False