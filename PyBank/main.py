# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')
# r'C:\Users\merse\Documents\python_challenge\PyBank\Resources\budget_data.csv'

tot_p = []
date = []
monthly_change_list = []
previous_value =0
count = 0
tot_value = 0

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
    Jan_data = next (csvreader)
    count = count+1 
    tot_value = tot_value + int(Jan_data[1])
    previous_value = int(Jan_data[1])

    # Read each row of data after the header and count the number of rows
    for row in csvreader:
       # Add dates
        date.append(row[0])

        # Add total profit/losses
        tot_p.append(row[1])

        count = count + 1
        tot_value = tot_value + int(row[1])
        
        change =int(row[1]) - previous_value
        previous_value = int(row[1])
        # put the monthly changes into the monthly change list
        monthly_change_list.append(change)
        
    average_change = round(sum(monthly_change_list)/len(monthly_change_list),2)
    
    print ("                               ")    
    print ("Financial Analysis")
    
    print ("-------------------------------")         
    # print the total number of months
    print ("Total Months = " + str(count))
    print ("Total_profit/loss = $ " + str(tot_value))   
    # print (date)
    # print (tot_p)
    # print (monthly_change_list)  "for chacking!"
    
    print ("Averange Monthly Change = $ " + str(average_change))

    # find and print the min and max change in the monthly_change_list
    great_increase = max (monthly_change_list)
    great_decrease = min (monthly_change_list)
    date_max_increase = date[monthly_change_list.index(great_increase)]
    date_max_decrease = date[monthly_change_list.index(great_decrease)]
    print ("The Greatest Increase = $ " + str(great_increase) + " on " + date_max_increase)
    print ("The Greatest Decrease = $ " + str(great_decrease) + " on " + date_max_decrease)
    print ("----------------------------------")

    Pybank_analysis = os.path.join('analysis')
    #r"C:\Users\merse\Documents\python_challenge\PyPoll\analysis"
    # 
    with open ('Pybank_analysis.txt', 'w') as text:
        text.write("                               \n")
        text.write("Financial Analysis\n")
        text.write("-------------------------------\n")
        text.write("Total Months = " + str(count) + "\n")
        text.write("Total_profit/loss = $ " + str(tot_value) + "\n") 
        text.write("Averange Monthly Change = $ " + str(average_change) + "\n")
        text.write("The Greatest Increase  = $ " + str(great_increase) + " on " + date_max_increase + "\n")
        text.write("The Greatest Decrease = $ " + str(great_decrease) + " on " + date_max_decrease + "\n")
        text.write("-------------------------------\n")
