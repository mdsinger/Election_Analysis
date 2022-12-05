# Add our dependencies
import csv
import os

# Assign a variable to the file to load and the path.
file_to_load = "Documents/Bootcamp/Class Folder/Election Analysis/Election_Analysis/Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file.
file_to_save = "Documents/Bootcamp/Class Folder/Election Analysis/Election_Analysis/analysis/election_analysis.txt"

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Use the open statement to open the file as a text file.


with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
    
# Close the file

# Initialize a total vote counter.

    total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout.
largest_county = ""
county_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        #Extract the county name from each row.
        county = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Check to see if county in in county list.
        if county not in counties:

            #Add the county to the list.
            counties.append(county)


            # Begin tracking the county's vote count.
            county_votes[county] = 0


        # Add a vote to that county's vote count.
        county_votes[county] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Get the county from the county dictionary.
    for county in counties:

        #Retrieve the county vote count.
        cvotes = county_votes.get(county)

        #Calculate the percentage of votes for the county.
        county_percentage = float(cvotes)/float(total_votes) * 100

        county_results = (f"{county}: {county_percentage:.1f}% ({cvotes:,})\n")


         #Print the county results to the terminal.
        print(county_results) 

         #Save the county votes to a text file.
        txt_file.write(county_results)

         # Determine the winning county and get its vote count.
        if cvotes > county_turnout:
            county_turnout = cvotes
            largest_county = county

    # Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

