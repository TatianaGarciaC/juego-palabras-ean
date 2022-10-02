import time
import puntajes

"""
    Metodo bucle que recorre las letras de la palabra ingresada por el usuario
    y muestra la cercania de las letras con la palabra secreta 

    Parametros
    ----------
    nombre : cadena
        Nombre del usuario
    palabraIngresada : cadena
        Palabra ingresada por el usuario
    palabraSecreta : cadena
        Palabra que el sistema escoge aleatoria para el nivel     
    lista : lista
        Lista de palabras base de datos del nivel seleccionado

"""
def recorrerPalabra(nombre,palabraIngresada,palabraSecreta,lista):
    print(nombre,palabraIngresada,palabraSecreta,lista)
    #inicio del nivel
    vidas=8
    aciertos=0
    inicioNivel = time.perf_counter()

    #Bucle mientras el usuario no adivine la palabra o se quede sin vidas
    while palabraIngresada != palabraSecreta:

        #Declaracion de variables palabra ingresada y secreta
        palabraIngresada = str(input(" Ingrese la palabra: "))
        palabraIngresada = palabraIngresada.lower()
        palabraSecreta = palabraSecreta.rstrip("\n")

        #Validar palabra 
        existePalabra = False
        palabraAdivinada = False

        #Validar que la palabra exista en la base de datos del nivel
        for palabra in lista:
            if (palabra.rstrip("\n") == palabraIngresada):
                existePalabra = True
        #Validar el largo de la palabra con la secreta del nivel
        if(len(palabraIngresada) != len(palabraSecreta)):
            print(f"\033[1;41m La cantidad de letras debe ser: {len(palabraSecreta)} para este nivel.\033[0;0m \n")
        
        #Mostrar que la palabra no existe en la base de datos del nivel
        if (existePalabra == False):
            print(f"\033[1;41m Por favor ingrese una palabra valida.\033[0;0m \n")
        else:
            #Pierde una vida por el intento
            vidas-=1
            #Si el usuario se queda sin vidas, guardar puntaje y finalizar el nivel
            if vidas == 0:
                print(f"\u001b[32m Vidas agotadas, la palabra era {palabraSecreta}\033[0;0m \n")
                finNivel = time.perf_counter()
                tiempoJuego = int(finNivel - inicioNivel)
                puntajes.adicionarPuntaje(nombre,aciertos,palabraAdivinada,tiempoJuego,palabraSecreta,vidas)
                break
            else:  
                #Contador de vidas
                print(f"\u001b[32m Vidas restantes: {vidas} \033[0;0m ")
                #Recorrer las letras de la palabra secreta
                for i in range(len(palabraSecreta)):
                    #Si la letra está en la posición y es la letra correcta
                    if palabraIngresada[i] == palabraSecreta[i]:
                        print(f"\033[1;42m {palabraIngresada[i].upper()} \033[0;0m", end="")
                        aciertos+=2
                    #Si la letra está en la palabra pero no en la posición correcta
                    elif palabraIngresada[i] in palabraSecreta:
                        print(f"\u001b[44;1m {palabraIngresada[i].upper()} \033[0;0m", end="") 
                        aciertos+=1   
                    #La letra no está en la palabra
                    else:
                        print(f"\033[1;40m {palabraIngresada[i].upper()} \033[0;0m", end="")
            
            #Validar si el usuario adivino la palabra secreta
            if(palabraIngresada==palabraSecreta):
                palabraAdivinada=True

            #Si adivino la palabra guardar el puntaje y finalizar el nivel
            if(palabraAdivinada):
                finNivel = time.perf_counter()
                tiempoJuego = int(finNivel - inicioNivel)
                puntajes.adicionarPuntaje(nombre,aciertos,palabraAdivinada,tiempoJuego,palabraSecreta,vidas)
        
