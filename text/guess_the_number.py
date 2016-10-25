'''guess the number game'''

import random

class Player(object):
    losses=0
    wins=0
    games_played = 0
    def find_average(self):
        a = self.wins / self.losses
        return a


def guessing():
    number = random.randrange(1,11)
    guess = input('guess number 1-10 or \'Q\' to quit \n>>>>:')
    if guess  in ['Q','q','quit']:
        return 'quit'
    else:
        try:
            number_guess=int(guess)
            if number_guess == number:
                return 'win'
            else:
                return 'lose'
        except ValueError:
            print('please enter valid number')
            guessing()

def main():
    player = Player()
    player.wins = 0
    player.losses = 0
    while True:
        guess = guessing()
        if guess =='quit':
            break
        if guess == 'win':
            player.wins +=1
            player.games_played +=1
            print('correct!')
        else:
            player.losses += 1
            player.games_played +=1
            print('incorrect')
    print('wins =',player.wins,'\nlosses=',player.losses,'\naverage={:.2f}%'.format(player.find_average()))

if __name__ == '__main__':
    main()



