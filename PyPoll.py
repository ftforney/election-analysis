# Data we need:
# 1. Total num of votes cast
# 2. Complete list of candidate who got votes
# 3. % of votes each candidate won
# 4. Total num of votes each candidate won
# 5. Winner of election based on popular vote

# For the challenge:
# 1. I need to get the voter turnout for each county.
# 2. I need to get the percentage of votes from each county out of the total count.
# 3. I need to get the county with the highest turnout.
# In order to complete this, take a look at how we managed to get the basic voting data.
# All we need to do is create a dictionary for a specified county, and the vote data.

import os
import csv
import datetime

#Defining variables we will need throughout the code here. Read is for the input file, Write is for the output file.
read = os.path.join("Resources","election_results.csv")
write = os.path.join("Analysis","election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
counties = []
county_vote_data = {}
highest_county = ""
highest_county_percentage = 0
highest_county_count = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Opening the data we want to read and looping through it, grabbing the candidate names and tallying their votes as we go through the whole file...
with open(read, 'r') as data:
    reader = csv.reader(data)
    headers = next(reader)
    for row in reader:
        candidate_name = row[2]
        county = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        if county not in counties:
            counties.append(county)
            county_vote_data[county] = 0
        candidate_votes[candidate_name] += 1
        county_vote_data[county] += 1
        total_votes += 1

#Opening the file we want to output to and writing the relevant data.
with open(write, 'w') as output:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    output.write(election_results)

    #Looping through our county_vote_data dictionary so we can grab each counties vote count, and get a percentage...
    for k,v in county_vote_data.items():
        c_votes = v
        c_vote_percentage = v/total_votes*100
        county_results = (f"{k}: {v/total_votes*100:.1f}% ({v:,})\n")
        print(county_results)
        output.write(county_results)
        if(c_votes>highest_county_count) and (c_vote_percentage>highest_county_percentage):
            highest_county_count = c_votes
            highest_county_percentage = c_vote_percentage
            highest_county = k
    highest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-------------------------\n")
    print(highest_county_summary)
    output.write(highest_county_summary)

    #Looping through our candidate_votes dictionary so we can grab their vote count, and calculate a percentage...
    for key, value in candidate_votes.items():
        votes=value
        vote_percentage = value / total_votes * 100
        candidate_results = (f"{key}: {value / total_votes * 100:.1f}% ({value:,})\n")
        print(candidate_results)
        output.write(candidate_results)
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = key
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    output.write(winning_candidate_summary)
