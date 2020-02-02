import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# total votes 
total_votes = 0

# list of candidates
candidate_options = []

# candidates votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
      total_votes += 1
      name = row[2]

      if name not in candidate_options:
        candidate_options.append(name)
        candidate_votes[name] = 0
    
      candidate_votes[name] += 1

    with open(file_to_save, "w") as txt_file:
      # Print the final vote count to the terminal.
      election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")

      # Save the final vote count to the text file.
      txt_file.write(election_results)

      for candidate in candidate_options:
          # get hte votes for each candidate
          votes = candidate_votes[candidate]
          # Calculate the percentage of votes.
          vote_percentage = int(votes) / int(total_votes) * 100
          
          candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)


          if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

      # summarizing the infomation about the winner
      winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

      # writting the infomation about the winner in the output file
      txt_file.write(winning_candidate_summary)
