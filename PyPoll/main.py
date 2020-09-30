#First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath =  os.path.join('Resources', 'election_data.csv')
#r'C:\Users\merse\Documents\python_challenge\PyPoll\Resources\election_data.csv'
# os.path.join('..', 'Resources', 'accounting.csv')
# declare variables 
candidate = []
candidate_votes = {}
count = 0
tot_vote = 0
percent_vote = []

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
     
    # Read each row of data after the header and count the number of rows
    for row in csvreader:
         # Add Voter Id
        candidate = row[2]
        count = count + 1 
        # count the number of votes for each candidate
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1
print("                        ")
print("Election Results") 
print("---------------------------")            
print("Total Votes: " + str(count))
# for each unique candidate, calculate the percentage based on the number of votes, then print each uniqu candidate name with their number and percentage vote
for i in candidate_votes:
    percent = round((float(candidate_votes[i])/count)*100, 0)
    constant = "% ("
    print (f'{i} {percent} {constant} {candidate_votes[i]}' + ")")

for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key


print("---------------------------")      
print ("The winner is : " + winner)
print("---------------------------")

 # Go to analysis folder, create a text file and print the same result there 
Pypoll_analysis = os.path.join("analysis", "Pypoll_analysis.txt")
   
     
with open (Pypoll_analysis , "w") as text:
    
    text.write("                        \n")
    text.write("Election Results\n") 
    text.write("---------------------------\n")            
    text.write("Total Votes: " + str(count) + "\n")

    for i in candidate_votes:
        percent = round((float(candidate_votes[i])/count)*100, 0)
        constant = "% ("
        text.write (f'{i} {percent} {constant} {candidate_votes[i]}' +")\n")
        
    text.write("---------------------------\n")      
    text.write("The winner is : " + winner +"\n")
    text.write("---------------------------\n")   
    



 
