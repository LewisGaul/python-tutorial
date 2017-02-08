import re #regular expression - for string pattern matching


print("Running 'utils' script...")

def is_email(string):
    # Dot matches any character, the plus matches one or more of the preceeding
    # character ('.+' matches at least one character which can be anything),
    # backslash is the escape character ('\.' matches an actual dot).
    email = re.search('.+@.+\.ox\.ac\.uk', string)
    if email is None:
        return False
    else:
        return True


if __name__ == '__main__':
    # This is a little trick to check if this file is the one which is being
    # run. If the file is imported, the test below won't run.
    email = input("What is your Oxford email?\n")
    print(is_email(email)) #Check if email is of correct form
