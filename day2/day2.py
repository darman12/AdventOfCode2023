with open("input.txt") as file:
    input = file.read().split("\n")

gameData = [
    {
        "ID": 0,
        "diceSets": {
            "red": 0,
            "green": 0,
            "blue": 0
        },
        "power": 0
    }
]    

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
    
def getPower(cubeSet):
    print("::getPower cubeSet")
    
    colorMinimums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for color in cubeSet:
        if each > colorMinimums[each]:
            print(str(each) + " is greater than " + colorMinimums[each])
            colorMinimums[each] = each
    
    power = 1

    for each in colorMinimums:
        power *= each

    print("power: " + str(power))

sum = 0
power = 0



for game in input:

    # create array of game IDs and list of dice
    game = game.replace("Game ", "")
    game = game.split(":")
    game[1] = game[1].strip()

    gameData[game].set("ID", int(game[0]))

    for cubeSet in game[1].split(";"):
        cubeSet = cubeSet.strip()
        colorGroups = cubeSet.split(",")

        for colorGroup in colorGroups:
            gameData[game].set()

    
    validGame = True

    for cubeSet in game[1].split(";"):     
        cubeSet = cubeSet.strip()  
        colorGroups = cubeSet.split(",")
        
        for colorGroup in colorGroups:
            colorGroup = colorGroup.strip()
            if validDraw(colorGroup) == False:
                validGame = False

        power += getPower(cubeSet)

    if validGame == True:
        sum += int(game[0])


print("Part 1 answer: " + str(sum))
print("Part 2 answer: " + str(power))
