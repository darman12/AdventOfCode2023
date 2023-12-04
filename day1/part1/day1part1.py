with open("input.txt") as file:
    input = file.read().replace('\n',',').split(",")

originalInput = input

solution = 0


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
    
    solution += int(strippedInput[i][0] + strippedInput[i][len(strippedInput[i]) - 1])


print("The answer is: " + str(solution))