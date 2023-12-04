with open("input.txt") as file:
    input = file.read().replace('\n',',').split(",")

originalInput = input

solution = 0

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
        return j.replace(i, "0o")
    elif i == "one":
        return j.replace(i, "o1e")
    elif i == "two":
        return j.replace(i, "t2o")
    elif i == "three":
        return j.replace(i, "t3e")
    elif i == "four":
        return j.replace(i, "4")
    elif i == "five":
        return j.replace(i, "5e")
    elif i == "six":
        return j.replace(i, "6")
    elif i == "seven":
        return j.replace(i, "7n")
    elif i == "eight":
        return j.replace(i, "e8t")
    elif i == "nine":
        return j.replace(i, "n9e")


# identify and replace written numbers with their digit counterpart
for i in numbers:

    for j in range(len(input)):
        
        if i in input[j]:
    
            input[j] = replaceNumber(i, input[j])


# remove non-digit characters from strings
strippedInput = []

for each in input:
    
    newString = ""
    
    for j in range(len(each)):
            
        if each[j].isdigit():
        
            newString += each[j]
        
    strippedInput.append(newString)


# add up first and last numbers of each string
for i in range(len(strippedInput)):
    print("original input " + originalInput[i])
    print("stripped input " + strippedInput[i])
    
    addition = strippedInput[i][0] + strippedInput[i][len(strippedInput[i]) - 1]
    print("adding " + addition)

    solution += int(addition)


print("The answer is: " + str(solution))