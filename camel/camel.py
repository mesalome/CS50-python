name = input("Please input name: ")

i = 0
upper_case=[]
if name.islower():
    print(name)
else:
    for n in name:
        if n.isupper():
            upper_case.append("_")
            upper_case.append(n.lower())
        else:
            upper_case.append(n)
            i = i+1
    print(''.join(upper_case))