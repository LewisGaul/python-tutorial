"github.com/lewisgaul/python-tutorial"
# WEEK 3 CHALLENGE - functions

# Work out how the code below works (use print statements or display variables
# in the shell), add in some comments and make some improvements by using better
# variable names and clearer code where you can.

# When you understand the code below you can choose either of the following
# challenges to start with (the first is easier):

# 1) Write a function which takes in two string arguments - the first is some
# text and the second is a short string (e.g. a character or a word). It should
# return the number of times the short string appears in the text (type
# help(str) in the shell to find the string method you will need). If the short
# string does not appear in the text a warning should be printed before it
# returns 0.
# You could then extend the function to take an optional third argument which
# should be another short string, and the function should then return the total
# number of times both short strings appear in the text.

# 2) Write a function which takes one integer argument, n. It should return the
# first n prime numbers.
# This could be altered to also accept a list of integers as its one argument
# (without changing the behaviour if an integer is given), and if a list is
# given it should return a list of the i'th primes, where the list contains
# the indices. e.g. get_primes([1, 3, 5]) -> [2, 5, 11]. Hint: use a
# condition like 'if type(arg) is int: ...'.


def transform_list(input_list, pow=1.5):
    # Map every element of input_list by raising it to the power pow which
    # defaults to 1.5.
    return [round(i**pow, 2) for i in input_list]

# Create a list of transformed lists using the function above with powers
# -3, -1, 1, 3 for the list [1, 2, 3, 4].
transformed_lists = []
for i in range(-3, 4, 2):
    transformed_lists.append(transform_list(range(1, 5), pow=i))
# Flatten the list of lists, putting all the elements into one list.
print([i for l in transformed_lists for i in l])

# Challenge 1:
def count_pattern(text, pattern1, pattern2=None):
    num1 = text.count(pattern1)
    if num1 == 0:
        print("Warning: pattern", pattern1, "not found in the text")
    if pattern2 is not None:
        num2 = text.count(pattern2)
    else:
        num2 = 0
    total = num1 + num2
    return total
    
text = "You can use this text to check your function works."
print("There are", count_pattern(text, 'e'), "'e's in the text.")
print("There are", count_pattern(text, 'a', 'e'), "'a's and 'e's in the text")
    

# Challenge 2:
def get_primes(arg):
    if type(arg) is int:
        n = arg
    else:
        n = max(arg)
    primes = [2] #Include the only even number
    num = 3 #Only consider odd numbers
    while len(primes) < n:
        for p in primes:
            if p > num**0.5:
                primes.append(num)
                break
            elif num % p == 0:
                break #Don't include in primes because it has a divisor
        num += 2
    if type(arg) is int:
        return primes
    else:
        return [primes[i-1] for i in arg] 

print("First 10 primes are:", get_primes(10))
print("Every other prime:", get_primes(range(1, 10, 2)))





