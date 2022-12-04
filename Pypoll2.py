
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


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    file_reader = csv.reader(election_data)

   


# Close File
election_data.close()


# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

