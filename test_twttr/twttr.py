def main():
    txt  = str(input())
    onlyCons= shorten(txt)
    print(onlyCons)

def shorten(str):
    str_into_list = list(str.strip(" "))

    for index in range(len(str_into_list)):
        for j in ["a", "e", "i", "o", "u",  "A", "E", "I", "O", "U"]:
            if str_into_list[index] == j:
                str_into_list[index]= ""
            else: pass

    result = "".join(str_into_list)
    return result

if __name__ == "__main__":
    main()