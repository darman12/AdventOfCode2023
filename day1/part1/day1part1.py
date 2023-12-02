with open("input.txt") as file:
    input = file.read().replace('\n',',').split(",")

# print(puzzleInput.read())

# parsedInput = input.split(",")



numbers = [
     "zero"
    ,"one"
    ,"two"
    ,"three"
    ,"four"
    ,"five"
    ,"six"
    ,"seven"
    ,"eight"
    ,"nine"
]

def replaceNumber(i, j):
    if i == "zero":
        return j.replace(i, "0")
    elif i == "one":
        return j.replace(i, "1")
    elif i == "two":
        return j.replace(i, "2")
    elif i == "three":
        return j.replace(i, "3")
    elif i == "four":
        return j.replace(i, "4")
    elif i == "five":
        return j.replace(i, "5")
    elif i == "six":
        return j.replace(i, "6")
    elif i == "seven":
        return j.replace(i, "7")
    elif i == "eight":
        return j.replace(i, "8")
    elif i == "nine":
        return j.replace(i, "9")

for i in numbers:
    for j in range(len(input)):
        if i in input[j]:
            input[j] = replaceNumber(i, input[j])
        # else:
        #     print("did not find " + i + " in " + j)
        #     # print(i)

for j in input:
    print(j)

for each in input:
    for each in each:
        if each.isdigit():
            print(each + " is a digit")
        else:
            print(each + " is not a digit")