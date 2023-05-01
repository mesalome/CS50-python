def main():
    check_answer (input("What is the answer to the Great Question of Life? \n"))



def check_answer(ans):
    ans = ans.strip()
    if ans == "42"  or ans.casefold() == "forty-two" or ans.casefold() == "forty two":
        print("Yes")
    else:
        print("No")



main()