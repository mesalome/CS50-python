import sys
import csv


try:
    if len(sys.argv) != 3:
        if len(sys.argv)<3:
            sys.exit("Too few arguments")
        else:
            sys.exit("Too many arguments")
    else:
        with open(sys.argv[1]) as before_file:
            before_data = csv.DictReader(before_file)
            with open(sys.argv[2], 'w', newline='') as after_file:
                writer = csv.DictWriter(after_file, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in before_data:
                    fullName, house = row['name'], row['house']
                    surname, name = fullName.strip().split(",")
                    name = name.strip()
                    surname = surname.strip()
                    writer.writerow({'first': name, 'last': surname, 'house': house})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")