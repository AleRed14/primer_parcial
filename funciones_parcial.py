def obtener_path_actual(nombre_archivo:str)->str:
    """Nos indica la ubicacion actual en la que estamos

    Args:
        nombre_archivo (str): Nombre del archivo al cual buscar la ubicacion

    Returns:
        str: el directorio del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

# def new_pelicula(ident:int,titulo:str,genero:str,edad:int)->dict:
#     pelicula = {}
#     pelicula["id"] = ident
#     pelicula["titulo"] = titulo
#     pelicula["genero"] = genero
#     pelicula["rating"] = edad

def new_pelicula(ident:int,titulo:str,genero:str,rating:int)->dict:
    """Crea un nuevo diccionario de una pelicula

    Args:
        ident (int): id de la pelicula
        titulo (str): titulo de la pelicula
        genero (str): genero de la pelicula
        rating (int): rating de la pelicula

    Returns:
        dict: La pelicula con sus keys y valores
    """
    pelicula = {}
    pelicula["id"] = ident
    pelicula["titulo"] = titulo
    pelicula["genero"] = genero
    pelicula["rating"] = rating
    
    return pelicula

# def cargar_lista_csv(nombre_archivo:str)->list:
#     lista = []
#     with open(obtener_path_actual(nombre_archivo), "r", 
#               encoding="utf-8") as archivo:
#         encabezado = archivo.readline().strip("\n").split(",")
#         # El slip separa un string por el parametro que le pasemos (en este caso
#         # una coma) y lo mete en una lista
#         for linea in archivo.readlines():
#             linea = linea.strip("\n").split(",")
#             # linea se convierte en una lista donde los datos son sus elementos.
#             id, titulo, genero, rating = linea 
#             # se llama umpacking o desempacar
#             # a cada uno de esos elementos se le asigna una variable.
#             lista.append(new_pelicula(int(id),titulo,genero,
#                                      int(rating)))
#     return lista

def cargar_lista_csv(nombre_archivo:str)->list:
    """Carga los datos de un archivo csv a una lista

    Args:
        nombre_archivo (str): nombre del archivo que buscamos

    Returns:
        list: Lista con diccionarios de los datos del archivo
    """
    lista = []
    with open(obtener_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip("\n").split(",")
        # El slip separa un string por el parametro que le pasemos (en este caso
        # una coma) y lo mete en una lista
        # print(encabezado)
        for linea in archivo.readlines():
            linea = linea.strip("\n").split(",")
            # linea se convierte en una lista donde los datos son sus elementos.
            # print(linea)
            id, titulo, genero, rating= linea 
            # se llama umpacking o desempacar
            # a cada uno de esos elementos se le asigna una variable.
            # print(linea)
            lista.append(new_pelicula(int(id),titulo,genero,int(rating)))
            # Se agregan los elementos a un diccionarios que se agrega a una lista.
            # print(dato)
        # print(linea)
    # for persona in lista:
    #     print(persona)
    # print(lista)
    return lista

def crear_archivo_csv(nombre_archivo:str, lista:list)->None:
    """Crea un archivo csv y lo carga con los datos que le pasemos

    Args:
        nombre_archivo (str): que nombre le queremos poner al archivo
        lista (list): los datos a cargar en el archivo
    """
    with open(obtener_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            lista_values = []
            for value in values:
                
                if isinstance(value,int):
                    lista_values.append(str(value))
                elif isinstance(value,float):
                    lista_values.append(str(value))
                else:
                    lista_values.append(value)
            linea = ",".join(lista_values) + "\n"
            archivo.write(linea)

def cargar_lista_json(nombre_archivo:str)->list:
    """Carga los datos de un archivo json a una lista

    Args:
        nombre_archivo (str): nombre del archivo que buscamos

    Returns:
        list: Lista con diccionarios de los datos del archivo
    """
    import json
    with open(obtener_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        personas = json.load(archivo)
    return personas

def crear_archivo_json(nombre_archivo:str, lista:list)->None:
    """Crea un archivo json y lo carga con los datos que le pasemos

    Args:
        nombre_archivo (str): que nombre le queremos poner al archivo
        lista (list): los datos a cargar en el archivo
    """
    import json
    with open(obtener_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)

def limpiar_pantalla()->None:
    """Limpia la pantalla
    """
    import os #Viene de sistema operativo
    os.system("cls") # Se encarga de limpiar la pantalla de todo lo de atras

def menu_con_lista(lista:list) -> str:
    """Imprime una lista con las opciones de un menu y pide un string como opcion a elegir

    Args:
        lista (list): Lista con las opciones a mostrar

    Returns:
        str: El string de la opcion elegida
    """
    limpiar_pantalla()
    for opcion in lista:
        print(opcion)
    return input("Ingrese opcion: ").lower()

def imprimir_peliculas(lista:list)->None:
    """Imprime un marco con los datos de una pelicula y cada pelicula una por una

    Args:
        lista (list): lista que contenga las peliculas
    """
    print(" ID |                   Titulo          |     Genero    | Rating")
    print("-----------------------------------------------------------------")
    for pelicula in lista:
        imprimir_pelicula(pelicula)

def imprimir_pelicula(peli:dict)->None:
    """Imprime los datos de una pelicula

    Args:
        peli (dict): la pelciula a mostrar sus datos
    """
    print(f"{peli["id"]:4}|{peli["titulo"]:35}|{peli["genero"]:15}|{peli["rating"]:3}")

def mapear_lista(mapeadora, lista:list)->list:
    """Se encarga de separar los datos que indiquemos de una lista

    Args:
        mapeadora (_type_): funcion que se encarga de diferenciar que datos queremos
        lista (list): lista a procesar

    Returns:
        list: lista con los datos de una key mapeada
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(mapeadora(el))
    return lista_retorno

