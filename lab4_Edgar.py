# Edgar Jimenez | Lab 4 | Intro to Python

# Ticket 1

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f"{age} - Access granted ✅")
    else:
        print(f"{age} - Too young ❌")
        # 17 Access Granted
        # 11 Access Denied
        # 25 Access Granted
        # 13 Access Granted
        # 9 Access Denied

# Ticket 2

# Set up a control variable
keep_checking = "yes"

#while keep_checking == "yes":
 # Ask the user to enter an age
 #age = int(input("Please enter the age to check:"))

 # Check if age is 13 or older and print the result
 #if age >= 13:
   # print("Access granted: They are 13 or older")
 #else:
  #  print("Access denied: They are too young.")
    # Ask if they want to check another age
    # Store their answer in keep_checking
#keep_checking = input ("Do you want to check another age? (type 'yes' to continue): ").lower()
# a while is better option because loop is for pre determined number to loop

#TICKET 3

while True:
   # Ask the user: enter an age or type 'stop'
   user_input = input("Enter an age or type 'stop' : ")
   # If they typed "stop", break out of the loop
   if user_input.lower() == 'stop':
      print("Exiting age checker. Goodbye!")
      break
   
   # Convert the string to a number for comparison
   age = int(user_input)
   # Check the age and print the result
   if age >= 18:
      print("You are an adult")
   else:
      print("You are a minor")

      # the difference is how it notifies you whether you are a minor or not and you can exit the system.

# Ticket 4
# Define the function to check if age is 13 or older
def can_access(age):
   if age >= 13:
      return True
   else:
      
      return False
   
# List of ages from Ticket 1
ages = [17, 11, 25, 13, 9]


# Loop through the list and check access using the function
for age in ages:
   if can_access(age):
      print(f"{age} — Access granted ✅")
else:
      print(f"{age} — Too young ❌")

# the difference is how we are delegating to the "can access" function 
# putting the check inside the function makes it easier in terms of where the changes can be made if needed as well as how clean the code looks.

#Ticket 5

def can_access(age):
    """Checks if a person meets the minimum age requirement of 13."""
    return age >= 13
def signup_report(ages):
    """Prints a formatted signup report and counts approved users."""
    print("--- StreamPass Signup Report ---")
    approved = 0
    total = len(ages)

    for index, age in enumerate (ages, start=1) :
     if can_access(age):
        print(f"Signup #{index} Age {age} - Access granted ✅")
        approved += 1
    else:
       print(f"Signup #{index} Age {age} - Too Young ❌")

    print(f"Approved: {approved} out of {total}")
# Given list of signups
signups = [22, 10, 15, 8, 19, 13]
# Call the function
signup_report(signups)
# I predict that only 4 out of the 6 will be granted 
# I used funcions for "Can access", Conditionals for if/else, loops for the sequence of ages and going through them one by one, I used variables and f srings {}, I also used parameters and arguements.
