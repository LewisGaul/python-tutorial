"github.com/lewisgaul/python-tutorial"
# WEEK 1 CHALLENGE SOLUTION

# Notice you can write single-line comments with the '#' symbol.
# This text will not be executed by the interpreter.

# Blank lines can be used wherever you like to make your code easier to read.
# Try not to let your lines of code exceed 80 characters in length.

# Work out how the code works, add in some comments and make some improvements
# by using better fiable names and clearer code where you can.

# Can you work out the golden ratio (~1.6) using some of the code we have here?
# Hint: try using ratios (and a google search if you need to!). Can you display
# the answer neatly alongside an upper bound for the percentage error in your
# calculation?


answer = "fibonacci"

# Calculate the first 7 fibonacci numbers.
f1, f2 = 1, 1 #Same thing as f1 = 1; f2 = 1
f3 = f1 + f2
f4 = f2 + f3
f5 = f3 + f4
f6 = f4 + f5
f7 = f5 + f6
fibs = [f1, f2, f3, f4, f5, f6, f7] #Create list of all the above

message = "This is a sequence of numbers called " + answer + " numbers:\n"
print(message, fibs) #(Remove the brackets if using Python version 2)

# Use ratio of fibonacci numbers to approximate the golden ratio.
g1 = f2 / f1 #(Use float(f2) if using Python version 2 to convert to decimal)
g2 = f3 / f2
g3 = f4 / f3
g4 = f5 / f4
g5 = f6 / f5
g6 = f7 / f6
print("Golden ratio approximation sequence is:\n", [g1, g2, g3, g4, g5, g6])

# We notice the ratios are converging in an oscillatory fashion towards ~1.6,
# so the error of the nth estimate is bounded by the difference between this
# estimate and the previous.
max_err = g6 - g5
# To calculate the maximum percentage error we should divide by the actual value
# for the golden ratio. However we assume this is unknown, and get the upper
# bound by dividing by the best estimate which we know to be below the actual
# value (using the oscillation property). g5 < g6 so use g5.
max_perc_err = 100 * max_err / g5
print("Golden ratio is approximately", g6)
print("Error is no more than", max_perc_err, "%.")
