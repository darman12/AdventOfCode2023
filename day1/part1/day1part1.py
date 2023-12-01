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

# for each in input:
#     if "four" in each.lower():
#         print(each)

for i in numbers:
    print("searching for " + i)
    for j in input:
        if i not in j:
            print("did not find " + i + " in " + j)
            # print(i)