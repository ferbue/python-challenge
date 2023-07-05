import csv

# Define the file paths
input_file = "Resources/election_data.csv"
output_file = "election_results.txt"

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # Add the candidate to the list of candidates if not already present
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Increment the vote count for the candidate
        candidate_votes[candidate_name] += 1

# Calculate the percentage of votes and find the winner
winner = ""
max_votes = 0

# Create the analysis output string
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100

    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the analysis to the terminal
print(output)

# Export the analysis to a text file
with open(output_file, "w") as txtfile:
    txtfile.write(output)

print("Analysis exported to 'election_results.txt' file.")

