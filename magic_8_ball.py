import random
# name, question, answer
name = input("What is your name? ")
question = input("What is your question? ")
answer = ""

# implement random number selection
random_number = random.randint(1,5)

# determine the Magic 8-Ball's answer based on the random number
if random_number == 1:
  answer = "Of course, don't think twice!"
elif random_number == 2:
  answer = "I have to say yes..."
elif random_number == 3:
  answer = "Truthfully, maybe yes, maybe no."
elif random_number == 4:
  answer = "Sadly, no."
elif random_number == 5:
  answer = "No no no!"
else:
  answer = "Error: Unexpected random number"

# no name is provided - conditonal
if name != "":
  print(name + " asks:", end=" ")
else:
  print("Question:", end=" ")
  
# if no question is provided - conditional
if question != "":
  print(question)
  print("Magic 8 ball's answer: " + answer)
else:
  print("\nMagic 8 ball cannot provide an answer without a question.")
