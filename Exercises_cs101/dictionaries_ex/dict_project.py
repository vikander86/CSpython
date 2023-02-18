letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combine letters and points to a dictionary with dict comprehension
letter_to_points = {key:value for key, value in zip(letters,points)}

#add to dict
letter_to_points[" "] = 0
print(letter_to_points)

#define function that scores the word based on letters
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

brownie_points = score_word("brownie")
print(brownie_points)
print(score_word("Hey"))


#create player/words dict
player_to_word = {"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

#init empty dict
player_to_points = {}

#iterate through player_to_word, incrementing the player_points by calling the score_word function with the word theyve chosen.
#finalize by adding player key with player_points value.
for player,words in player_to_word.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player]=player_points

#finding max and addressing the winner.
maximum = max(player_to_points.values())
for player, points in player_to_points.items():
    if points == maximum:
        print("The winner is {} with {} points!".format(player, points))
