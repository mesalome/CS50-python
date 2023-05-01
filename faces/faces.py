def main():
    n = input("Make smiley or sad face\n")
    print (convert(n))


def convert(txt):
    txt = txt.replace(":)", "🙂")
    txt = txt.replace(":(", "🙁")
    return txt




main()