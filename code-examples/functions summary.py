# Some of the functions we've seen already:
my_list = list(range(2, 11, 2)) #[2, 4, 6, 8, 10] (list type)
length = len(my_list) #5 (int type)
# The range function returns an iterator, which we can convert to a list using
# the list function.
# The len function returns the length of a list or a string.

# Remember functions are called (told to perform their action) with the round
# brackets. Inside these brackets you can give arguments to the function.

# Functions are defined in the following way:
def sqrt(num):
    return num**0.5 #This is the output of the function
# The function is called sqrt, and is called in the following way:
print("sqrt(2):", sqrt(2)) #prints 1.41....
a = sqrt(4) + sqrt(9) #a = 2 + 3 = 5

# Remember to use the brackets to call the function, even if it doesn't take
# any arguments. For example:
def get1to10():
    return list(range(1, 11))
print("Function reference:", get1to10)
print("get1to10 output:", get1to10()) #Don't forget the brackets

# Functions can have optional arguments by giving default values:
def shorten_list(L, n=1):
    # Shorten list L by removing n elements from the end. By
    # default only one element is removed.
    for i in range(n):
        L.pop()
    # Note we don't need to return anything because we are just changing the
    # list L. (This is a special behaviour with lists).

my_list2 = [3, 5, 22, 5, 0, -1, 2]
shorten_list(my_list2) #Shorten by one
print("After the funtion is called, the list is:", my_list2)
# Shorten it by 3 more elements:
shorten_list(my_list2, 3)
print("Now the list is:", my_list2)
# What do you think shorten_list returns? Notice we haven't used a return
# statement in the function definition.
output = shorten_list([1])
print("shorten_list returns", output)
