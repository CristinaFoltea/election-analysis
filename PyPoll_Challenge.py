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

# list of counties
counties_options = []

# candidates votes
candidate_votes = {}

# counties votes
counties_votes = {}

# county with the largest turnout
largest_turnout_county = ""
largest_turnout_county_votes = 0
largest_turnout_county_vote_percentage = 0

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
      county = row[1]

      # write the candidate data
      if name not in candidate_options:
        candidate_options.append(name)
        candidate_votes[name] = 0

      # write the county data
      if county not in counties_options:
        counties_options.append(county)
        counties_votes[county] = 0

      counties_votes[county] += 1
      candidate_votes[name] += 1

    with open(file_to_save, "w") as txt_file:

      # Get the formated election result
      election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")

      # Print total votes to the terminal
      print(election_results)

      # Save the final vote count to the text file.
      txt_file.write(election_results)

      # add a header for the candidate data
      candidate_header = "\nCandidate election data:\n"
      print(candidate_header)
      txt_file.write(candidate_header)

      for candidate in candidate_options:
        # total votes for each candidate
        votes = candidate_votes[candidate]
        # Candidate percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Format the candidate result
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # print the result summary to the terminal
        print(candidate_results)

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

      # print candidate election results summary
      print(winning_candidate_summary)

      # writting the infomation about the winner in the output file
      txt_file.write(winning_candidate_summary)


      # add a header for the county data
      county_header = "\nCounty election data:\n"
      print(county_header)
      txt_file.write(county_header)

      for county in counties_options:
        # total votes per county
        county_votes = counties_votes[county]
        # County vote turnout percentage
        county_vote_percentage = int(county_votes) / int(total_votes) * 100
        # Format the county analysis result 
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        # save county infomation to the output file
        txt_file.write(county_results)

        if county_votes > largest_turnout_county_votes:
          largest_turnout_county = county
          largest_turnout_county_votes = county_votes
          largest_turnout_county_vote_percentage = county_vote_percentage

      # largest country turnout summary
      largest_turnout_county_summary = (
      f"-------------------------\n"
      f"County with the largest turnout is: {largest_turnout_county}\n"
      f"{largest_turnout_county}'s number of votes: {largest_turnout_county_votes:,}\n"
      f"{largest_turnout_county}'s vote percentage: {largest_turnout_county_vote_percentage:.1f}%\n"
      f"-------------------------\n")

      # print county with the largest turnout summary infomation
      print(largest_turnout_county_summary)

      # save the data of the county with the largest turnout
      txt_file.write(largest_turnout_county_summary)