from tkinter import *
import random

# The main window is called window
window = Tk()
# Set the title
window.title("Password Generator")
# Set the window size
window.geometry("550x200")
# Set the background black
window.configure(bg="black")
# Make the window unsizable
window.resizable(False, False)

# The main title
label = Label(window, text="Password Generator", font=(None, 15), height=2, fg="white", bg="black")
# Align the text to the top of page
label.pack(side=TOP)
# frame for items (without title)
gridFrame = Frame(window, bg="black")
# Setting the frame anchor to the top
gridFrame.pack(side=TOP)


def defaultCharacterPasswordPage(defaultCharactersButton, customPasswordButton):
    defaultCharactersButton.destroy()
    customPasswordButton.destroy()

    sizeLabel = Label(gridFrame, text="How many characters should your password contain? ", fg="white", bg="black")
    sizeLabel.grid(column=0, row=0)

    sizeInput = Entry(gridFrame, width=10, bg="black", fg="white", highlightthickness=1, highlightbackground="white")
    sizeInput.grid(column=1, row=0)

    submitButton = Button(gridFrame, text="Submit", command=lambda: defaultCharacterPassword(int(sizeInput.get()), submitButton, sizeLabel, sizeInput))
    submitButton.grid(column=0, row=1, pady=5)


def defaultCharacterPassword(passwordSize, submitButton, sizeLabel, sizeInput):
    sizeLabel.destroy()
    sizeInput.destroy()
    submitButton.destroy()
    passwordCharacters = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890$+!?"
    # Split every letter from string in array
    passwordCharactersArray = list(passwordCharacters)

    passwordCharactersLabel = Label(gridFrame, text="Your password contains " + str(passwordSize) + " characters!", bg="black", fg="white")
    passwordCharactersLabel.grid(column=0, row=0)

    # Temporary value to work with while
    x = 1
    # Set the password as being empty
    password = ""

    # While x is smaller than the size the user wants
    while x <= int(passwordSize):
        # Gets a number between 0 and all desired password characters
        r = random.randint(0, len(passwordCharacters) - 1)
        # With help of r, rValue takes a value from passwordCharactersArray
        rValue = passwordCharactersArray[r]
        # Updates the password with the new data
        password = str(password) + str(rValue)
        # x grows with 1, to finnish the while loop
        x = x + 1

        # When x is greater than the desired size the program shows the password
        if x > int(passwordSize):

            passwordIsLabel = Label(gridFrame, text="The generated password:", bg="black", fg="white")
            passwordIsLabel.grid(column=0, row=1)

            passwordLabel = Label(gridFrame, text=password, font=(None, 10), height=2)
            passwordLabel.grid(column=0, row=2)

            passwordCopiedLabel = Label(gridFrame, text="Now just paste the password where you need. That simple it is.", bg="black", fg="white")
            passwordCopiedLabel.grid(column=0, row=3, pady=5)

            passwordLabel.clipboard_append(password)
            passwordLabel.update()


def customPasswordPage(defaultCharactersButton, customPasswordButton):
    defaultCharactersButton.destroy()
    customPasswordButton.destroy()

    typeOfPasswordLabel = Label(gridFrame, text="What kind of password do you want to create?", bg="black", fg="white")
    typeOfPasswordLabel.grid(column=0, row=0)

    secondGrid = Frame(gridFrame)
    secondGrid.configure(bg="black")
    secondGrid.grid(column=0, row=1)

    charactersBasedPasswordButton = Button(secondGrid, text="Custom Characters", command=lambda: customCharacterPasswordPage(typeOfPasswordLabel, secondGrid))
    charactersBasedPasswordButton.grid(column=0, row=0, padx=2, pady=2)

    wordBasedPasswordButton = Button(secondGrid, text="Word Based", command=lambda: wordBasedPasswordPage(typeOfPasswordLabel, secondGrid))
    wordBasedPasswordButton.grid(column=1, row=0, padx=2, pady=2)


def customCharacterPassword(charactersLabel, secondGrid, thirdGrid, customCharacters, size):
    charactersLabel.destroy()
    secondGrid.destroy()
    thirdGrid.destroy()

    customCharactersArray = list(customCharacters)
    # Temporary value to work with while
    x = 1
    # Set the password as being empty
    password = ""

    # While x is smaller than the size the user wants
    while x <= int(size):
        # Gets a number between 0 and all desired password characters
        r = random.randint(0, int(len(customCharactersArray)) - 1)
        # With help of r, rValue takes a value from passwordCharactersArray
        rValue = customCharactersArray[r]
        # Updates the password with the new data
        password = str(password) + str(rValue)
        # x grows with 1, to finnish the while loop
        x = x + 1

        # When x is greater than the desired size the program shows the password
        if x > int(size):
            passwordSizeLabel = Label(gridFrame, text="Your password contains " + str(size) + " characters!", bg="black", fg="white")
            passwordSizeLabel.grid(column=0, row=0)

            passwordIsLabel = Label(gridFrame, text="The generated password:", bg="black", fg="white")
            passwordIsLabel.grid(column=0, row=1)

            passwordLabel = Label(gridFrame, text=password, font=(None, 10), height=2)
            passwordLabel.grid(column=0, row=2)

            passwordCopiedLabel = Label(gridFrame, text="Now just paste the password where you need. That simple it is.", bg="black", fg="white")
            passwordCopiedLabel.grid(column=0, row=3, pady=5)

            passwordLabel.clipboard_append(password)
            passwordLabel.update()


