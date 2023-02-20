import random
from dicts_game import questions_C,answers_C,money_value,small_talk,choices_C

class Player:
    lifelines = {0: ["50/50", True],1: ["Hint",True], 2: ["New try", True]}
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        description = """
        Hi {}!
        Welcome to another round of WHO WANTS TO BE A MILLIONARIE

        You get 15 questions on your road to 1,000,000$
        Along the way you can use the following lifelines
            
            50/50 (remove two incorrect answers)
            Hint (get a hint)
            Extra life (if you fail a question, you can use your extra life to try again)
        
        There are several checkpoints on the way, and you can stop whenever you want.
        You would then win the amount of the previous checkpoint.

        Good LUCK!

        Now lets play
        WHO WANTS TO BE A MILLIONARIE?
        """.format(self.name)
        return description

class Game:
    index = 0
    game_on = True
    game_start = 0
    checkpoint = 0
    def __init__(self):
        self.questions = questions_C
        self.answers = answers_C

    def next_question(self):  
        print("""
    Here's the question for {}$\n
    {}
        """.format(money_value[Game.index],questions_C.pop(money_value[Game.index])))
        Game.game_start = 1
    
    def choices(self):
        print(choices_C[Game.index])    

    def player_answer(self,answer):
        if answer in answers_C[Game.index]:
            print("Correct!!")
            if money_value[Game.index] == 1000 or money_value[Game.index] == 32000 or money_value[Game.index] == 1000000:
                Game.checkpoint = money_value[Game.index]
            if Game.index > 0:
                random_num = random.randint(0,9)
                print(small_talk[random_num])
        else:
            print("uff, tough shit bro! You loose")
            Game.game_on = False
        Game.index += 1
        

name = input("Name: ")
player_one = Player(name)
print(player_one)
new_game = Game()
while(Game.game_on == True):
    if Game.game_start == 0:
        choice_start_game = input("Are you ready to play??(press Enter)")
    
    if Game.game_start != 0:
            continue_game = input("Do you want to continue?(y/n): ")
            Game.game_start = 1
            if continue_game == 'n':
                Game.game_on == False
                break   
    new_game.next_question()
    new_game.choices()
    answer = input("What is your answer?: ")
    while answer not in answers_C.values():
         answer = input("Wrong input! (a,b,c,d): ")
    new_game.player_answer(answer)
input("""
      You won {}$
      Thanks alot for playing
      (press Enter to exit)
      """.format(Game.checkpoint))

    
#add checkpoints
#add lifelines
  