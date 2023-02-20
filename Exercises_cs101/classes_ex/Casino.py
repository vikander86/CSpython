import random
cards = {
    '2 of Clubs': (2, 'Clubs'),
    '3 of Clubs': (3, 'Clubs'),
    '4 of Clubs': (4, 'Clubs'),
    '5 of Clubs': (5, 'Clubs'),
    '6 of Clubs': (6, 'Clubs'),
    '7 of Clubs': (7, 'Clubs'),
    '8 of Clubs': (8, 'Clubs'),
    '9 of Clubs': (9, 'Clubs'),
    '10 of Clubs': (10, 'Clubs'),
    'Jack of Clubs': (11, 'Clubs'),
    'Queen of Clubs': (12, 'Clubs'),
    'King of Clubs': (13, 'Clubs'),
    'Ace of Clubs': (14, 'Clubs'),
    '2 of Diamonds': (2, 'Diamonds'),
    '3 of Diamonds': (3, 'Diamonds'),
    '4 of Diamonds': (4, 'Diamonds'),
    '5 of Diamonds': (5, 'Diamonds'),
    '6 of Diamonds': (6, 'Diamonds'),
    '7 of Diamonds': (7, 'Diamonds'),
    '8 of Diamonds': (8, 'Diamonds'),
    '9 of Diamonds': (9, 'Diamonds'),
    '10 of Diamonds': (10, 'Diamonds'),
    'Jack of Diamonds': (11, 'Diamonds'),
    'Queen of Diamonds': (12, 'Diamonds'),
    'King of Diamonds': (13, 'Diamonds'),
    'Ace of Diamonds': (14, 'Diamonds'),
    '2 of Hearts': (2, 'Hearts'),
    '3 of Hearts': (3, 'Hearts'),
    '4 of Hearts': (4, 'Hearts'),
    '5 of Hearts': (5, 'Hearts'),
    '6 of Hearts': (6, 'Hearts'),
    '7 of Hearts': (7, 'Hearts'),
    '8 of Hearts': (8, 'Hearts'),
    '9 of Hearts': (9, 'Hearts'),
    '10 of Hearts': (10, 'Hearts'),
    'Jack of Hearts': (11, 'Hearts'),
    'Queen of Hearts': (12, 'Hearts'),
    'King of Hearts': (13, 'Hearts'),
    'Ace of Hearts': (14, 'Hearts'),
    '2 of Spades': (2, 'Spades'),
    '3 of Spades': (3, 'Spades'),
    '4 of Spades': (4, 'Spades'),
    '5 of Spades': (5, 'Spades'),
    '6 of Spades': (6, 'Spades'),
    '7 of Spades': (7, 'Spades'),
    '8 of Spades': (8, 'Spades'),
    '9 of Spades': (9, 'Spades'),
    '10 of Spades': (10, 'Spades'),
    'Jack of Spades': (11, 'Spades'),
    'Queen of Spades': (12, 'Spades'),
    'King of Spades': (13, 'Spades'),
    'Ace of Spades': (14, 'Spades')
}

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
snake_bet = [1,5,9, 12, 14, 16, 19, 23, 27, 30, 32, 34]

balance = 5000
class Roulette:
    
    def roulette_table(balance):
        
        game_init = """
        Hi! Welcome to the roulette table.
        
        Shall we play?        
        """
        print(game_init)
        option = 1
        while(option != 0):
            random_number = random.randint(1,37)
            if balance <= 0:
                print("You better go home now.")
                break
            make_bet = int(input("Make your bet: "))
            while(make_bet > balance):
                print("Bet is too high, current balance is {}$".format(balance))
                make_bet = int(input("Make your bet: "))
                
            print("Choose how you want to bet")
            print("1. Bet on color\n2: Bet on even or odd\n3: Dozen bet 1-12\n4: Dozen bet 13-24\n5: Dozen bet 25-36\n6: Snake bet\n7: Low(1-18)\n8: High(19-36)\n9: One number\n")
            option = int(input("Enter option: "))
            if option == 1:
                choice = input("Pick a color(red or black): ")
                if choice == "red":
                    if red.count(random_number) == 1:
                        print("It landed on {}. You win!!!".format(random_number))
                        balance += make_bet
                    else:
                        print("It landed on {}. Better luck next time".format(random_number))
                        balance -= make_bet
                elif choice == "black":
                    if black.count(random_number) == 1:
                        print("It landed on {}. You win!!!".format(random_number))
                        balance += make_bet
                    else:
                        print("It landed on {}. Better luck next time".format(random_number))
                        balance -= make_bet
                else:
                    print("wrong input")
            print("Your balance is {}$".format(balance))
                         
        
        

class BlackJack:
    pass

Roulette.roulette_table(5000)
