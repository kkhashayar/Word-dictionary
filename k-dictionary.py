import json, os, time, random, winsound
import difflib
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

# some text based fun animation for starting the program
letters = ["|","||","|||","||||","|||||","||||||","|||||||","||||||||",]
# takes the array and return the items one by one, using next
for next in letters:
    os.system("cls")
    print("Loading data ", next)
    time.sleep(0.30)
winsound.Beep(1000, 500)

data = json.load(open("data.json"))
def main():
    running = True
    while running:
        os.system("cls")
        print("*********** Dictionary v.1.0 By: KN ***********")
        print("Press Shift + q to terminate!")
        count = 0
        word = input("\nEnter your word: ")
        if word != "q".upper():
            word = word.lower()
            if word in data:
                for key,val in data.items():
                    if key == word:
                        if len(val) > 1:
                            print("There are more than one definition for your request, ")
                            print()
                            see_all = input("Display all? (Y/N): ")
                            print()
                            if see_all == "y".lower():
                                for next in val:
                                    count += 1
                                    time.sleep(0.20)
                                    print(count,"- " ,next)
                        else:
                            print(val)
                input("\nPress a key to continue..")
            else:
                matches = gcm(word, data.keys(), cutoff = 0.8)
                if len(matches) == 0:
                    print("No match found")
                    time.sleep(1)
                else:
                    print(matches)
                    word = input("select your word from the list: ")
                    for key,val in data.items():
                        if key == word:
                            if len(val) > 1:
                                print("There are more than one definition for your request, ")
                                print()
                                see_all = input("Display all? (Y/N): ")
                                print()
                                if see_all == "y".lower():
                                    for next in val:
                                        count += 1
                                        time.sleep(0.20)
                                        print(count,"- " ,next)
                            else:
                                print(val)
                    input("\nPress a key to continue..")
        else:
            print("Bye...")
            time.sleep(2)
            winsound.Beep(1000, 250)
            winsound.Beep(500, 250)
            running = False

if __name__ == "__main__":
    main()