def generar_numero_random(desde:int,hasta:int)->int:
    """Genera un numero random

    Args:
        desde (int): El numero minimo a generar
        hasta (int): El numero maximo a generar

    Returns:
        int: Un numero random
    """
    from random import randint
    return randint(desde,hasta)

def generar_rating_random()->float:
    """Genera un rating random con una decimal

    Returns:
        float: El rating
    """
    MIN = 1
    MAX = 10
    rating = f"{generar_numero_random(MIN,MAX)}.{generar_numero_random(0,9)}"
    return float(rating)

def asignar_rating_random(lista:list)-> None:
    """Asigna el valor del rating a una key de un diccionario

    Args:
        lista (list): Lista que contenga los diccionarios
    """
    for peli in lista:
        peli["rating"] = generar_rating_random()

def generar_genero_random(lista_generos:list)->str:
    """Genera un genero random

    Args:
        lista_generos (list): Lista de los generos

    Returns:
        str: El genero elegido aleatoreamente
    """
    MIN = 0
    MAX = 3
    genero = lista_generos[generar_numero_random(MIN,MAX)]
    return genero

def asignar_genero_random(lista:list, lista_generos:list)->None:
    """Asigna un genero a una key de un diccionario

    Args:
        lista (list): lista con los diccionarios
        lista_generos (list): lista con los generos
    """
    for peli in lista:
        peli["genero"] = generar_genero_random(lista_generos)

def filter_list(filtradora, lista:list)->list:
    """Filtra una lista con los parametros que le pasemos

    Args:
        filtradora (_type_): funcion que indica si swapear o no el dato
        lista (list): lista a ser filtrada

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for empleado in lista:
        if filtradora(empleado):
            lista_filtrada.append(empleado)
    return lista_filtrada

def swap_lista(lista:list, i:int, j:int)->None:
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar

# def ordenar_lista(criterio, lista:list)->None:
#     tam = len(lista)
#     for i in range(tam - 1):
#         for j in range(i + 1, tam):
#             if criterio(lista[i], lista[j]):
#                 swap_lista(lista,i,j)

# def sort_list_lambda(lista:list,comparador)->None:
#     tam = len(lista)
#     for i in range(tam):
#         for j in range(i + 1):
#             if comparador(lista[i],lista[j]):
#                 swap_lista(lista,i,j)

# def sort_list(lista:list,comparador)->None:
#     tam = len(lista)
#     for i in range(tam):
#         for j in range(i + 1):
#             if comparador(lista[i],lista[j]) > 0:
#                 swap_lista(lista,i,j)

def reduce_lista(funcion, lista:list)->dict:
    """compara todos los diccionarios de una lista segun el parametro que le pasemos

    Args:
        funcion (_type_): funcion que determina que que diccionario retornar
        lista (list): lista con los diccionarios

    Returns:
        dict: el diccionario que paso la funcion
    """
    ant = lista[0]
    for i in range(1,len(lista)):
        ant = funcion(ant,lista[i])
    return ant

def pedir_confirmacion(mensaje:str)->bool:
    """Pide confirmacion de salida

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        bool: Retorna True si la respuesta es si, false en caso contrario
    """
    rta = input(mensaje).lower()
    return rta == "s"

def pausar()->None:
    """Pausa el programa para leerlo
    """
    import os #Viene de sistema operativo
    os.system("pause") # Pausa el programa hasta que se toque alguna tecla, 
                       #sirve para que no se borre insantaneamente lo mostrado

def puntoseis(lista:list)->None:
    """Ordena las peliculas por genero y dentro del genero por rating descendente

    Args:
        lista (list): Lista con las pelicuals
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i]["genero"] != lista[j]["genero"]:
                if lista[i]["genero"] < lista[j]["genero"]:
                    swap_lista(lista,i,j)
            elif lista[i]["rating"] > lista[j]["rating"]:
                    swap_lista(lista,i,j)