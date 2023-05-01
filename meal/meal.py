def main():
    this_moment= input("What time is it now?\n")
    this_moment = convert(this_moment)
    meal_time(this_moment)


def convert(time):
    if time.endswith('a.m.'):
        time = time.removesuffix('a.m.')
        time = time.split(":")
        hours = float(time[0])
    elif time.endswith('p.m.'):
        time = time.removesuffix('p.m.')
        time = time.split(":")
        hours = float(time[0])%12 + 12
    else:
        time = time.split(":")
        hours = float(time[0])

    minutes = float(time[1])/60
    time = hours+minutes
    return time

def meal_time(time):
    if time >=7 and time <8:
        print("Breakfast time")
    elif time >=12 and time<=13:
        print("Lunch time")
    elif time >=18 and time<19:
        print("Dinner time")
    else: None

if __name__== "__main__":
    main()