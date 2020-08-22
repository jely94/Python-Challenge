#Import the os module
import os

#Import the module for reading csv file
import csv

#Csv file path
election_data = os.path.join("Resources", "election_data.csv")

#Create lists to hold candidates, votes, and percent of votes
candidates = []
num_votes = []
vote_percent = []

#Create a count for the total number of votes 
total_votes = 0

#Read the Csv and specify delimiter and the variable
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row first
    csv_header = next(csvreader)

    #Read each row of the data after the header
    for row in csvreader:
        #Add to the vote-counter 
        total_votes = total_votes + 1 

        #Adds candidate to list and set num_votes to 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        #Increases num_votes by 1 for candidate
        else:
            index = candidates.index(row[2])
            num_votes[index] = num_votes[index] + 1
    
    #Adds the percentage calculation to vote_percent list and formating
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        #percentage = round(percentage)
        percentage = "%.2f%%" % percentage
        vote_percent.append(percentage)
    
    #Determine the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#Display the results of the election data
print("Here Are The Election Results")
print("--------------------------")
print(f"Total Votes Cast: {str(total_votes)}")
print("--------------------------")

#From each list print out the candidate, number of votes, and percentage of total votes for each candidate
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(num_votes[i])} ({str(vote_percent[i])})")

print("--------------------------")
print(f"And The Winner Is: {winning_candidate}")
print("--------------------------")


#Output data to .txt file
output = open("output.txt", "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes Cast: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))

#From each list print out the candidate, number of votes, and percentage of total votes for each candidate
for i in range(len(candidates)):
    line5 = str(f"{candidates[i]}: {str(num_votes[i])} ({str(vote_percent[i])})")
    output.write('{}\n'.format(line5))

line6 = "--------------------------"
line7 = str(f"Winner: {winning_candidate}")
line8 = "--------------------------"

output.write('{}\n{}\n{}\n'.format(line5, line6, line7))