def main():
    userList = grocery_list()
    ordered_list(userList)

def grocery_list():
    userList = {}
    while True:
        try:
            userInput = input().upper()
            searchGrocery = userList.get(userInput)
            if searchGrocery is not None:
                userList[userInput] += 1
            else:
                userList[userInput] = 1
        except (EOFError, KeyError):
            break
    return userList



def ordered_list(originalList):
        orderedList = sorted(originalList.items())
        for i in range(len(orderedList)):
             print(f"{orderedList[i][1]} {orderedList[i][0]}")

main()