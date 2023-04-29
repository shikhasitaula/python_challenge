#import different librabry to perform the methds.
import math 
import csv

# assign the path to get the correct file from where it is stored
csvpath = "./Resources/budget_data.csv" 
# use of 'with open' to assess the file and read and return the data.
# the delimiter indicates the next value for the row 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #separates the header from the group of data
    print(f"csv header: {csv_header}")
    month_count = 0
    total_profit_loss = 0
    change_in_profitloss= 0
    row_count = 1
    new_list = []
    greatest_increase = -math.inf 
    greatest_decrease = math.inf  
    print("Financial Analysis")
    print("-------------------------------------------")
    # uses for loop to iterate through each of the rows and saves each row separately
    for row in csvreader:
        #appends each rows to the new list.
        new_list.append(row)
        #counts the number of row to find the total months
        month_count = month_count + 1
        #calculates total profit and loss over the entire period
        total_profit_loss = total_profit_loss + int(row[1])
        change_in_profitloss_total = 0
    print(f"Total months : {month_count}")
    print(f"Total :  ${total_profit_loss}")
    # here the logic loops thorough entire rows and finds out the average change in profit and loss
    # then compairs the change to find out the greatest increase and decrease in profit and loss
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
    print(f"Average Change:  ${round(average_of_change_in_profitloss, 2 )}")
    print(f"Greatest Increase in Profits  :  {data_of_change_in_profitloss_increase} (${greatest_increase})")
    print(f"Greatest Decrease in Profits  :  {data_of_change_in_profitloss_decrease} (${greatest_decrease})")
