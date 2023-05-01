def main():
    user_input = input("Please type your text: ")
    output = convert(user_input)
    print(output)

def convert(txt):
    txt = txt.replace(":)", "🙂")
    txt = txt.replace(":(", "🙁")
    return txt

main()
