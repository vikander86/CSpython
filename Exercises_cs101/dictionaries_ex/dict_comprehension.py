songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#dictionary comprehension, pair songs(key) with playcounts(value)
plays = {key:value for key, value in zip(songs,playcounts)}
print(plays)

#adding new entry to plays dict.
plays["Purple Haze"]=1

#updating current key with new value
plays["Respect"]=94

#creating new dictionary with value of a dictionary.
library = {"The Best Songs": plays,"Sunday Feelings": {}}
print(library)
