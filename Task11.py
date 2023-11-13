with open("info.txt") as f: #using the with statement as well as the open function to wrap the file while we access it
    for lines in f: #using a for loop to go through the file line by line
        print(lines) #using a print function to print out each individual line that the for loop goes through