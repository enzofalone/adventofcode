score_win = 6
score_draw = 3
score_lose = 0



## PART 1
# winning moves provided by cool elf
# strategy_dict = {
#     'A': 'Y',
#     'B': 'Z',
#     'C': 'X'
# }

# get equivalent of opponent moves -> my moves
equivalent_dict = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

# get score just by passing this dictionary to my move
score_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

total_score = 0

## PART 2

# losing moves
losing_dict = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

winning_dict = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


with open('input.txt') as file:
    for line in file:
        # 0 -> opponent
        # 1 -> me
        turn_array = line.split()

        ##### PART ONE

        # # won with strategy
        # if strategy_dict[turn_array[0]] == turn_array[1]:
        #     total_score += score_dict[turn_array[1]] + score_win
        # # draw with strategy
        # elif equivalent_dict[turn_array[0]] == turn_array[1]:
        #     total_score += score_dict[turn_array[1]] + score_draw
        # # lost with strategy
        # else:
        #     total_score += score_dict[turn_array[1]] + score_lose

        ##### PART TWO
        
        if turn_array[1] == 'Y':
            total_score += score_dict[equivalent_dict[turn_array[0]]] + score_draw
        elif turn_array[1] == 'X':
            total_score += score_dict[losing_dict[turn_array[0]]]
        else:
            total_score += score_dict[winning_dict[turn_array[0]] ] + score_win

        
        

print("total score is: " + str(total_score))