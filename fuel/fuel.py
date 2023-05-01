class IrregularFraction(Exception):
    "Raised when input fraction is irregular"
    pass



def main():
    output(fraction())


def fraction():
    while True:
        try:
            fuel = input("Fraction: ")
            fuel_fraction = list(fuel.split("/"))
            numerator = int(fuel_fraction[0])
            denominator = int(fuel_fraction[1])
            if numerator>denominator:
                raise IrregularFraction
            else:
                fraction = int(numerator)/int(denominator)
                return fraction
        except (ValueError, ZeroDivisionError, IrregularFraction):
            pass
        else:
            break

def output(fraction):
    percent = fraction*100
    if percent >= 99:
        print("F")
    elif percent <= 1:
         print("E")
    else:
        print (f"{round(percent)}%")



main()