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
#brute force method:
CandidatesList= []

# calculate total number of votes each candidate won
VotesKhan = 0
VotesCorrey = 0
VotesLi = 0
VotesOTooley = 0

for x in Candidate:
    if x not in CandidatesList:
        CandidatesList.append(x)
    if x == 'Khan':
        VotesKhan = VotesKhan + 1
    elif x == 'Correy':
        VotesCorrey = VotesCorrey + 1
    elif x == 'Li':
        VotesLi = VotesLi + 1
    elif x == "O'Tooley":
        VotesOTooley = VotesOTooley + 1

# calculate percentage of votes each candidate won

    PercentageKhan = '{:.2%}'.format(VotesKhan / totalvotes)
    PercentageCorrey = "{:.2%}".format(VotesCorrey / totalvotes)
    PercentageLi = "{:.2%}".format(VotesLi / totalvotes)
    PercentageOTooley = "{:.2%}".format(VotesOTooley / totalvotes)

#create dictionary with stats
CandidateStats = [
    {'Candidate' :'Khan', 'Votes' : VotesKhan, 'VotesPercent' : PercentageKhan},
    {'Candidate' : 'Correy', 'Votes' : VotesCorrey, 'VotesPercent' : PercentageCorrey},
    {'Candidate' : 'Li', 'Votes' : VotesLi, 'VotesPercent' : PercentageLi},
    {'Candidate' : 'OTootley', 'Votes' : VotesOTooley, 'VotesPercent' : PercentageOTooley}]

# calculate the winner of the election based on popular vote.
#use list sort method to sort in order of greatest votes then choose the winner as the first palce in the list 
SortedResults = sorted(CandidateStats, key=lambda k: k['Votes'], reverse = True) 
Winner = SortedResults[0]

# print final results
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(totalvotes))
print("-----------------------")
print(SortedResults[0])
print(SortedResults[1])
print(SortedResults[2])
print(SortedResults[3])
print("-----------------------")
print("The Winner is " + str(Winner))
#export to text file 
with open("out.txt", "w") as f:
    f.write("OUTPUT")

  