crates = [
    ['F','H','B','V','R','Q','D','P'],
    ['L', 'D', 'Z','Q','W','V'],
    ['H','L','Z','Q','G','R','P','C'],
    ['R','D','H','F','J','V','B'],
    ['Z','W','L','C'],
    ['J','R','P','N','T','G','V','M'],
    ['J','R','L','V','M','B','S'],
    ['D','P','J'],
    ['D','C','N','W','V']
]

# crates = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P']
# ]

with open('input.txt') as file:
    for line in file:
            # [0] -> move how many
            # [1] -> from where
            # [2] -> to where
            instructions = line.split(' ')
            n = int(instructions[1])
            column_from = int(instructions[3]) - 1
            column_to = int(instructions[5]) - 1

            order = n

            for i in range(n):
                crate_moved = crates[column_from].pop(len(crates[column_from]) - n)
                crates[column_to].append(crate_moved)
                n -= 1
            


result = ''

for i in range(len(crates)):
    result += str(crates[i][-1])

print(result)