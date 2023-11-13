name = "Joe" #assigning the value to the variable "name". The value is a string
age = 80 #assigning a value to the variable called "age", this is an integer

print(f"{name:15} - {age:10}")  #using an f-string and the print function to display the name and age
print(f"{name:<15} - {age:10}") #using an f-string and the print function to display the name to the left and the age
print(f"{name:>15} - {age:10}") #using an f-string and the print function to display the right to the right and the age
print(f"{name:^15} - {age:/=10}") #using an f-string and the print function to display the name in the middle and the age with the padding of a '/'
