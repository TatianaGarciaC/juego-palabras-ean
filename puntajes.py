"""
    Metodo encargado de mostrar los puntajes en la terminal 
"""
def verPuntajes():

    #Abrir el archivo base de datos de los puntajes
    file = open("puntajes.txt", 'r')

    #Traer la lista de puntajes
    lista = file.readlines()
    lista = [i.split() for i in lista]
    lista = [i for i in lista if i != []]

    #Ordena la lista de forma ascendente por defecto
    lista.sort(key=lambda x: int(x[0]), reverse=True)
    #Primeros 10 puntajes
    result = lista[:10]

    #Mostrar puntajes en pantalla
    print("\u001b[34;1m╓≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈╖")
    print("\t\t   Puntajes")
    print("╙≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈•≈╝")

    print("\u001b[36;1mPuesto\t\t" + " Puntaje\t\t" + "Nombre \u001b[0m")
    j = 0
    for i in result:
        j += 1
        print(j, "\t\t", i[0], "\t\t\t", i[-1])

"""
    Metodo que adiciona un nuevo puntaje y muestra el fin de la partida

    Parametros
    ----------
    nombre : cadena
        Nombre del usuario
    aciertos : entero
        Cantidad de aciertos en la partida
    palabraAdivinada : boleano
        Si el usuario adivino la palabra secreta
    tiempoJuego : entero
        El tiempo que el usuario jugo el nivel
    palabraSecreta : cadena
        Palabra que el sistema escoge aleatoria para el nivel            
    vidasRestantes : entero
        Vidas sobrantes del nivel
"""
def adicionarPuntaje(nombre,aciertos,palabraAdivinada,tiempoJuego,palabraSecreta,vidasRestantes):
    
    #Los puntos iniciales son el largo de la palabra secreta por 10 por las vidas restantes
    puntos=10*len(palabraSecreta)*vidasRestantes
    
    #Mensaje si el usuario adivino la palabra y paso el nivel
    if(palabraAdivinada):
        print("\u001b[33m ¡Felicitaciones nivel superado!")
    else: 
        print(f"\u001b[33m La palabra secreta es:{palabraSecreta}") 

    #El puntaje son los puntos iniciales por los aciertos menos el tiempo de juego
    puntaje=int(puntos*aciertos-tiempoJuego)

    #No guardar puntajes negativos
    if puntaje < 0:
        puntaje = 0

    #Mostrar el resultado final del juego
    print(f"\u001b[33m {nombre} \u001b[0m¡Gracias por jugar!, tu puntaje es de:\u001b[32m {puntaje} \u001b[0m")

    #Guardar el nuevo puntaje en la base de datos de los puntajes 
    file = open("puntajes.txt", 'a')
    file.write((str(puntaje)) + "\t\t" + (nombre) + "\n")
    file.close()
