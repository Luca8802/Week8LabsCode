name = "Joe" #assigning the value to the variable "name". The value is a string
age = 80 #assigning a value to the variable called "age", this is an integer

print(f"{name:@^15} - {age:#^10}") #printing using the f -string
print("{:@^15} - {:#^10}".format(name, age)) #printing the same thing without the f string