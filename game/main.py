import random

user_option = '''
    Bienvenido al juego de piedra papel o tijera en python.
    Para poder jugar tendras que elegir: 
    piedra, papel o tijera
    Escribe tu opcion:
    '''
    
def choose_options():
    options = ('piedra', 'papel', 'tijera')
    option = input(user_option)
    User_selection = option.lower()
    
    
    if not User_selection in options:
        print('Esa opcion no es valida')
        return None, None

    computer_option = random.choice(options)

    print('User option => ', User_selection)
    print('Computer option => ', computer_option)
    
    return User_selection, computer_option

def check_rules(User_selection, computer_option, user_wins, computer_wins):
    wins_user = 'Felicidades, le ganaste a la computadora'
    wins_computer = 'Que mal, la computadora te gano'
    
    if User_selection == computer_option:
        print('Empate!')
        
    elif User_selection == 'piedra':
        if computer_option == 'tijera':
            print(f'Piedra gana a tijera, {wins_user}')
            user_wins += 1
        else:
            print(f'Papel le gana a piedra, {wins_computer} ')
            computer_wins += 1
    elif User_selection == 'papel':
        if computer_option == 'piedra':
            print(f'papel gana a piedra, {wins_user}')
            user_wins += 1
        else: 
            print(f'tijeras les gana a papel, {wins_computer}')
            computer_wins += 1
    elif User_selection == 'tijera':
        if computer_option == 'papel':
            print(f'{wins_user}')
            user_wins += 1
        else:
            print(f'Piedra le gana a tijera, {wins_computer}')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    
    while True: 
        
        print('*'  * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('computer wins => ', computer_wins)
        print('User Wins => ', user_wins)
        
        User_selection, computer_option = choose_options()
        user_wins, computer_wins=check_rules(User_selection, computer_option,user_wins, computer_wins)


        
        if computer_wins == 2:
            print('Te gano la computadoram paila')
            break 
        if user_wins == 2:
            print('Joda mani felciitaciones, le ganaste a la computadora')
            break
        rounds += 1
        
run_game()