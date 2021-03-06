"github.com/lewisgaul/python-tutorial"
# WEEK 2 CHALLENGE - lists, ifs and loops

# Write single-line comments with the '#' symbol.
# This text will not be executed by the interpreter.

# Blank lines can be used wherever you like to make your code easier to read.
# Try not to let your lines of code exceed 80 characters in length.

# Work out how the code below works (use print statements or display variables
# in the shell), add in some comments and make some improvements by using better
# variable names and clearer code where you can.

# Decode the string shuffled_instructions with the code below to find the
# challenge.

# If you complete the task in the hidden message, can you reduce it to 4 lines?
# Finally, use a while loop make a list of the powers of 3 which are less than
# 1000 (the list should start 3, 9, 27,... and all entries should be <1000).
# Introduce a for loop to make a list of lists of the powers of the odd numbers
# less than 10 (the list created above should be one of the entries).


shuffled_instructions = "iarrtbtl oe 4e0cl0b  ulooh 8s0p nu e umeh otoed u0ucaMseo ffp enloaeom    st1 dw iebnma0de wem h lnts lffiic t6lpiatti.uba hnr1  rn e lekesm"
shuffle_order = [97, 61, 138, 81, 108, 136, 68, 111, 92, 75, 131, 64, 84, 63, 53, 58, 17, 43, 34, 11, 123, 66, 16, 115, 91, 59, 33, 42, 119, 51, 110, 127, 26, 27, 18, 30, 6, 87, 65, 24, 23, 96, 19, 22, 121, 3, 102, 120, 106, 52, 101, 99, 5, 0, 9, 38, 80, 45, 122, 20, 116, 14, 118, 98, 67, 12, 1, 39, 94, 105, 49, 41, 113, 104, 73, 88, 50, 89, 48, 37, 25, 109, 137, 86, 47, 28, 129, 44, 90, 126, 82, 55, 103, 135, 60, 125, 79, 71, 40, 10, 128, 132, 7, 76, 13, 57, 8, 114, 74, 95, 78, 100, 70, 117, 46, 36, 124, 69, 139, 134, 29, 15, 85, 56, 133, 62, 83, 21, 4, 31, 93, 77, 112, 54, 107, 35, 2, 72, 32, 130]

# Create a list of the same length as the message. Each element of the list
# will be replaced with a character from the message, so it could be a list of
# anything to begin with.
text_list = len(shuffle_order) * ['_']
# Loop through the indices which correspond to the correct position for each
# character. Use each index to place the i'th character of the message in the
# right place in the list.
i = 0
for index in shuffle_order:
    # print(''.join(text_list)) #Uncomment this for supercool illustration
    text_list[index] = shuffled_instructions[i]
    i += 1
# Note the above can (and should) be done as follows:
# for i, index in enumerate(shuffle_order):
#     text_list[index] = shuffled_instructions[i]
    
# Join up all the characters in the list 'text_list' into a string.
# Type help(str) or help(str.join) in shell to see how this functions works.
instructions = ''.join(text_list)
print("Challenge:", instructions, sep='\n')

# Print all multiples of 6 or 14 between 800 and 1000.
multiples = []
for i in range(800, 1001):
    if i % 6 == 0 or i % 14 == 0:
        multiples.append(i)
print("\nMultiples of 6 or 14 from 800 to 1000:", multiples, sep='\n')

# Create a list which will contain lists of powers.
all_powers = []
for i in range(3, 10, 2):
    n = 1
    powers = []
    while i**n < 1000:
        powers.append(i**n)
        n += 1
    all_powers.append(powers)
print("\nPowers less than 1000 of the odd numbers from 3 to 10:")
# Loop through the lists in all_powers and print them alongside the base.
i = 3 #Initialise counter
for pows in all_powers:
    print(i, "-", pows)
    i += 2



