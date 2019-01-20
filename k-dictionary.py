# Dictionary with python
import json, os, time, random

data = json.load(open("data.json")) # Loads the json data file, data variable will be a python dictionary
os.system("cls")
# some text based fun animation for starting the program 
letters = ["|","||","|||","||||","|||||","||||||","|||||||","||||||||",]
# takes the array and return the items one by one, using next 
for next in letters:
    os.system("cls")
    print("Loading data ", next)
    time.sleep(0.30)

# Main loop 
time.sleep(1)
running = True
while running:
    #Cleans the screen and writes the header for program
    os.system("cls")
    print("*********** Dictionary v.1.0 By: KN ***********")
    print("Press Shift + q to terminate!")
    word = input("\nEnter your word: ") # Gets the input from user
    if word != "Q": # set a condition, as long as input is not Upper case Q, it runs the program
        count = 0
        for key,value in data.items(): # checks for input key and returns the value 
            if key == word:
                if len(value) > 1: #checks if value is a list! then asks for showing more answers
                    print("\nthere is more than one definition for your request")
                    print("--------------------------------------------------")
                    all = input("\nshow all of them? (Y/N): ")
                    print()
                    if all == "y".lower():
                        for next in value:
                            count += 1
                            print(count, " ",next)
                            print()
                            time.sleep(0.30)
                        print()
                        input("press a key to continue ")
                        print()
                    else: # if user doesnt want to see all definitions, it returns the first one 
                        print(value[0])
                        print()
                        input("press a key to continue ")
                        print()
                else: # if there is only one definition, print it 
                    print(value)
                    print()
                    input("press a key to continue ")
                    print()
    else: # if input is upper Q, terminates the while loop and exit the program
        print("bye")
        time.sleep(1)
        running = False
