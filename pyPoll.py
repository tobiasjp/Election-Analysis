# 1. The data we need to retrieve.
# Add our dependancies
import csv
import os

# assign a variable to the file path for csv file
electionresults = os.path.join("election-analysis", "election_results.csv")

# assign a variable to save the file to a path.
electionsummary = os.path.join("analysis", "election_summary.txt")


# Open the election results and read the file.
with open(electionresults) as election_data:
#     print(election_data)
# To do: read and analyze the data here.
# read the file with the reader function
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    # for row in file_reader:
    #     print(row) 
# Print the header row:
    headers = next(file_reader)
    print(headers)

    


# outfile = open(electionsummary, "w")
# outfile.write("Hello World")
# outfile.close()

#with open(electionsummary,"w") as txtfile:
    #txtfile.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")



#print(txtfile)



# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winnder of the election based on popular vote.