def customCharacterPasswordPage(typeOfPasswordLabel, secondGrid):
    secondGrid.destroy()
    typeOfPasswordLabel.destroy()

    charactersLabel = Label(gridFrame, text="Enter the characters you want to use. Don't use any spaces", bg="black", fg="white")
    charactersLabel.grid(column=0, row=0)

    secondGrid = Frame(gridFrame)
    secondGrid.configure(bg="black")
    secondGrid.grid(column=0, row=1)

    customCharactersInput = Text(secondGrid, bg="black", fg="white", highlightthickness=1, highlightbackground="white", width=60, height=2)
    customCharactersInput.grid(column=0, row=0, pady=10)

    thirdGrid = Frame(secondGrid)
    thirdGrid.configure(bg="black")
    thirdGrid.grid(column=0, row=1)

    sizeLabel = Label(thirdGrid, text="How many characters should your password contain? ", bg="black", fg="white")
    sizeLabel.grid(column=0, row=0)

    sizeInput = Entry(thirdGrid, bg="black", fg="white", highlightthickness=1, highlightbackground="white", width=10)
    sizeInput.grid(column=1, row=0)

    submitButton = Button(secondGrid, text="Submit", command=lambda: customCharacterPassword(charactersLabel, secondGrid, thirdGrid, customCharactersInput.get("1.0", "end").replace("\n", ""), int(sizeInput.get())))
    submitButton.grid(column=0, row=2, pady=5)


def wordBasedPassword(wordsLabel, secondGrid, thirdGrid, customWords, size):
    wordsLabel.destroy()
    secondGrid.destroy()
    thirdGrid.destroy()

    customWordsArray = customWords.split(",")

    # Temporary value to work with while
    x = 1
    # Set the password as being empty
    password = ""

    # While x is smaller than the size the user wants
    while x <= int(size):
        # Gets a number between 0 and all desired password characters
        r = random.randint(0, int(len(customWordsArray)) - 1)
        # With help of r, rValue takes a value from passwordCharactersArray
        rValue = customWordsArray[r]
        # Updates the password with the new data
        password = str(password) + str(rValue)
        # x grows with 1, to finnish the while loop
        x = x + 1

        # When x is greater than the desired size the program shows the password
        if x > int(size):

            passwordSizeLabel = Label(gridFrame, text="Your password contains " + str(len(password)) + " characters!", bg="black", fg="white")
            passwordSizeLabel.grid(column=0, row=0)

            passwordIsLabel = Label(gridFrame, text="The generated password:", bg="black", fg="white")
            passwordIsLabel.grid(column=0, row=1)

            passwordLabel = Label(gridFrame, text=password, font=(None, 10), height=2)
            passwordLabel.grid(column=0, row=2)

            passwordCopiedLabel = Label(gridFrame, text="Now just paste the password where you need. That simple it is.", bg="black", fg="white")
            passwordCopiedLabel.grid(column=0, row=3, pady=5)

            passwordLabel.clipboard_append(password)
            passwordLabel.update()


def wordBasedPasswordPage(typeOfPasswordLabel, secondGrid):
    secondGrid.destroy()
    typeOfPasswordLabel.destroy()

    wordsLabel = Label(gridFrame, text="Enter the words you want to use followed by a comma. Don't use any spaces", bg="black", fg="white")
    wordsLabel.grid(column=0, row=0)

    secondGrid = Frame(gridFrame)
    secondGrid.configure(bg="black")
    secondGrid.grid(column=0, row=1)

    customWordsInput = Text(secondGrid, bg="black", fg="white", highlightthickness=1, highlightbackground="white", width=60, height=2)
    customWordsInput.grid(column=0, row=0, pady=10)

    thirdGrid = Frame(secondGrid)
    thirdGrid.configure(bg="black")
    thirdGrid.grid(column=0, row=1)

    sizeLabel = Label(thirdGrid, text="How many words should your password contain? ", bg="black", fg="white")
    sizeLabel.grid(column=0, row=0)

    sizeInput = Entry(thirdGrid, bg="black", fg="white", highlightthickness=1, highlightbackground="white", width=10)
    sizeInput.grid(column=1, row=0)

    submitButton = Button(secondGrid, text="Submit", command=lambda: wordBasedPassword(wordsLabel, secondGrid, thirdGrid, customWordsInput.get("1.0", "end").replace("\n", ""), int(sizeInput.get())))
    submitButton.grid(column=0, row=2, pady=5)


def main():
    defaultCharactersButton = Button(gridFrame, text="Default Characters", command=lambda: defaultCharacterPasswordPage(defaultCharactersButton, customPasswordButton))
    defaultCharactersButton.grid(column=0, row=0, padx=2)

    customPasswordButton = Button(gridFrame, text="Custom Characters", command=lambda: customPasswordPage(defaultCharactersButton, customPasswordButton))
    customPasswordButton.grid(column=1, row=0, padx=2)

    window.mainloop()


main()
