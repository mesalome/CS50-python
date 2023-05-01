def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # return float(d.removeprefix("$"))
    return float(d[1:]) #whole string from the second character to the rest
    # return float(d.replace("$", ""))



def percent_to_float(p):
    # return float(p.removesuffix("%"))/100
    return float(p[:-1])/100 # whole string without the last character
    # return float(p.replace("%", ""))/100


main()