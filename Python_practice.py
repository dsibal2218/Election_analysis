#what is the score?
score = int(input("whats your test score?"))
if score>=90:
    print("grade is A")
elif score>=80:
    print("grade is B")
elif score>=70:
    print("grade is C")
elif score>=60:
    print("grade is D")
else:
    print("your grade is F")
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
     