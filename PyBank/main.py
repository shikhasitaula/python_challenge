# Imports different libraries to perform methods.
import math 
import csv
import os

# Assigns the path to get the correct file from where it is stored.
csvpath = os.path.join('.','Resources','budget_data.csv') 

# Opens new file for storing the result.
file_write = open(os.path.join('.','analysis','PyBank_result.txt'), 'w' )

# The function below wrint output to both terminal and file once it is called.
def print_to_terminal_and_file(file_open, text):
    print(text)
    file_open.write(text + "\n")
    
# Uses of 'with open' to assess the file and read and return the data.     
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    # Separates the header from the rest of the data.
    month_count = 0
    total_profit_loss = 0
    change_in_profitloss= 0
    row_count = 1
    new_list = []
    greatest_increase = -math.inf 
    greatest_decrease = math.inf  
    print_to_terminal_and_file(file_write,"Financial Analysis\n")
    print_to_terminal_and_file(file_write,"-------------------------------------------\n")
    # Uses 'for loop' to iterate through each of the rows and saves each row separately.
    for row in csvreader:
        # Appends each row to the new list.
        new_list.append(row)
        # Counts the number of rows to find the total months.
        month_count = month_count + 1
        # Calculates total profit and loss over the entire period
        total_profit_loss = total_profit_loss + int(row[1])
        change_in_profitloss_total = 0
    print_to_terminal_and_file(file_write,f"Total months : {month_count}\n")
    print_to_terminal_and_file(file_write,f"Total :  ${total_profit_loss}\n")
    
    # The logic loops through entire rows and finds out the average change in profit and loss
    # Then the if condition compairs the change to find out the greatest increase and decrease in profit and loss
    for index in range(1, len(new_list), 1):
        previous_profitloss= new_list[index - 1]
        current_profitloss= new_list[index]
        change_in_profitloss = int(current_profitloss[1]) - int(previous_profitloss[1])
        change_in_profitloss_total = change_in_profitloss_total + change_in_profitloss
        if change_in_profitloss > greatest_increase:
            greatest_increase = change_in_profitloss
            data_of_change_in_profitloss_increase = current_profitloss[0]
            
        if change_in_profitloss < greatest_decrease:
            greatest_decrease = change_in_profitloss 
            data_of_change_in_profitloss_decrease = current_profitloss[0]
    average_of_change_in_profitloss = change_in_profitloss_total / (len(new_list)-1)   
    # Calls "the print_to_terminal_and_file" functions to print logic both in the terminal and the text file.                                 
    print_to_terminal_and_file(file_write, f"Average Change:  ${round(average_of_change_in_profitloss, 2 )}\n")
    print_to_terminal_and_file(file_write, f"Greatest Increase in Profits  :  {data_of_change_in_profitloss_increase} (${greatest_increase})\n")
    print_to_terminal_and_file(file_write, f"Greatest Decrease in Profits  :  {data_of_change_in_profitloss_decrease} (${greatest_decrease})\n")
    file_write.close()