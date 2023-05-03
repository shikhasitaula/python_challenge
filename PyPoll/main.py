# Impots csv ,os and math library.
import csv
import math
import os

# Opens text file named PyPoll_result.txt.
file_write = open(os.path.join('.','analysis','PyPoll_result.txt'), 'w' )
# Goes to the the folder where the csv file is saved.
csvpath = os.path.join('.','Resources','election_data.csv')
# Prints the logic to both terminal and text file.
def print_in_terminal_and_text_file(file_open, text):
    print(text)
    file_open.write(f"{text}\n")
# Uses of 'with open' to assess the file and read and return the data.  
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    print_in_terminal_and_text_file(file_write,"Election Results\n")
    print_in_terminal_and_text_file(file_write,"-------------------------------\n")
    
    total_vote_count = 0
    # Creates the dictionaty and saves the unique candidate and stores the total vote counts of each.
    vote_count_for_each_candidate = {}
    candidate_count = 0
    # Iterates though each row in the csv file.
    # Counts the total number of votes cast.
    # Uses if condition to iterate though each row in column 2 to find the unique candidate as key.
    # counts the votes count of each candidate and stores it as a value.
    for row in csvreader:
        total_vote_count = total_vote_count + 1   
        if (row[2] in vote_count_for_each_candidate):
            candidate_count = vote_count_for_each_candidate[row[2]] + 1
            vote_count_for_each_candidate[row[2]] = candidate_count   
        else: 
            candidate_count = 1
            vote_count_for_each_candidate[row[2]] = candidate_count
        percentage = (candidate_count/ total_vote_count)*100
    print_in_terminal_and_text_file(file_write,f"Total Votes:  {total_vote_count}\n")
    print_in_terminal_and_text_file(file_write,"-------------------------------\n")       
    winner = -math.inf
    winner_name = ""
    # Iterates throung each candidate and performs the percentage calculation.
    # Uses if condition to find the candidate with highest number of vote.
    for candidate in vote_count_for_each_candidate:
        vote_count =  vote_count_for_each_candidate[candidate]
        percentage = round((vote_count/ total_vote_count)*100, 3)
        print_in_terminal_and_text_file(file_write, f"{candidate} : {percentage}%  ({vote_count_for_each_candidate[candidate]})\n")
        if  vote_count > winner:
            winner = vote_count 
            winner_name = candidate
    print_in_terminal_and_text_file(file_write,"-------------------------------\n") 
    print_in_terminal_and_text_file(file_write,f"Winner: {winner_name}\n")   
    print_in_terminal_and_text_file(file_write,"-------------------------------") 
# Close the text file     
file_write.close() 
   
        