import random
import sys

def main():
    n = get_level()
    if n == 1:
        guessingNumber = 1
    else:
        myList = range(1, n)
        guessingNumber = random.choice(myList)
    print(guessingNumber)
    while True:
        try:
            userInput = int(input("Guess: ").strip())
            if userInput <= 0 or userInput > n:
                pass
            elif userInput > guessingNumber:
                print("Too large!")
                continue
            elif userInput < guessingNumber:
                print("Too small!")
                continue
            elif userInput == guessingNumber:
                sys.exit("Just right!")

        except ValueError:
            pass

def get_level():
     while True:
        try:
            n = int(input("Level: ").strip())
            if n<=0:
                pass
            else:
                return n
        except ValueError:
            pass
main()
