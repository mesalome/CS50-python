import sys
try:
    if len(sys.argv) == 1:
        sys.exit("Too few command - line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command - line arguments")
    else:
        fileName = sys.argv[1].strip()
        if fileName.endswith(".py") != True:
            sys.exit("Not a Python file")
        else:
            with open(sys.argv[1]) as file:
                count = 0
                for line in file:
                    line = line.strip()
                    if line.strip() == '':
                        pass
                    elif line.strip()[0] != "#":
                        count +=1

        print("total lines", count)
except FileNotFoundError:
    print("File doesn't exist")