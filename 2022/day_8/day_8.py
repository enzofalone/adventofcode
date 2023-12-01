map = []

visible_trees = 0

with open('input.txt') as file:
    for line in file:
        map.append(list(line.strip()))

for i in range(len(map)):
    if i == 0 or i == (len(map)-1):
        visible_trees += 1
    
    for j in range(len(map[i])):
        if j == 0 or j == (len(map[i])-1):
            print(map[i][j])
            visible_trees += 1
            continue
        
print(visible_trees)

