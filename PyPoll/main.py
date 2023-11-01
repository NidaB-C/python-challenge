import os
import csv 

#Set path for csv file - absolute path was used for development - has been changed to relative path for GitHub
election_data = os.path.join("..","python-challenge","PyPoll","Resources","election_data.csv")

#Define function to calculate the percentage of the vote for each candidate
def calculate_percentage(part,whole):
    return (float(part)/float(whole))* 100

#Initialise variables 
total_votes = 0
candidates = {}

#Read the CSV file and store the header
with open(election_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Define variables in each column by unapcking the tuple
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        #Count the total votes 
        total_votes += 1
        
        #Count the votes for each candidate 
        # - if name is in dictionary, add to count, if not, add name as key and add to count in value
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Find the winner 
winner = max(candidates, key=candidates.get)

# Print the title and total votes 
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

#Save the output filepath
output_file = os.path.join ("..","PyPoll","analysis","Election Analysis.txt")

#Open and print output in the text file 
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-" * 30 + "\n")

    #Calculate the percentage of votes for each candidate (using function described above) and print in terminal and text file 
    for candidate, votes in candidates.items():
        percentage = calculate_percentage(votes, total_votes)
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    #Print the winner 
    print("-" * 30)
    print(f"Winner: {winner}")
    print("-" * 30)
    
    #Save the winner name to the text file 
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-" * 30 + "\n")








