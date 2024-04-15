print("Welcome to my computer quiz.")

playin = input("do you want to play? ").lower()
if playin != "yes":
    quit()
print("Oaky! let's play :)")
score = 0
answer = input("What is cpu stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who is the Father of the Computer? ").lower()
if answer == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("How much is a byte equal to? ").lower()
if answer == "8 bits":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is also known as a portable computer? ").lower()
if answer == "laptop":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What do you need to use to connect to the internet? ").lower()
if answer == "modem":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which key of the keyboard is mainly used to cancel the program? ").lower()
if answer == "esc key":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print (f"You score {score} out of 6 ")
print (f"You got {str(score / 4)*100}% ")