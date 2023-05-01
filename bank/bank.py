def main():
    greeting_fine(input("How where you greeted with?\n"))



def greeting_fine(greeting):
    if greeting.strip().casefold().startswith("hello"):
        print("$0")
    elif greeting.strip().casefold().startswith("h"):
        print("$20")
    else:
        print ("$100")



main()