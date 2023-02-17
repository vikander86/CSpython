# Import random below:
import random

# Create random_list below:
#adding a random int between 0-100, 100 times.
random_list = [random.randint(0,101) for num in range(0,101)]


#picking a random inte from the random list
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)