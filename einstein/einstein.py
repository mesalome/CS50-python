# asks mass and prints energy
def main ():
     m = input("m: ")
     print(energy(m))


#calculates energy
def energy(m):
    e = int(m) * pow(300000000, 2)
    return e

main()