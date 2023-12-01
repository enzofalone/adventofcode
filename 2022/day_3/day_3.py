
total_sum = 0

group_items = {}

with open('input.txt') as file:
    for line in file:
        # first_compartment = line[0 : int(len(line)/2)]
        # second_compartment = line[int(len(line)/2) : -1]

        lowercase = 96
        uppercase_offset = 27
        uppercase = 65

        # compartment_set = set()

        # PART 1
        # for i in range(len(first_compartment)):
        #     for j in range(len(second_compartment)):
        #         if first_compartment[i] == second_compartment[j] and second_compartment[j] not in compartment_set:
        #             compartment_set.add(first_compartment[i])

        #             if ord(first_compartment[i]) >= lowercase:
        #                 total_sum += ord(first_compartment[i]) - lowercase
        #                 # print(first_compartment[i], ord(first_compartment[i]) - lowercase)
        #             else:
        #                 total_sum += ord(first_compartment[i]) - uppercase + uppercase_offset
        #                 # print(first_compartment[i], ord(first_compartment[i]) - uppercase + uppercase_offset)

        # PART 2

        # remove duplicates from current line (and strip to remove endline and prevent headache)
        items = "".join(set(line.strip()))
        
        for i in range(len(items)): # iterate through all letters(items)
            # store them in dictionary to keep account
            if items[i] not in group_items:
                group_items[items[i]] = 1
            else:
                group_items[items[i]] += 1
            
            # ding ding ding we found the badge
            if group_items[items[i]] == 3:
                # sum based on priority
                if ord(items[i]) >= lowercase:
                    total_sum += ord(items[i]) - lowercase
                else:
                    total_sum += ord(items[i]) - uppercase + uppercase_offset
                
                # reset main dictionary for every 3 lines and break loop
                group_items = {}
                break

print(total_sum)