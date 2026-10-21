from random import choice
import utilities

currentrnd = 1
maxrnd = 5
roundplayed = 0
rndpoints = []
total = 0

utilities.clearScreen()
print("========== TREASURE HUNT ==========")
username = utilities.getNonEmptyString("Enter your name: ")
print(f"Welcome, {username}!")
utilities.pause("Press Enter to start the game...")
print("========== DIFFICULTY SELECT ==========")
utilities.printNumberedList(["Easy","Medium","Hard"])
difficulty = utilities.getValidInt("Pick a difficulty (1-3): ",1,3)

if difficulty == 1:
    treasure = 10
    trap = 5
elif difficulty == 2:
    treasure = 20
    trap = 10
elif difficulty == 3:
    treasure = 30
    trap = 20

empty = 0

score = 0
while roundplayed != maxrnd:
    score = 0
    utilities.clearScreen()
    print("========== TREASURE HUNT GAME ==========")
    print(f"Round {currentrnd} of {maxrnd}")

    utilities.printNumberedList(["Dark Cave","Sandy Beach","Ancient Ruins"])
    utilities.getValidInt("Enter your choice (1-3): ",1,3)

    found = choice(["treasurefnd","trapfnd","none"])

    if found == "treasurefnd":
        print(f"You found the treasure! (+{treasure} Points.)")
        score += treasure
    elif found == "trapfnd":
        print(f"You got trapped! (-{trap} Points.)")
        score -= trap
    else:
        print("You found nothing, better luck next time! (+0 Points)")

    rndpoints.append(score)
    total += score
    print(f"Total Score: {total}")

    currentrnd += 1
    roundplayed += 1
    utilities.pause()
_, treasurecount, trapcount, emptycount = utilities.analyzeNumbers(rndpoints)

utilities.clearScreen()

print("========== TREASURE REPORT ==========")
print(f"Explorer: {username}")

index = 0
while index != roundplayed:
    print(f"Round {index+1} : {rndpoints[index]}")
    index += 1


print(f"Treasure Rounds: {treasurecount} | Trap Rounds: {trapcount} | Empty Rounds: {emptycount} ")
print(f"Total Score: {total}")
if total > 0:
    rank = "Treasure Hunter!"
if total == 0:
    rank = "Unlucky Hunter."
if total < 0:
    rank = "Trapped Hunter"
print(f"Rank: {rank}")