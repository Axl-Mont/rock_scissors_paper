''' Importamos el módulo random para las elecciones aleatorias.'''
import random

OPTIONS = ('piedra', 'papel', 'tijera')

WINNING_CONDITION = [
    # Piedra, Papel, Tijera
    [0, -1, 1],  # Piedra
    [1, 0, -1],  # Papel
    [-1, 1, 0]   # Tijera
]

def determine_winner(player_choice, player_wins, computer_choice, computer_wins):
    """
    Determina el ganador de una ronda de Piedra, Papel y Tijera.

    Args:
        player_choice (str): Elección del jugador ('piedra', 'papel' o 'tijera').
        player_wins (int): Puntuación actual del jugador.
        computer_choice (str): Elección de la computadora ('piedra', 'papel' o 'tijera').
        computer_wins (int): Puntuación actual de la computadora.

    Returns:
        Tuple[int, int]: Nueva puntuación del jugador y de la computadora después de la ronda.
    """
    result = WINNING_CONDITION[OPTIONS.index(player_choice)][OPTIONS.index(computer_choice)]

    if result == 0:
        print('Es un Empate')
    elif result == 1:
        print('¡Ganaste esta ronda!')
        return player_wins + 1, computer_wins
    else:
        print('¡Mr Roboto gana esta ronda!')
        return player_wins, computer_wins + 1

def game_status(round_count, player_name, player_wins, computer_wins):
    """
    Imprime el estado actual del juego.

    Args:
        round_count (int): Número de la ronda actual.
        player_name (str): Nombre del jugador.
        player_wins (int): Puntuación actual del jugador.
        computer_wins (int): Puntuación actual de la computadora.
    """
    print(" ")
    print('*' * 45)
    print(f'{"ROUND "}{round_count}'.center(45))
    print('*' * 45)
    print(" ")
    print(f'{player_name} : {player_wins}  VS  Mr Roboto : {computer_wins}'.center(45))

def main():
    """
    Función principal que ejecuta el juego de Piedra, Papel y Tijera.
    """
    print('Bienvenido al legendario Piedra Papel y Tijera')
    user_wins = 0
    computer_wins = 0
    rounds = 1
    winning_limit = 2
    user_name = input('Para comenzar ingresa tu nombre \n==> ')
    user_name = user_name.capitalize()

    while True:
        game_status(rounds, user_name, user_wins, computer_wins)
        rounds += 1

        user_choice = input('\nElige: Piedra, Papel o Tijera \n=> ').lower()

        if not user_choice in OPTIONS:
            print('\nEsa opción no es válida, vuelve a intentar')
            continue

        computer_choice = random.choice(OPTIONS)

        print(f'\n{user_name} eligió: {user_choice}')
        print(f'Mr Roboto eligió: {computer_choice}\n')

        user_wins, computer_wins = determine_winner(
            user_choice, user_wins,
            computer_choice, computer_wins)

        if user_wins > winning_limit:
            print(f'\n¡El Ganador es {user_name}! ¡Felicidades!')
            break
        if computer_wins > winning_limit:
            print('\nMr Roboto Ganó el juego!\nHasta la próxima!')
            break

if __name__ == "__main__":
    main()

input()
