from funciones_parcial import *

# Enunciado:
# Se dispone de un archivo con datos acerca de películas, que tiene el siguiente formato:
# id_peli, titulo, genero, rating
# por ejemplo: 1,Adventures of Rocky,sin genero,0
# 2,My Brother the Devil,sin genero,0
# 3,Criminal,sin genero,0


# Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
# nuevos archivos de salida de formato similar filtrados por varios criterios:
lista_opciones = ["1) Cargar archivo .CSV.","2) Imprimir lista.","3) Asignar rating.",
                  "4) Asignar género.","5) Filtrar por género.","6) Ordenar películas.",
                  "7) Informar Mejor Rating.","8) Guardar películas.","9) Salir."]
lista_generos = ["drama","comedia","acción","terror"]
# el programa contará con el siguiente menú:
seguir = True
lista_cargada = False
generos_cargados = False
rating_cargados = False
while seguir:
    match menu_con_lista(lista_opciones):
        case "1":
            # 1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos
            # del mismo.
            if not lista_cargada:
                lista_peliculas = cargar_lista_csv("movies.csv")
                lista_cargada = True
            else:
                print("Ya cargaste la lista")
        case "2":
            # 2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
            if lista_cargada:
                imprimir_peliculas(lista_peliculas)
            else:
                print("Primero carga la lista.")
        case "3":
            # 3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
            # función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
            # calculado de manera aleatoria se mostrará por pantalla el mismo.
            # lista_ratings = mapear_lista(lambda peli: peli["rating"] + generar_rating_random(),lista_peliculas)
            # print(lista_rating)
            if lista_cargada:
                asignar_rating_random(lista_peliculas)
                rating_cargados = True
            else:
                print("Primero carga la lista.")
        case "4":
            # 4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
            # función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
            # 1: drama
            # 2: comedia
            # 3: acción
            # 4: terror
            if lista_cargada:
                asignar_genero_random(lista_peliculas, lista_generos)
                generos_cargados = True
            else:
                print("Primero carga la lista.")
            # imprimir_peliculas(lista_peliculas)
            # lista_genero = mapear_lista(lambda peli: peli["genero"] )
        case "5":
            # 5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero donde solo
            # aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
            if lista_cargada and generos_cargados:
                genero_correcto = True
                while genero_correcto:
                    genero_pedido = input("Ingrese genero a filtrar: ")
                    for genero in lista_generos:
                        if genero_pedido == genero:
                            lista_genero_pedido = filter_list(lambda peli: peli["genero"] == genero_pedido,lista_peliculas)
                            crear_archivo_csv(f"{genero_pedido}.csv",lista_genero_pedido)
                            genero_correcto = False
                    if genero_correcto == True:
                        print("Genero incorrecto, vuelva a intentarlo.")
            else:
                print("Primero carga los generos.")
        case "6":
            # 6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
            # género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
            # sort_list_lambda(lista_peliculas,lambda peli_ant,peli_act: peli_ant["genero"] == 
            #                  peli_act["genero"] and peli_ant["rating"] < peli_act["rating"])
            # sort_list_lambda(lista_peliculas,lambda peli_ant,peli_act: peli_ant["rating"] < peli_act["rating"])
            # puntoseis(lista_peliculas)
            # imprimir_peliculas(lista_peliculas)
            if lista_cargada and generos_cargados and rating_cargados:
                puntoseis(lista_peliculas)
            else:
                print("Falta generar la lista o los generos o los ratings")
            # imprimir_peliculas(lista_peliculas)
        case "7":
            # 7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
            if lista_cargada and rating_cargados:
                pelicula_mejor_rating = reduce_lista(lambda peli_ant,peli_act:peli_ant 
                                                if peli_ant["rating"] > peli_act["rating"] else peli_act,lista_peliculas)
                print(f"La peli con mejor rating es:\nTitulo: {pelicula_mejor_rating["titulo"]}"
                f"\nRating: {pelicula_mejor_rating["rating"]}")
            else:
                print("Falta generar los ratings")
        case "8":
            # 8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
            if lista_cargada and generos_cargados and rating_cargados:
                crear_archivo_json("peliculas_guardadas.json",lista_peliculas)
            else:
                print("Falta generar la lista o los generos o los ratings")
        case "9":
            # 9) Salir.
            seguir = not pedir_confirmacion("¿Quieres salir? s/n: ")
            continue
    pausar()



# Requerimientos del desarrollo.
# Nota 1: Todas las funciones deben estar en un módulo distinto al programa principal
# y respetar las reglas de estilo de la cátedra.
# Nota 2: Todas las funciones deben tener su propio docstring
# Nota 3: Para ordenar se deberá utilizar los algoritmos de ordenamiento vistos en la catedra














