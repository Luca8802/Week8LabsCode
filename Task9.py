f = open("info.txt") #opening the text file

for line in f: #setting up a for loop to go through the file
    print(line) #using a print function to print out a line with each pass

f.close() #closing the file