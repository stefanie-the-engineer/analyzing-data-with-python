import os
import csv

# this module reads in csv file, counts all votes, gets candidate names, prints percentage for each candidate and provides output to both the terminal and a text file

# get the csv file and create output folder and output file
this_folder = os.path.dirname(__file__)
import_path = os.path.join(this_folder, "Resources", "election_data.csv")
output_path = os.path.join(this_folder, "Output", "election_results.txt")

votes = []
candidates = {}

# method to convert list to set to get unique candidates, 
def printToTerminalCandidatesWithVotes(votes = [], candidates = {}):
    
    # converts list to set to get all unique candidate names
    candidates = {*votes}
    
    # list declaration and instantiation to store percentages for candidates
    percents = []
    candiatesWithVotes = []
    
    # variable declarations and initializations 
    winner = ""
    count = 0
    
    # print results to terminal
    print("Election Results")
    print("----------------------------------------------")
    print("Total Votes: " + str(len(votes)))
    print("----------------------------------------------")
    
    for candidate in candidates:
        for vote in votes:
            if vote == candidate:
                count = count + 1
            else:
                continue
        percents.append(count / len(votes))
        print(candidate + ": " + '{:.3%}'.format(count / len(votes)) + " (" + str(count) + ")")
        count = 0
        
    print("----------------------------------------------")
    
    # get the winner of the election - uses list to iterate through percents, stores max and index of highest percent (index of highest percent will be index of candidate list to retrieve winner
    max = 0
    index = 0
    for i, percent in enumerate(percents):
        if percent > max:
            max = percent
            index = i
            
    # convert set back to list so we have access to indexing
    candidatesWithVotes = list(set(candidates))
    
    # set translates to list with same index hence we can do this        
    print("Winner: " + candidatesWithVotes[index])
       
    print("----------------------------------------------")
    
def printToTextFileCandidatesWithVotes(votes = [], candidates = {}, output_path = ""):
    
    # converts list to set to get all unique candidate names
    candidates = {*votes}
    
    # create output file to write
    output_file = open(output_path, "w")
    
    # list declaration and instantiation to store percentages for candidates
    percents = []
    candiatesWithVotes = []
    
    # variable declarations and initializations 
    winner = ""
    count = 0
    
    # print results to terminal
    output_file.write("Election Results\n")
    output_file.write("----------------------------------------------\n")
    output_file.write("Total Votes: " + str(len(votes)) + "\n")
    output_file.write("----------------------------------------------\n")
    
    for candidate in candidates:
        for vote in votes:
            if vote == candidate:
                count = count + 1
            else:
                continue
        percents.append(count / len(votes))
        output_file.write(candidate + ": " + '{:.3%}'.format(count / len(votes)) + " (" + str(count) + ")\n")
        count = 0
        
    output_file.write("----------------------------------------------\n")
    
    # get the winner of the election - uses list to iterate through percents, stores max and index of highest percent (index of highest percent will be index of candidate list to retrieve winner
    max = 0
    index = 0
    for i, percent in enumerate(percents):
        if percent > max:
            max = percent
            index = i
            
    # convert set back to list so we have access to indexing
    candidatesWithVotes = list(set(candidates))
    
    # set translates to list with same index hence we can do this        
    output_file.write("Winner: " + candidatesWithVotes[index] + "\n")
       
    output_file.write("----------------------------------------------")

# reads in csv from resources folder
with open(import_path, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        votes.append(row[2])

# print results to terminal
printToTerminalCandidatesWithVotes(votes, candidates)

# prints results to output text file
printToTextFileCandidatesWithVotes(votes, candidates, output_path)