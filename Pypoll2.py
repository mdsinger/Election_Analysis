# Add our dependencies
import csv
import os

# Assign a variable to the file to load and the path.
file_to_load = "Documents/U of U data analytics bootcamp/Class Folder/Election Analysis/Election_Analysis/Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Documents/U of U data analytics bootcamp/Class Folder/Election Analysis/Election_Analysis/analysis/election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Use the open statement to open the file as a text file.


with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
    
# Close the file

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare an empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
       
            # Track that candidate's vote
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate.
    
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.

    vote_percentage = float(votes) / float(total_votes) * 100

    # 4. Print the candidate name and percentage of votes.

    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

#  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.

     # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.



# Close File
election_data.close()


# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

