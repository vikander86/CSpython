user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}


#create view objects to look at the current state of the dictionary
users = dict.keys(user_ids)
print(users)
#cannot  add or remove elements, but can be used instead of a list for iteration
for user in users:
    print(user)

lessons = dict.keys(num_exercises)
print(lessons)   