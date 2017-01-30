"github.com/lewisgaul/python-tutorial"
# WEEK 3 CHALLENGE - functions

# Work out how the code below works (use print statements or display variables
# in the shell), add in some comments and make some improvements by using better
# variable names and clearer code where you can.

# When you understand the code below you can choose either of the following
# challenges:

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


# Can you rewrite this function in 2 lines instead of 6?
def transform_list(input_list, pow=1.5):
    # Write here an explanation of what the function does.
    output_list = []
    for i in input_list:
        output_list.append(round(i**pow, 2))
    return output_list

# What is this loop doing?
transformed_lists = []
for i in range(-3, 4, 2):
    transformed_lists.append(transform_list(range(1, 5), pow=i))
# If you're not sure how this works consider printing transformed_lists.
print([i for l in transformed_lists for i in l])
    




