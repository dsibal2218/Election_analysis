#add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
#declare the candidate list
candidate_options = []
# Declare the empty dictionary for votes
candidate_votes = {}
#initialize county list
county_options = []
#initialize county dictionary
county_votes = {}
#initilize empty string that will hold county names
winning_county = ""
#Initialize a variable for county number of votes
winning_county_count = 0
winning_percentage_county = 0
# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes+= 1
        #print the candidate name for each row
        candidate_name=row[2]
        # If the candidate does not match any existing candidate, add it to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 
        #Add a vote tot he candidate's count
        candidate_votes[candidate_name] +=1
        
        #print the county name for each row
        county_name = row[1]
        if county_name not in county_options:
           #add the county name to the county list
            county_options.append(county_name)
            #begin tracking that county's vote count/initilize to zero
            county_votes[county_name] = 0
        #add a vote to the county's count
        county_votes[county_name] +=1
        
#save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count of a candidate.
        votes_per_county = county_votes[county_name]
        # Calculate the percentage of votes
        votes_percentage_county = float(votes_per_county) / float(total_votes) * 100
        #  Print out each county's name, vote count, and percentage of
        #  votes to the terminal.
        county_results = (
            f"{county_name}: {votes_percentage_county:.1f}% ({votes_per_county:,})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

        # Determine winning vote count and county
        # Determine if the votes is greater than the winning count.
        if (votes_per_county > winning_county_count) and (votes_percentage_county > winning_percentage_county):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_county_count = votes_per_county
            winning_percentage_county = votes_percentage_county
            # And, set the winning_county equal to the county's name.
            winning_county = county_name
    # Print out the winning county, vote count and percentage to
    # terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
# Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #  Print out each candidate's name, vote count, and percentage of
        #  votes to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # Print out the winning candidate, vote count and percentage to
    # terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)  
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)