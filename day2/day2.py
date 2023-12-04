with open("input.txt") as file:
    input = file.read().split("\n")

colorMaximums = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def validDraw(colorGroup):
    numDice = int(colorGroup.split(" ")[0])
    color = colorGroup.split(" ")[1]
    
    if numDice > colorMaximums[color]:
        return False

sum = 0

for game in input:

    # create array of game IDs and list of dice
    game = game.replace("Game ", "")
    game = game.split(":")
    game[1] = game[1].strip()
    
    validGame = True

    for cubeSet in game[1].split(";"):     
        cubeSet = cubeSet.strip()  
        colorGroups = cubeSet.split(",")
        
        for colorGroup in colorGroups:
            colorGroup = colorGroup.strip()
            if validDraw(colorGroup) == False:
                validGame = False

    if validGame == True:
        sum += int(game[0])

print("The answer is " + str(sum))