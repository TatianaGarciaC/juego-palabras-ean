import random
import puntajes
import validarPalabra

#Iniciar el juego, pedir el nombre de usuario, mostrar reglas y opciones al usuario
print("\u001b[34;1m╓≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈╖")
print("\t\t  ¡JUGUEMOS!")
nombre = str(input("Nombre de jugador: "))
print(f"\n╙≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈╝\u001b[0m")

print(f"¡Bienveid@! \u001b[33;1m{nombre}\033[0;0m\u001b[37m pistas para adivinar la palabra: \033[0;0m \n", end="")

print(f"\033[1;42m A \033[0;0m \u001b[37;1m La letra está en la palabra y en la posición correcta. \033[0;0m \n", end="")
print(f"\u001b[44;1m A \033[0;0m \u001b[37;1m La letra está en la palabra pero en la posición incorrecta. \033[0;0m \n", end="")
print(f"\033[1;40m A \033[0;0m \u001b[37;1m La letra no está en la palabra. \033[0;0m \n", end="")

print("Opciones disponibles: \n \u001b[37m 1 Nivel fácil (Cosas de 4 letras español) \n \u001b[36m 2 Nivel medio (Comidas de 5 letras español) \n \u001b[35m 3 Nivel difícil (Animales de 6 letras español) \n \u001b[31m 4 Nivel experto (Tecnología de 7 letras terminos técnicos español e inglés) \n \u001b[33m 5 Ver puntajes históricos")

#El usuario ingresa la opción deseada 
opcion = input("\u001b[37m \n Ingresa una opción: ")
palabraIngresada=""

#Iniciar los datos según la opción ingresada

#Nivel 1 
if opcion == "1":
    palabraIngresada = ""
    f = open("nivel1.txt", "r")
    lista = f.readlines()
    f.close()
    palabraSecreta = random.choice(lista)
#Nivel 2
elif opcion == "2":
    palabraIngresada = ""
    f = open("nivel2.txt", "r")
    lista = f.readlines()
    f.close()
    palabraSecreta = random.choice(lista)
#Nivel 3
elif opcion == "3":
    palabraIngresada = ""
    f = open("nivel3.txt", "r")
    lista = f.readlines()
    f.close()
    palabraSecreta = random.choice(lista)
#Nivel 4
elif opcion == "4":
    palabraIngresada = ""
    f = open("nivel4.txt", "r")
    lista = f.readlines()
    f.close()
    palabraSecreta = random.choice(lista)
#Ver puntajes
elif opcion == "5":
    puntajes.verPuntajes()

#Si la opción es un nivel
if(opcion!="5"):
    #Palabra secreta que se genera en la opción del nivel a minúsculas
    palabraSecreta = palabraSecreta.lower()
    #Invocar validarPalabra usa el metodo de ue recorre las letras de la palabra ingresada
    validarPalabra.recorrerPalabra(nombre,palabraIngresada,palabraSecreta,lista)



