

with open('input.txt') as file:
    for line in file:

        n = 1
        checked = dict()
        sequence = ''
        for i in range(len(line)):
            sequence += line[i]

            # if the length is more than 4
            # we can begin doing logic
            if len(sequence) > 4:
                # remove first character so we always have 4 characters
                sequence = sequence[1::]

                # check for duplicates
                checked = dict()
                duplicate = False
                
                for letter in sequence:
                    if letter not in checked:
                        checked[letter] = 1
                    else:
                        duplicate = True
                        break
                
                if duplicate == False:
                    print(sequence)
                    print(i+1) # index begins at 1
                    break
