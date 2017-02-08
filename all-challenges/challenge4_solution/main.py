"github.com/lewisgaul/python-tutorial"
# WEEK 4 CHALLENGE - functions and imports

# Work out how the code works (use print statements, try running functions
# in the shell), add in some comments to help yourself understand. You will
# need to open 'utils.py' which is used in this code.

# Use the list of questions defined below to make a timed quiz, giving the
# user their score at the end.

# If you have time, try making a simple noughts and crosses game in a separate
# file.


import time
import random as rnd #Use the random module with the alias 'rnd'

from utils import is_email


# '\n' is the newline character.
email = input("What is your Oxford email address?\n")
while not is_email(email):
    print("Invalid email.")
    email = input("Please enter your Oxford email ([name]@[college].ox.ax.uk)\n")



questions = [
    "How old is the Queen of England?",
    "What is the best programming language?",
    "What letter is commonly considered the equivalent of 'a' in the Greek alphabet?",
    "If it walks like a duck and quacks like a duck, it must be a ______?",
    "Which college is closest to Teddy Hall?"
    ]
options = [
    ["75", "80", "85", "90"],
    ["C", "Java", "Python", "Javascript"],
    ["alpha", "omega", "phi", "pi"],
    ["object", "action", "duck", "animal"],
    ["Oriel", "New", "Queens", "Univ"]
    ]
answers = ['d', 'c', 'a', 'c', 'b']

nr_questions = len(questions)
print("\nThis quiz has", nr_questions, "questions.",
      "You have 5 seconds to answer each question (a, b, c, or d).")
score = 0
order = list(range(nr_questions)) #[0, 1, 2, 3, 4]
rnd.shuffle(order) #shuffle the order
# In the loop below, i takes values 0,1,2,3,4 in shuffled order, and q_num
# takes the same values but in order (see 'help(enumerate)').
for q_num, i in enumerate(order):
    print("\nQ", q_num+1, ": ", questions[i], sep='')
    for j, letter in enumerate(['a', 'b', 'c', 'd']):
        print(letter, ") ", options[i][j], sep='')
    start_time = time.time()
    choice = input() #Get their answer
    elapsed = time.time() - start_time
    if elapsed > 5:
        print("You took longer than 5 seconds!")
    elif choice == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Nope!")
# (See 'help(str.format)').
print("You scored {}/{}.".format(score, nr_questions))
        
    



    
    
