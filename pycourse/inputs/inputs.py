
# The program below captures values from the user on command line and then checks the age type 
# if the type is not int then we do not process other wise we print the name and age. 

name = input("Enter your name: ")
age = input("Enter your age: ")
wage = input("Enter your hourly wage:")
hours = input("Enter your hours worked:")


if age.isdigit():  
    # isdigit will find out of the string is a digit or not 
    name = name.strip().title()
    """
        the strip() method will remove starting and ending spaces in the string you are processing. 
        The strip method will not remove spaces in between the characters. 
        the title() method will capitalize the first letters of the string. 
    """ 
    print(f"Name: {name}, Age: {int(age)} and Payable is: ${float(wage)*float(hours):.2f}")
else: 
    print(f"Age, wage or hours worked are not in the correct format.")