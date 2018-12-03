import os
import csv

budget_data = os.path.join("./Resources","budget_data.csv")
with open(budget_data, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Create counters/vars for all the aggregates
    total_months = 0
    total_profit = 0
    max_change = 0
    min_change = 0
    avg_helper = 0
    curr_value = 0
    
    # for each row in the file
    for row in csvreader:
        # keep track of last value
        last_value = curr_value
        curr_value = int(row[1])
        # calculate the amount of months
        total_months += 1 
        # add the curr_value to profits
        total_profit += curr_value 
        # if first month, skip
        if (total_months == 1):
            continue
        # calculate change statistics
        curr_change = -(last_value - curr_value)
        avg_helper += curr_change
        # check if curr_value is greater than the previous max, if true, update
        if (curr_change > max_change):
            max_date = row[0]
            max_change = curr_change
        # check if curr_Value is less than the previous min, if true, update
        elif (curr_change < min_change):
            min_change = curr_change
            min_date = row[0]
    # calculate avg change
    avg_change = round(avg_helper/(total_months - 1),2)
    
    # print to terminal
    print ( "Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {total_months}\nTotal: {total_profit}\nAverage Change: {avg_change}")
    print (f"Greatest Increase in Profits: {max_date} ({max_change})\nGreatest Decrease in Profits: {min_date} ({min_change})")
   