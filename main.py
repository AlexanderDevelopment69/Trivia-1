import time,sys

import os
cont = 0
contf = 0
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
ORANGE = '\033[33m'
RESET = '\033[39m'
BOLD='\033[01m'
LIGHT='\033[96m'
iniciar_trivia = True
timeout = 5
pregunta1=(
        BLUE +
        "1) ¿En general en los sistemas operativos,con respecto a la ejecución de los programas, es decir para que pasen al estado de Nuevo se considera:?\n"
        + RESET)
pregunta2=(
        BLUE +
        "\n2) Se tiene un sistema de computo diseñado con 24 bits para sus direcciones en memoria física, si el ancho de palabra es de 16 bits,¿Cuantos caracteres puede almacenar ?\n"
        + RESET)
pregunta3=(
        BLUE +
        "\n3) Se requiere mantener en un sistema especificamente 40 procesos, si cada proceso ocupa como máximo 256 KB ¿cuál debería ser el tamaño de memoria a recomendar? Considere el peor de los casos en la concurrencia de procesos.\n"
        + RESET)
pregunta4=(
        BLUE +
        "\n4) Considerando que el grado de multiprogramación es el Tiempo promedio que el CPU está ocupado, entonces en un sistema deberíamos buscar que este valor sea:\n"
        + RESET)
pregunta5=(BLUE + "\n5) La relocalización de memoria se efectua para:\n" +
          RESET)
while iniciar_trivia == True:
    print("--------------------------------------------")
    print(LIGHT+"Bienvenido a mi trivia sobre computación"+RESET)
    print("--------------------------------------------")
    print("Pondremos a prueba tus conocimientos")

    print(
        "Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"
    )

    # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
    

    # Pregunta 1
    print(pregunta1)
    print("a) Que su imágen binaria se encuentre en memoria RAM")
    print("b) Se ejecuta el proceso más importante")
    print(
        "c) Su arquitectura de instrucciones corresponda a la plataforma X86")
    print(
        "d) Sus instrucciones se hayan traducido al lenguaje máquina de la plataforma x86"
    )
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  
    respuesta_1 = input("\nTu respuesta: ")
  

    while respuesta_1 not in ('a', 'b', 'c', 'd'):
        respuesta_1 = input("Ingresa una opcion valida : ")

    if respuesta_1 == 'a':
        print(GREEN + "Respuesta correcta ✔" + RESET)
        cont = cont + 1
    else:
        print(RED + "Respuesta incorrecta ✗" + RED)
        contf = contf + 1

      
    # Pregunta 2
    
    print(
        pregunta2)
    print("a) 16 MB")
    print("b) 32 MB ")
    print("c) 16 Mbits")
    print("d) 64 MB")

    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    respuesta_2 = input("\nTu respuesta: ")
 
    while respuesta_2 not in ('a', 'b', 'c', 'd'):
        respuesta_2 = input("Ingresa una opcion valida : ")

    if respuesta_2 == 'b':
        print(GREEN + "Respuesta correcta ✔" + RESET)
        cont = cont + 1
    else:
        print(RED + "Respuesta incorrecta ✗" + RESET)
        contf = contf + 1

    # Pregunta 3

    print(
        pregunta3)
    print("a) 16 MB")
    print("b) 10 MB ")
    print("c) 32 MB")
    print("d) 64 MB")

    # Almacenamos la respuesta del usuario en la variable "respuesta_3"
    respuesta_3 = input("\nTu respuesta: ")

    while respuesta_3 not in ('a', 'b', 'c', 'd'):
        respuesta_3 = input("Ingresa una opcion valida : ")

    if respuesta_3 == 'a':
        print(GREEN + "Respuesta correcta ✔" + RESET)
        cont = cont + 1
    else:
        print(RED + "Respuesta incorrecta ✗" + RESET)
        contf = contf + 1

    # Pregunta 4

    print(
        pregunta4)
    print("a) Siempre el más cercano a cero")
    print("b) cuando se pueda cercano a cero ")
    print("c) Siempre el más cercano al valor 1.")
    print("d) Es irrelevante ya que no influencia en la velocidad del sistema")

    # Almacenamos la respuesta del usuario en la variable "respuesta_4"
    respuesta_4 = input("\nTu respuesta: ")

    while respuesta_4 not in ('a', 'b', 'c', 'd'):
        respuesta_4 = input("Ingresa una opcion valida : ")

    if respuesta_4 == 'c':
        print(GREEN + "Respuesta correcta ✔" + RESET)
        cont = cont + 1
    else:
        print(RED + "Respuesta incorrecta ✗" + RESET)
        contf = contf + 1

    # Pregunta 5

    print(pregunta5)
    print(
        "a) Modificar las ubicaciones de los datos a zonas de fácil acceso por el procesador"
    )
    print(
        "b) Crear bloques de memoria continuos y así permitir que procesos grandes sean ubicados en memoria "
    )
    print(
        "c) Modificar la ubicación de los bloques asignados a los procesos y así lograr reducir los tiempos de respuesta"
    )
    print(
        "d) Reducir la fragmentación externa de los discos, logrando así mejorar la velocidad del computador"
        + RESET)

    # Almacenamos la respuesta del usuario en la variable "respuesta_4"
    respuesta_5 = input("\nTu respuesta: ")

    while respuesta_5 not in ('a', 'b', 'c', 'd'):
        respuesta_5 = input("Ingresa una opcion valida : ")

    if respuesta_5 == 'c':
        print(GREEN + "Respuesta correcta ✔" + RESET)
        cont = cont + 1
    else:
        print(RED + "Respuesta incorrecta ✗" + RESET)
        contf = contf + 1
    print("\n-----------------------------------")
    print(ORANGE + "Resultados 'Gestion de Memoria'   -" + RESET)
    print("-----------------------------------")
    print("Respuestas correctas :", cont, "         -")
    print("Respuestas incorrectas :", contf, "       -")
    print("-----------------------------------")
    print(ORANGE + "CALIFICACION                      -" + RESET)
    print("-----------------------------------")
    if cont >= 4:
        print(GREEN + "Aprobado" + RESET, "                         -")
        print("-----------------------------------")
        iniciar_trivia = False
    else:
        print(RED + "Desaprobado" + RESET, "                      -")
        print("-----------------------------------")
        print("\n¿Deseas intentar la trivia nuevamente?")
        repetir_trivia = input(
            "Ingresa '1' para repetir, o cualquier tecla para finalizar: ")

        if repetir_trivia != '1':
            iniciar_trivia = False
            print("-------------------------------------------------------------------")
            print(
                "Gracias por hacer el test,esto te ayudara a probar tus conocimientos"
            )
            print("-------------------------------------------------------------------")
        else:
            iniciar_trivia = True
            os.system("clear")
            cont = 0
            contf = 0
