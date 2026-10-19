from os import system

def getValidInt(prompt:str, min=0, max=100) -> int:
    """
    Repeat until a valid integer within the inclusive range is entered; return the integer. 
    """
    playerinput = input(prompt)
    


def getValidResponse(prompt, validResponses:str) -> str:
    """
    Repeat until an accepted response is entered.
    Ignore case and surrounding spaces; use a list comprehension to lowercase valid responses.
    Return lowercase input.
    """
    prompt = input(prompt)
    while prompt.isdigit() != False:
        print("Invalid response, must be letter.")
        prompt = input("Enter a response: ")
    prompt = prompt.lower().strip()

def getNonEmptyString(prompt) -> str:
    """
    Reject empty or whitespace-only input; return the trimmed string.
    """

def clearScreen():
    """
    Clear the Windows console.
    """
    system("cls")

def pause(message="Press Enter to continue..."):
    """
    Show the message and wait for Enter.
    """

def printNumberedList(items):
    """
    Print items numbered from 1; for an empty list print “No items to display.”
    """

def filterByLength(items, minLength:int, maxLength:int):
    """
    Use a list comprehension to return strings with lengths in the inclusive range, preserving order.
    """

def analyzeNumbers(numbers:int):
    """
    Use a list comprehension to collect positive numbers.
    Return four values: positive-number list, positive count, negative count, zero count.
    """

if __name__ == "__main__":
    # Test each utility fuction here.
    promptltr = "Enter a letter: "
    promptnum = "Enter a number: "
    while True:
        test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8) Break(B/b): ")
        if test == 1:
            getValidInt(promptnum)
        elif test == 2:
            getValidResponse(promptltr)
        elif test == 3:
            getNonEmptyString()
        elif test == 4:
            clearScreen()
        elif test == 5:
            pause()
        elif test == 6:
            printNumberedList()
        elif test == 7:
            filterByLength()
        elif test == 8:
            analyzeNumbers()
        elif test == "B" or test == "b":
            break
        else:
            while test.isdigit() == False:
                print("Invalid input.")
                test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8): ")
            test = int(test)
            while test <= 1:
                print("Invalid function number, too low.")
                test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8): ")
            while test >= 8:
                print("Invalid function, too high.")
                test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8): ")
