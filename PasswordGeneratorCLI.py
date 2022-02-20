import random

# Ask user if he wants the default password characters
print("Do you want to use the default password characters? y/n")
# Let him choose
choice = input()
# If choice is n
if choice == "n":
    # Ask him if he wants to use specific words
    print("Do you want to use specific words or do you want to use random letters? ")
    # User choices
    print("1. Words")
    print("2. Random Letters")
    choicePasswordType = input()
    if choicePasswordType == "1" or choicePasswordType == "Words" or choicePasswordType == "words":
        print("Enter the words you want to use, followed by a comma. Do not insert any spaces! ")
        # User enters his words, followed by a comma
        passwordWords = input()
        # Swap name, so the the program can run
        passwordCharacters = passwordWords
        # Split the words after comma
        passwordCharactersArray = passwordCharacters.split(",")
        # Boolean if password is custom
        custom = True
        # Print the array
        # print(passwordCharactersArray)

        # If choice is 2
    elif choicePasswordType == "2":
        # Ask user to write the desired characters
        print("Type the characters you want to use")
        passwordCharacters = input()
        # Split every letter from string in array
        passwordCharactersArray = list(passwordCharacters)

# If user want to use the default password characters
elif choice == "y" or choice == "":
    passwordCharacters = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890$+!?"
    # Split every letter from string in array
    passwordCharactersArray = list(passwordCharacters)
    custom = False
    # Print the array
    # print(passwordCharactersArray)

# Ask for password size in letters
print("Size? ")
size = input()

# If boolean custom is true
if custom:
    # sizeOfPasswordCharacters counts how many elements are in passwordCharactersArray and takes its value
    sizeOfPasswordCharacters = len(passwordCharactersArray)
else:
    # sizeOfPasswordCharacters counts how many elements are in passwordCharacters and takes its value
    sizeOfPasswordCharacters = len(passwordCharacters)

# Temporary value to work with while
x = 1
# Set the password as being empty
password = ""

# While x is smaller than the size the user wants
while x <= int(size):
    # Gets a number between 0 and all desired password characters
    r = random.randint(0, int(sizeOfPasswordCharacters) - 1)
    # With help of r, rValue takes a value from passwordCharactersArray
    rValue = passwordCharactersArray[r]
    # Updates the password with the new data
    password = str(password) + str(rValue)
    # x grows with 1, to finnish the while loop
    x = x + 1

    # When x is greater than the desired size the program shows the password
    if x > int(size):
        print(password)
