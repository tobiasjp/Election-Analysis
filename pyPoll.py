# 1. The data we need to retrieve.
# Add our dependancies
import csv
import os

# assign a variable to the file path for csv file
electionresults = os.path.join("Election-Analysis", "election_results.csv")

# assign a variable to save the file to a path.
electionsummary = os.path.join("Election-Analysis/analysis", "election_summary.txt")

# Initialize a total vote counter (must be initialized to 0)
total_votes = 0
# initialize a candidate options lists
candidate_options = []
# Create a dictionary
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(electionresults) as election_data:
#     print(election_data)
# To do: read and analyze the data here.
# read the file with the reader function
    file_reader = csv.reader(election_data)


    #Read the header row:
    headers = next(file_reader)
    # print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        #adds to the total vote count
        total_votes += 1

        # Print the total votes
        # print(total_votes)

        #Print the candidate name from each row
        candidate_name = row[2]

        # print each row
        # print(row) 

         #if the candidates name does not match
        if candidate_name not in candidate_options:


        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

        #Begin tracking that candidate's votes
            candidate_votes[candidate_name]= 0
        #add a vote to each candidate's names
        candidate_votes[candidate_name] += 1 


with open(electionsummary, "w") as txt_file:

    election_results = (
        f"Election Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")
    
    print(election_results, end= "")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentages = float(votes) / float(total_votes) * 100
            #print(f"{candidate_name}: received {vote_percentages:.2f}% of the vote.")

        candidateresults = (f"{candidate_name}: {vote_percentages:.1f}% ({votes:,})\n")
        
        print(candidateresults)

        txt_file.write(candidateresults)
        # print the candidate list
        # print(candidate_options)
        # print candidate votes
        # print (candidate_votes)

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
            # print(f"{candidate_name}: {vote_percentages:.1f}% ({votes:,})\n")

            #Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentages > winning_percentage):
                #if true then set wining count = votes and winning percent =
                #vote_percentage.

            winning_count = votes
            winning_percentage = vote_percentages

            winning_candidate = candidate_name
            

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
        


    




































# outfile = open(electionsummary, "w")
# outfile.write("Hello World")
# outfile.close()

#with open(electionsummary,"w") as txtfile:
    #txtfile.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")



#print(txtfile)



# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

