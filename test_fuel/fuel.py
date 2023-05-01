import math

def main():
    userInput = input("Input fuel ratio: ")
    percent = convert(userInput)
    print(gauge(percent))


def convert(strFraction):
     # parameter is str "X/Y"
    try:
        fuel_fraction_values = list(strFraction.split("/"))
        numerator, denominator = int(fuel_fraction_values[0]), int(fuel_fraction_values[1])
    except ValueError:
        raise

    try:
        if denominator == 0:
            raise ZeroDivisionError
        elif numerator>denominator:
            raise ValueError
        else:
            percent = numerator/denominator*100
            return myround(percent)
    except (ZeroDivisionError, ValueError):
        raise

def gauge(percent):
    if percent >= 99:
        return("F")
    elif percent <= 1:
         return("E")
    else:
        return (f"{percent}%")

def myround(n):
    nTimes10intoInt = int(n * 10)
    #this will determine first number after whole number
    if nTimes10intoInt % 10 >= 5:
        return math.ceil(n)
    return math.floor(n)


if __name__ == "__main__":
    main()