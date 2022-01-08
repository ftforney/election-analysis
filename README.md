# election-analysis
Python is going to be used during this project to analyze the results of various ballots for election purposes.

## Project Overview
An employee from the Colorado Board of Elections has given us the tasks listed below to perform an election audit of a recent local congressional election.

1. Calculate total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate total number of votes each candidate received.
4. Calculate percentage of votes each candidate won.
5. Determine the winner of election based on popular vote.

Furthermore, the board itself has requested that we collect the number of votes each county had.

## Results
Here is the data we got from the election:
- 369,711 votes in total were cast.
- Here are the vote counts for the following counties:
  - Jefferson: 10.5% (38,855 votes)
  - Denver: 82.8% (306,055 votes)
  - Arapahoe: 6.7% (24,801 votes)
- Denver had the largest county turnout.
- The candidates were as follows:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doane
- And the results are as follows:
  - Charles Casper Stockham with 23.0% of the votes. (85,213 votes)
  - Diana DeGette with 73.8% of the votes. (272,892 votes)
  - Raymon Anthony Doane with 3.1% of the votes. (11,606 votes)
- The winner of the election was:
  - Diana DeGette, who got 73.8% of the votes, which is 272,892 votes!

## Summary

This code was able to automatically go though the provided datafile to calculate the amount of votes each candidate got, see the vote count of various counties, and calculate a percentage for both of these. There was no effort needed to analyze the data, and this is a great tool for performing an election audit in the future!

The code can be easily modified to obtain other results. For example, if the party the candidate was in the dataset, we can grab that and display that. If we had the data for the type of vote used, we would be able to see the count of mail-in ballots, electronic votes, and punch card votes.

## Some Code Review

For the challenge, I opted to use the following for loop:
```py
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
```

I found it easier to use this type of loop to grab my keys and values since I don't need to do any extra work to obtain the value of a key I want, it's already there to be used.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Atom 1.58.0
