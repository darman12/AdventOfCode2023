with open("input.txt") as file:
    input = file.read().split("\n")

originalInput = input

# remove non-digit characters from strings
strippedInput = []

for each in input:
    
    newString = ""
    
    for j in range(len(each)):
            
        if each[j].isdigit():
        
            newString += each[j]
        
    strippedInput.append(newString)


sum = 0

# add up first and last numbers of each string
for i in range(len(strippedInput)):
    
    sum += int(strippedInput[i][0] + strippedInput[i][len(strippedInput[i]) - 1])

print("The answer is: " + str(sum))