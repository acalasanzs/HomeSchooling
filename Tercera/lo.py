def Juego():
    """
    Quiero hacer un juego para adivinar números
    """
    numero = 50

    pregunta = int(input("Qué número piensas?"))

    if pregunta > numero + 10:
        print("caliente")
    elif pregunta < numero - 10:
        print("Muy frío")
    else:
        if pregunta < numero:
            print("frio")
        elif pregunta > numero:
            print("Muy caliente")
        else:
            print("Has acertado")


while True:
    Juego()
