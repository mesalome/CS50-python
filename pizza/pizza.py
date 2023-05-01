import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                table = []
                headers = []
                i=0
                cvsFile = csv.reader(file)
                for row in cvsFile:
                    if i==0:
                        headers = row
                        i+=1
                    else:
                        table.append(row)
            print(headers)
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            sys.exit("non-csv file was passed")


except FileNotFoundError:
    sys.exit("File does not exist")