import time  # Importing Module
password=2026  # Right password
n=0           # Iteration number start count
ss=int(input("Enter the password:"))  # User input
while ss!= password:  # Loop check
  n+=1                # Iteration number increment
  if n>=3:         # Check. So that th code allows only 3 tries to the user
    print("The system is locked now!!❌🔒") #Locking if all 3 tries are used up
    break            # Code ends
  else:               # When tries are still left
    print("Incorrect possword entered!❌ Please wait for 5 seconds.")
    for i in range (1,6):# Timer loop
      print(i)
      time.sleep(1)
    ss=int(input("Enter the password:")) # Input request ater timer ends
else:
  print("Access granted!✅") # Password entered is right and system is unlocked