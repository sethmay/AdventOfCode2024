# Advent of Code Day 1 - Part 1

# Step 1 - read in file
with open ('../../AdventOfCode2024_Inputs/day01/inputs2.txt', 'r') as inputfile:
    inputList = inputfile.read().splitlines()

# Step 2 - Split into two lists
set1 = []
set2 = []

for line in inputList:
    var = line.split("   ")
    set1.append(var[0])
    set2.append(var[1])


#Step 3 - Sort the lists
set1.sort()
set2.sort()


#Set 4 - Find distance scores
distances = []

counter = 0
while (counter < len(set1)):
    distances.append(abs(int(set1[counter]) -  int(set2[counter])))
    counter = counter + 1

sumDistances = 0
for val in distances:
    print(val)
    sumDistances = sumDistances + val

print('sum: ' + str(sumDistances))