import random

def main(mazo, manos_jugador, mano_casa):
    random.shuffle(mazo)      
    
    # Repartir cartas iniciales al jugador y la casa
    manos_jugador.append([mazo.pop() for _ in range(2)])    # Una sola mano inicial para el jugador
    mano_casa.extend([mazo.pop() for _ in range(2)])        # Mano inicial de la casa
    
    #Verificar si se puede hacer split y preguntar al jugador 
    if manos_jugador[0][0][0] == manos_jugador[0][1][0]:
        print(f"Mano inicial: {manos_jugador[0]}")
        if input("Tienes cartas del mismo valor. ¿Deseas hacer split? (s/n): ").lower() == 's':
            # Realizar el split sin crear variables adicionales
            manos_jugador.append([manos_jugador[0].pop()])  # La segunda carta se convierte en una nueva mano
            manos_jugador[0].append(mazo.pop())             # Agregar una nueva carta a la primera mano
            manos_jugador[1].append(mazo.pop())             # Agregar una nueva carta a la segunda mano

            # Jugar cada mano separadamente
            jugar_mano(mazo, manos_jugador, mano_casa)
            return  # Terminar la ejecución aquí ya que las manos se manejaron en `jugar_mano`

    # Si no se realiza el split, jugar normalmente con la mano inicial
    jugar_mano(mazo, manos_jugador, mano_casa)

    def jugar_mano(mazo, manos_jugador, mano_casa):
        # Recorrer cada mano del jugador y jugar de forma independiente
        for i in range(len(manos_jugador)):
            while True:
                print(f"Mano {i+1} del jugador: {manos_jugador[i]} - Valor de la mano: {suma_mano(manos_jugador[i])}")
                
                if suma_mano(manos_jugador[i]) > 21:
                    print(f"Mano {i+1}: Te has pasado de 21 ¡PERDISTE!")
                    break
                elif suma_mano(manos_jugador[i]) == 21:
                    print(f"Mano {i+1}: ¡Hiciste 21, GANASTE!")
                    break
                
                if input(f"¿Quiere pedir una nueva carta en la Mano {i+1}? (s/n): ").lower() != 's':
                    break
                
                manos_jugador[i].append(mazo.pop())
    
  
    # Seguimos la regla del 17
    while suma_mano(mano_casa) < 17:
        print(f"Mano de la casa: {mano_casa} - Valor de la mano: {suma_mano(mano_casa)}")
        mano_casa.append(mazo.pop())
    
    # Mostrar la mano final del dealer
    print(f"Mano final de la casa: {mano_casa} - Valor de la mano: {suma_mano(mano_casa)}")
    
    if suma_mano(mano_casa) > 21 or suma_mano(mano_jugador[0]) > suma_mano(mano_casa):
        print("¡Felicidades, ganaste!")
    elif suma_mano(mano_casa) > suma_mano(mano_jugador[0]):
        print("La casa gana, ¡mejor suerte la próxima!")
    else:
        print("Empate.")
  

def suma_mano(mano):
    return sum(valor_carta(carta) for carta in mano)

def valor_carta(carta):
    return 10 if carta[0] in ['J', 'Q', 'K'] else (11 if carta[0] == 'A' else int(carta[0]))

# Iniciar el juego    
main([(valor, palo) for palo in ['♠', '♥', '♦', '♣'] for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']], [], [])