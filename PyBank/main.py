# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = r'C:\Users\merse\Documents\python_challenge\PyBank\Resources\budget_data.csv'
# os.path.join('..', 'Resources', 'accounting.csv')


tot_p = []
date = []
monthly_change_list = []
first_value = 867884 
count = 0
tot_value = 0
next_value = 0
change = 0
average_change = 0
sum_change = 0
great_increase = 0
great_decrease = 0
date_max_increase = 0
date_max_decrease = 0

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
     
    # Read each row of data after the header and count the number of rows
    for row in csvreader:
       # Add dates
        date.append(row[0])

        # Add total profit/losses
        tot_p.append(row[1])

        count = count + 1
        tot_value = tot_value + int(row[1])
        next_value = int(row[1])
        change = next_value - first_value
        # put the monthly changes into the monthly change list
        monthly_change_list.append(change)
        first_value = next_value
        sum_change= sum_change + change
    
    print ("                               ")    
    print ("Financial Analysis")
    
    print ("-------------------------------")         
    # print the total number of months
    print ("total months = " + str(count))
    print ("total_profit/loss = $ " + str(tot_value))   
    # print (date)
    # print (tot_p)
    # print (monthly_change_list)  "for chacking!"
    average_change = int(sum_change/(count -1))
    print ("Averange monthly change = $ " + str(average_change))

    # find and print the min and max change in the monthly_change_list
    great_increase = max (monthly_change_list)
    great_decrease = min (monthly_change_list)
    date_max_increase = date[monthly_change_list.index(great_increase)]
    date_max_decrease = date[monthly_change_list.index(great_decrease)]
    print ("Increase in profit = $ " + str(great_increase) + " on " + date_max_increase)
    print ("the greatest decrease = $ " + str(great_decrease) + " on " + date_max_decrease)
    print ("----------------------------------")

    Pybank_analysis = r"C:\Users\merse\Documents\python_challenge\PyPoll\analysis"
    # os.path.join("web_final.csv")
    with open ('Pybank_analysis.txt', 'w') as text:
        text.write("                               ")
        text.write("Financial Analysis")
        text.write("-------------------------------")
        text.write("total months = " + str(count))
        text.write("total_profit/loss = $ " + str(tot_value)) 
        text.write("Averange monthly change = $ " + str(average_change))
        text.write("Increase in profit = $ " + str(great_increase) + " on " + date_max_increase)
        text.write("the greatest decrease = $ " + str(great_decrease) + " on " + date_max_decrease)
        text.write("-------------------------------")
