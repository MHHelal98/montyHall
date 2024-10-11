import random

def simulate_game(stick=True):
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    first_choice = random.randint(0, 2)
    remaining_doors = [i for i in range(3) if i != first_choice and doors[i] == 'goat']
    host_reveal = random.choice(remaining_doors)

    if stick:
        final_choice = first_choice
    else:
        final_choice = [i for i in range(3) if i != first_choice and i != host_reveal][0]

    return doors[final_choice] == 'car'

def monty_hall_simulation(num_simulations=100000, stick=True):
    wins = sum(simulate_game(stick) for _ in range(num_simulations))
    win_rate = wins / num_simulations
    strategy = "stick" if stick else "switch"
    print(f'Win rate when you {strategy}: {win_rate * 100:.2f}%')

monty_hall_simulation(stick=True)
monty_hall_simulation(stick=False)