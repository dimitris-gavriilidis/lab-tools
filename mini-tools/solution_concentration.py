'''

A program that calculates the concentration in mg/mL of a solution

'''


def get_inputs():
    while True:
        try:
            mass = float(input("Enter mass of analyte in mg: "))
            volume = float(input("Enter volume of solution in mL: "))

        except ValueError:
            print("mass and volume should not be strings. Enter numbers")
            continue
        if mass <=0:
            print("mass should be greater than 0")
            continue
        elif volume <=0:
            print("volume should be greater than 0")
            continue

        return mass, volume


def concentration(mass, volume):
    conc = mass / volume
    return conc


def main():
    mass, volume = get_inputs()
    conc = concentration(mass,volume)
    print(f"The concentration is {conc:.2f} mg/mL")


main()
