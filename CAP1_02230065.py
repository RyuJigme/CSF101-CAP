################################
# Jigme Thinley
# 1. Electrical
# 02230065
################################
# REFERENCES
# @DQ-Logo
# @https://www.blackbox.ai/
################################
# SOLUTION
# Your Solution Score:49977
# CSF101-CAP/input_5_cap1.txt
################################# Read the input.txt file
def read_input(Insert_file_name): # First we have to define a fucntion "read_input"
    x = [] # then initialize an empty list
    with open(Insert_file_name, 'r') as files: # For each line in the file
        for y in files: #we have to split the lines into two parts using whitespace as the delimiter
            challenger_option, result = y.split() # we have to initialize a tuple containing the two parts and append it to the above list
            x.append((challenger_option, result)) # we have to initialize a tuple containing the values of 'challenger_option' and 'result', and append it to the list
    return x # We have to Return the list containing 'challenger_option' and 'result'

# for calculating the score of each round
def calculate_score(total_rounds): # we have to define a function calculate_score inorder to calculates a score of "total_rounds"
    score = 0 # The starting score shold be 0
    for challenger_option, result in total_rounds: #we should iterate through each game in "total_rounds" 
# and show the values of 'challenger_option' and 'result'
        if result == 'X':  #For X we have to lose and challenger should win
            if challenger_option == 'A': # Challenger shows Rock
                score += 3 # Rock wins over scissor
            elif challenger_option == 'B': # challenger shows Paper
                score += 1  # Paper wins over rock
            elif challenger_option == 'C': # Opponent shows Scissor
                score += 2 # Scissors wins over paper
        elif result == 'Y':  # Both should be draw 
            if challenger_option == 'A': # challenger chose Rock
                score += 4  # Rock against Rock is draw 
            elif challenger_option == 'B': # challenger chose Paper
                score += 5  # Paper against Paper is draw 
            elif challenger_option == 'C': # challenger chose Scissors
                score += 6  # Scissors against Scissors is draw 
        elif result == 'Z':  # We have to win and challenger should lose 
            if challenger_option == 'A': # challenger chose Rock
                score += 8  # Paper wins over Rock
            elif challenger_option == 'B': # challenger chose Paper
                score += 9 # Scissors wins over Paper
            elif challenger_option == 'C': # challenger chose Scissors
                score += 7 # Rock wins over Scissor
    print(f"Your final score is:{score}") #We have to print out the total sum of the scores from the input file designated

#To run the program
Insert_file_name = "CSF101-CAP/input_5_cap1.txt"  # As per index number of the students
calculate_score(read_input(Insert_file_name)) # we have to calculate the final score using the data obtained from reading the input file
