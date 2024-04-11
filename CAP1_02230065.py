################################
# Jigme Thinley
# 1. Electrical
# 02230065
################################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
################################
# SOLUTION
# Your Solution Score:49977
# CSF101-CAP/input_5_cap1.txt
################################# Read the input.txt file
def read_input(Insert_file_name): # We define a fucntion "read_input"
    x = [] # initialize an empty list
    with open(Insert_file_name, 'r') as files: # For each line in the file
        for y in files: # Split the lines into two parts using whitespace as the delimiter
            challenger_option, result = y.split() # initialize a tuple containing the two parts and append it to the above list
            x.append((challenger_option, result)) # initialize a tuple containing the values of 'challenger_option' and 'result', and append it to the list
    return x # Return the list containing 'challenger_option' and 'result'

# Calculating the point for each game/round
def calculate_score(total_rounds): # Calculates a score based on "total_rounds"
    score = 0 # The starting score is 0
    for challenger_option, result in total_rounds: # Iterate through each game in "total_rounds" 
# and show the values of 'challenger_option' and 'result'
        if result == 'X':  # we have to lose and challenger should win
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
    print(f"Your final score is:{score}") #Printing out the total sum of the scores from the input file

# Running the program
Insert_file_name = "CSF101-CAP/input_5_cap1.txt"  # As per index number of the students
calculate_score(read_input(Insert_file_name)) # Calculate the final score using the data obtained from reading the input file