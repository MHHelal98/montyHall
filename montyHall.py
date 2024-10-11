import random

def montyStick():
  wins = 0
  for i in range(100000):
    doors = {'door1':'goat','door2':'goat','door3':'goat'}
    doors[random.choice(list(doors.keys()))] = 'car'
    playerChoice = random.choice(list(doors.values()))
    if playerChoice == 'car':
      wins += 1
    else:
      wins += 0
  winrate = wins / 100000
  print(f'Winrate is {winrate*100}%')

def montySwitch():
  wins = 0
  for i in range(100000):
    doors = {'door1':'goat','door2':'goat','door3':'goat'}
    doors[random.choice(list(doors.keys()))] = 'car'
    playerChoice = random.choice(list(doors.values()))
    firstChoice = playerChoice
    if doors['door1'] == 'goat':
      del doors['door1']
    elif doors['door2'] == 'goat':
      del doors['door2']
    else:
      del doors['door3']
    while playerChoice == firstChoice:
      playerChoice = random.choice(list(doors.values()))
    if playerChoice == 'car':
      wins += 1
    else:
      wins += 0
  winrate = wins / 100000
  print(f'Winrate is {winrate*100}%')