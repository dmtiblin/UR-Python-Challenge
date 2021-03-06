# import os and create file path
import os 
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

#open and read the csv file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header
    next(csvreader)
    #create variables for list data
    Date = []
    PL = []
    #add data to python lists
    for row in csvreader:
        Date.append(row[0])
        PL.append(int(row[1]))

# calculate total number of months included in the dataset
#format the date into datetime
from datetime import datetime 

working_dates= []

for date in Date:
    
    working_dates.append(datetime.strptime(date, '%b-%Y').date())

#find max & min
latest_date = max(working_dates)
earliest_date = min(working_dates)
#print(earliest_date)
#print(latest_date)

#calculate # of months # WIP** 

totalmonths = len(working_dates)


totaldays = (latest_date-earliest_date) 
totalmonths2 = totaldays / 30


# calculate net total amount of "Profit/Losses" over the entire period
PLTotal = sum(PL)

# Calculate the changes in "Profit/Losses" over the entire period, 
PLchangemonthly = []
formattedPLchangemonthly = []
PLchangemonthly.insert(0,0)
for i in range(len(PL)):
    if i > 0:
        PLchangesinglemonth = PL[i]- PL[i-1]
        PLchangemonthly.append(PLchangesinglemonth)
        formattedPLchangesinglemonth = PLchangesinglemonth
        formattedPLchangemonthly.append(formattedPLchangesinglemonth)
        

# then find the average of those changes
AvgPLchange = sum(PLchangemonthly) / (totalmonths-1)

# find the greatest increase in profits (date and amount) over the entire period
maxPLincrease = max(PLchangemonthly)

# find the greatest decrease in profits (date and amount) over the entire period
minPLincrease = min(PLchangemonthly)

#zip together the max and min PL changes with their corresponding months
reportedPLchangezip = dict(zip(Date, PLchangemonthly))
for Date, PLchangemonthly in reportedPLchangezip.items():
    if PLchangemonthly == maxPLincrease:
        formattedmaxPLincrease = Date + " " + "${:,.2f}".format(PLchangemonthly)
    if PLchangemonthly == minPLincrease:
        formattedminPLincrease = Date + " " + "${:,.2f}".format(PLchangemonthly)

#print final results
print("Financial Analysis:") 
print("-----------------------")
print("Total Months: " + str(totalmonths))
print("Total Profit: " + "${:,.2f}".format(PLTotal))
print("Average Change in PL: " + "${:,.2f}".format(AvgPLchange))
print("Greatest monthly increase in profit: " + formattedmaxPLincrease)
print("Greatest monthly decrease in profit: " + formattedminPLincrease)

#and export to text file 
with open("BudgetAnalysis.txt", "w") as f:
    f.write("Financial Analysis:\n")
    f.write("-----------------------\n")
    f.write("Total Months: " + str(totalmonths) + "\n")
    f.write("Total Profit: " + "${:,.2f}".format(PLTotal) + "\n") 
    f.write("Average Change in PL: " + "${:,.2f}".format(AvgPLchange) + "\n")
    f.write("Greatest monthly increase in profit: " + formattedmaxPLincrease + "\n")
    f.write("Greatest monthly decrease in profit: " + formattedminPLincrease + "\n")
    f.close()


