# WEEK 1 CHALLENGE

# Notice you can write single-line comments with the '#' symbol.
# This text will not be executed by the interpreter.

# Blank lines can be used wherever you like to make your code easier to read.
# Try not to let your lines of code exceed 80 characters in length.

# Work out how the code works, add in some comments and make some improvements
# by using better variable names and clearer code where you can.

# Can you work out the golden ratio (~1.6) using some of the code we have here?
# Hint: try using ratios (and a google search if you need to!). Can you display
# the answer neatly alongside the amount of error you think there is in your
# calculation?


answer = "???"

var1 = 1
var2 = 1
var3 = var1 + var2
var4 = var2 + var3
var5 = var3 + var4
all_vars = [var1, var2, var3, var4, var5, var4 + var5]
bigger_all_vars = all_vars + [var4 + 2*var5, 2*var4 + 3*var5]

message = "These are " + answer + " numbers:\n"
print(message, bigger_all_vars)
