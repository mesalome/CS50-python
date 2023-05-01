def main():
    mthDayYear = check()
    change(mthDayYear)


def check():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Write a date: ").strip()
        try:
            if date.count(",") != 0:
                x = date.replace(",", "")
                date_list = x.split(" ")
                for month in months:
                    if  date_list[0].lower()==month.lower():
                        month_number = months.index(month)+1
                        date_list[0] = str(month_number)
                if 1 <= int(date_list[1]) <= 31 and len(date_list[2])== 4 and date_list[2].isdigit():
                    return date_list
                else:
                    continue

            elif date.count("/") != 0:
                date_list = date.split("/")
                if 1 <= int(date_list[0]) <=12 and 1 <= int(date_list[1]) <= 31 and len(date_list[2])== 4 and date_list[2].isdigit():
                    return date_list
                else:
                    continue
                break
            else:
                continue
        except ValueError:
            pass


def change(mthDayYear):
    month = int(mthDayYear[0])
    day = int(mthDayYear[1])
    year = int(mthDayYear[2])
    print(year, '-', '%02d' % month, '-', '%02d' % day, sep='')

main()