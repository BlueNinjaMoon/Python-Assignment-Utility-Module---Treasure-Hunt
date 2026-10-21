
def getValidInt(prompt:str, min=0, max=100) -> int:
    """
    Repeat until a valid integer within the inclusive range is entered; return the integer. 
    """
    playerinput = input(prompt) 
    while not playerinput.isdigit() or int(playerinput) < min or int(playerinput)> max:
        print("Invalid")
        playerinput = input(prompt) 

    #     getValidResponse()
    # if not playerinput >= 0:
    #     print("Invalid input, too low.")
    # else:
    #     if not playerinput <= 100:
    #         print("Invalid input, too high.")
    #         playerinput
    return int(playerinput)

def getValidResponse(prompt:str, validResponses) -> any:
    """
    Repeat until an accepted response is entered.
    Ignore case and surrounding spaces; use a list comprehension to lowercase valid responses.
    Return lowercase input.
    """
    user = input(prompt).strip().lower()
    validResponses = [resp.lower().strip() for resp in validResponses]
    while user not in validResponses:
        print("Invalid entry. ")
        user = input(prompt).strip().lower()

    return user

    # if validResponses.isdigit == False:
    #     print("Input must be letter.")
    #     while user.isdigit() != False:
    #         print("Invalid response, must be letter.")
    #         user = input("Enter a response: ")
    #     prompt = prompt.lower().strip()
    # if validResponses.isdigit == False:
    #     print("Input must be number.")
    #     while user.isdigit() != True:
    #         print("Invalid response, must be a number.")
    #         user = input("Enter a response: ")
    #     user = int(user)

def getNonEmptyString(prompt) -> str:
    """
    Reject empty or whitespace-only input; return the trimmed string.
    """
    playerinput = input(prompt).strip()
    while playerinput == "":
        print("Invalid response.")
        playerinput = input(prompt).strip()
    return playerinput

def clearScreen():
    """
    Clear the Windows console.
    """
    from os import system
    system("cls")

def pause(message="Press Enter to continue..."):
    """
    Show the message and wait for Enter.
    """
    playerinput = input(message)
    while playerinput != "":
        print("Invalid response, must be enter (eg. ''): ")
        playerinput = input("")

def printNumberedList(items):
    """
    Print items numbered from 1; for an empty list print “No items to display.”
    """
    index = -1
    inlist = 0
    for i in items:
        index += 1
        inlist +=1
    if index == -1:
        print("No items to display.")
    else:
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")

def filterByLength(items, minLength:int, maxLength:int):
    """
    Use a list comprehension to return strings with lengths in the inclusive range, preserving order.
    """
    return {item for item in items if minLength <= len(item) <= maxLength}

def analyzeNumbers(numbers:int):
    """
    Use a list comprehension to collect positive numbers.
    Return four values: positive-number list, positive count, negative count, zero count.
    """
    positiveNumbers = [number for number in numbers if number > 0]
    positiveCount = len(positiveNumbers)
    negativeCount = len([number for number in numbers if number < 0])
    zeroCount = len([number for number in numbers if number == 0])

    return positiveNumbers, positiveCount, negativeCount, zeroCount

if __name__ == "__main__":
    # Test each utility fuction here.
    userin = getValidInt("Enter a number between 10 and 20: ", 10, 20)
    userin = getValidResponse("Enter a Y or N: ", ["y", "N"])
    userin = getNonEmptyString("Enter a string: ")
    userin = clearScreen()
    print("Screen Clear (Only prints this in __main__)")
    userin = pause("Press enter to continue.")
    userin = printNumberedList(["", "a", "2"])
    print(filterByLength(["623","21","8234","1","5","10","9"], 1, 10))
    print(analyzeNumbers([1, 2, 3, -5, -10, 0, 11]))
    



"""
    from random import choice
    promptltr = "Enter a letter: "
    promptnum = "Enter a number: "
    numOrltr = ["A", 1]
    rand = choice(numOrltr)
    while True:
        test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8) Break(B/b): ")
        if test == 1:
            getValidInt(promptnum, 0, 100)
        elif test == 2:
            getValidResponse(promptltr, rand)
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
            while test < 1 or test > 8:
                if test < 1:
                    print("Invalid function number, too low.")
                elif test > 8:
                    print("Invalid function, too high.")
                else:
                    print("Invalid response.")
                    getValidResponse("Enter a valid function number. (1-8): ", 1)
                test = input("getValidInt(1) getValidResponse(2) getNonEmptyString(3) clearScreen(4) pause(5) printNumberedList(6) filterByLength(7) analyzeNumbers(8): ")
                test = int(test)
"""
