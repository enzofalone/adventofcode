MAX_DIRECTORY_SIZE = 100000

input = ''

with open('input.txt') as file:
    input = file

for line_input in input:
    line = line_input.strip().split(' ')

    # if current line is an instruction
    if line[0] == '$':
        if line[1] == 'cd':
            
    else: