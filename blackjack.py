import random


def main(mazo, mano_jugador, mano_casa):
    
    random.shuffle(mazo)      
    
    # Repartir cartas iniciales al jugador y la casa
    mano_jugador.append([mazo.pop() for _ in range(2)])
    mano_casa.extend([mazo.pop() for _ in range(2)])
    
    # Turno del jugador
    while True:
        print(f"Mano del jugador: {mano_jugador[0]} - Valor de la mano: {suma_mano(mano_jugador[0])}")
        
        if suma_mano(mano_jugador[0]) > 21:
            print('Te has pasado de 21 ¡PERDISTE!')
            return
        elif suma_mano(mano_jugador[0]) == 21:
            print('¡Hiciste 21, GANASTE!')
            return
        
        if input("¿Quiere pedir una nueva carta? (s/n): ").lower() != 's':
            break
        
        mano_jugador[0].append(mazo.pop())
    
    # Turno del dealer (la casa)
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
