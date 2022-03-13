#import the datetime class from the datetime module
import datetime as dt
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#print the present time
print("The time right now is", now)
#add our dependencies
import os
import csv
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # print the header row
    headers = next(file_reader)
    print(headers)

#the data we need to retrieve
#1. the total number of votes cast
#2 complete list of candidate whoe received votes
#3. The percentage of votes each candidate won
#4. The total number of vote each candidate won
#5. The winner of the election based on popular votes