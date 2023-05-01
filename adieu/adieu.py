import inflect

def main():
    p = inflect.engine()
    myList = []

    while True:
        try:
            user_input = input()
            myList.append(user_input)
        except EOFError:
            break
    joinedList = p.join(myList)
    print ("Adieu, adieu, to", joinedList)

main()