import random

def monty_stick_single():
    doors = ['car','goat','goat']
    random.shuffle(doors)
    player_choice = (random.randint(0,2))
    return doors[player_choice] == 'car'

def monty_stick_multiple(n):
    wins = sum(monty_stick_single() for _ in range(n))
    winrate = wins / n
    print(f'Winrate = {winrate * 100:.2f}%')
    
def monty_switch_single():
    doors = ['car','goat','goat']
    random.shuffle(doors)
    first_choice = (random.randint(0,2))
    reveal_candidates = [i for i in range(3) if i != first_choice and doors[i] != 'car']
    host_reveal = random.choice(reveal_candidates)
    second_choice = [i for i in range(3) if i != first_choice and i != host_reveal][0]
    return doors[second_choice] == 'car'

def monty_switch_multiple(n):
    wins = sum(monty_switch_single() for _ in range(n))
    winrate = wins / n
    print (f'Winrate = {winrate * 100:.2f}%')
    
monty_switch_multiple(1000000)