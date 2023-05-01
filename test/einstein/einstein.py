def main():
    mass = int(input("Mass: "))
    jouls = energy(mass)
    print(jouls)

def energy(m):
    c = 300000000
    return m*c*c

main()