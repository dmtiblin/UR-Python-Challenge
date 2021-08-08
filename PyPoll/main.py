# import os and create file path
import os 
import csv
csvpath = os.path.join("Resources", "election_data.csv")

#open and read the csv file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header
    next(csvreader)
    #create variables for list data
    VoterID = []
    County = []
    Candidate = []
    #add data to python lists
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

# calculate total number of votes cast
totalvotes = len(Candidate)

# generate a complete list of candidates who received votes
#brut forecce method:
CandidatesList= []
for x in Candidate:
    if x not in CandidatesList:
        CandidatesList.append(x)
print(CandidatesList)

# calculate total number of votes each candidate won


# calculate percentage of votes each candidate won

# calculate the winner of the election based on popular vote.

# print final results
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(totalvotes))
print("-----------------------")
#export to text file 