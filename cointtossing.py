import random
coin = ['Heads','Tails']
toss = random.choice(coin)
while True:
    spin = input('Heads or Tails:')
    if spin == toss:
        print("you win! The coin based on " + toss)
    else:
        print('you lose! the coin landed on ' + toss)


