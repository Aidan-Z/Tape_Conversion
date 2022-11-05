import math

pi = math.pi
depth_slot = 0.6                                            # depth of slot
length_slot = 2.4                                           # length of slot + space between next slot
radius_start = 3.75                                         # un-used space in middle of carrier tape reel


rows_remaining = input("How many rows of tape remain?: ")


def find_slots_remaining():                                 # function to find how many slots are left
    row_float = float(rows_remaining)                       # convert user input to a float
    row_int = int(row_float)                                # convert 'n' back to an int for rnage function
    for row_float in range(1, row_int):                     # create a range for user input
        conv_list = list(range(1, row_int+4))               # put range into a list (+ the hidden rows- varies for each type of tape)
        it_list = [i * depth_slot for i in conv_list]       # list comp.
        radius = [i + radius_start for i in it_list]        # find radius
        circumfrence = [(2*pi) * i for i in radius]         # find circumfrence
        quotient = [i / length_slot for i in circumfrence] 
        remaining_slots = sum(quotient)                     # give the remaining slots on tape in reel
        return(remaining_slots)                             # return slots left when this function is called
        
x = find_slots_remaining()                                  # call function
slots_remaining = round(x)                                  # round to nearest whole number
print('There are:',slots_remaining, 'slots remaining') 
print('===============================')
in_metres = round(((x * length_slot) / 100), 3)                        # convert to metres of reel left
print('There are: ', in_metres, 'metres remaining')












