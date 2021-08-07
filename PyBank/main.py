# import os and create file path
import os 
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

#open and read the csv file
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile)