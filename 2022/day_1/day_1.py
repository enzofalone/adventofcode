puzzleFile = open('input.txt','r')

elfList = []
currElf = 0

with open('input.txt') as puzzleFile:
    for lineCal in puzzleFile:
        if len(lineCal) == 1: # empty string
            elfList.append(currElf)

            currElf = 0
        else:
            currElf += int(lineCal)

elfList = sorted(elfList, reverse=True)

print(elfList[0] + elfList[1] + elfList[2])