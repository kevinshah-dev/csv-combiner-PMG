# CODED BY KEVIN SHAH - PMG GRADUATE LEADERSHIP PROGRAM CANDIDATE
# EMAIL: ks539@duke.edu

import os
import sys
import pandas as pd

#Change path variable depending on where the csv-combiner is located. 
path = "/home/runner/CSV-Combiner/csv-combiner/"

#Checks the arguments to see if there are at least two CSV files passed
if len(sys.argv) < 2:
  print("This program requires at least two CSV files to work! Please try again. Add CSV files to the fixtures folder.")
  quit()

filesList = []
csvList = []

# Appends all of the terminal arguments into a list called filesList. This list contains the file paths of all the CSV files to be merged
for i in range(1, len(sys.argv)):
  filesList.append(path+"fixtures/"+sys.argv[i])

#Appends all of the CSV files to a list called csvList. This list is a list of pandas dataframes (created using the .read_csv function). The code also adds a new column named filename to all of the CSV inputs
for file in filesList:
    csvList.append(pd.read_csv(file).assign(filename = os.path.basename(file)))

# pd.concat merges the CSV files located in csvList and places the dataframe in
# the variable csv_merged
csv_merged = pd.concat(csvList, ignore_index=True)

#This line passes the merged pandas dataframes to the .to_csv function. This function turns the dataframe into a csv file. The csv file is saved in the csv-combiner folder.
csv_merged.to_csv(path + 'combined.csv', index=False)

print("The merged CSV (combined.csv) can be found in the csv-combiner folder")

#UNIT TESTS

#TEST 1
# Input into terminal: python3 csv-combiner.py
# Output: This program requires at least two CSV files to work! Please try again. Add CSV files to the fixtures folder.

#TEST 2
# Input into terminal: python3 csv-combiner.py accessories.csv
# Output: This program requires at least two CSV files to work! Please try again. Add CSV files to the fixtures folder.

#TEST 3 (Output of this test is under the Unit Test Outputs folder as test3.csv)
# Input into terminal: python3 csv-combiner.py accessories.csv clothing.csv
# Output: The merged CSV (combined.csv) can be found in the csv-combiner folder

#TEST 4 (Output of this test is under the Unit Test Outputs folder as test4.csv)
# Input into terminal: python3 csv-combiner.py accessories.csv clothing.csv household_cleaners.csv
# Output: The merged CSV (combined.csv) can be found in the csv-combiner folder









