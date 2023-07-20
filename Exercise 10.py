# Unit Testing Exercise

#Create a Python file which does the following:

# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Reads and displays the names of the 1st and 4th team in the file.

with open ("teams.txt", "w") as file:
    for n in ["Manteam", "Ball Blockers", "Foot Flingers", "Goal Grinders", "Score Slingers"]:
        newline = n + "\n"
        file.write(newline)
    

file.close

file = open ("teams.txt", "r")

files = file.readline 

#print(files[0], files[3])


