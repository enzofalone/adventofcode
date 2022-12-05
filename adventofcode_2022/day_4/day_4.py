total_sum = 0

with open('input.txt') as file:
    for line in file:
        pairs = line.strip().split(',')

        first_pair = pairs[0].split('-')
        second_pair = pairs[1].split('-')
        
        # PART ONE
        # split in half for more readability
        # if (int(first_pair[0]) <= int(second_pair[0])) and (int(first_pair[1]) >= int(second_pair[1])):
        #     total_sum += 1
        # elif (int(first_pair[0]) >= int(second_pair[0])) and (int(first_pair[1]) <= int(second_pair[1])):
        #     total_sum += 1
        
        # PART TWO
        if (int(first_pair[0]) <= int(second_pair[0])) and (int(first_pair[1]) >= int(second_pair[1])):
            total_sum += 1
        elif (int(first_pair[0]) >= int(second_pair[0])) and (int(first_pair[1]) <= int(second_pair[1])):
            total_sum += 1
        elif (int(first_pair[1]) >= int(second_pair[0])) and (int(second_pair[1]) >= int(first_pair[1])):
            total_sum += 1
        elif (int(second_pair[1]) >= int(first_pair[0])) and (int(first_pair[1]) >= int(second_pair[1])):
            total_sum += 1
            


print(total_sum)
