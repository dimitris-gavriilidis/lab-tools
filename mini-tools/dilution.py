'''

A program that calculates the volume of stock solution needed using C1V1 = C2V2 →

c1 = stock_conc
v1 = stock_vol
c2 = final_conc
v2 = final_vol

V1 = C2*V2/C1
stock_vol = final_conc * final_vol / stock_conc

diluent_vol = v2 - v1
diluent_vol = final_vol - stock_vol

'''


def get_input():
    while True:
        try:
            stock_conc = float(input("Enter stock concentration: "))
            final_conc = float(input("Enter final concentration: "))
            final_vol = float(input("Enter final volume: "))

        except ValueError:
            print("Type numbers")
            continue

        if stock_conc <= 0:
            print("Enter stock concentration >0")
            continue
        elif final_conc <= 0:
            print("Enter final concentration >0")
            continue
        elif final_conc >= stock_conc:
            print("Final concentration should be less than stock concentration")
            continue
        elif final_vol <= 0:
            print("Enter final volume >0")
            continue

        return stock_conc, final_conc, final_vol


def calculate(stock_conc, final_conc, final_vol):
    # volume from stock
    stock_vol = final_conc * final_vol / stock_conc
    # volume of water to dilute the stock: final volume - stock volume
    diluent_vol = final_vol - stock_vol
    return stock_vol, diluent_vol


def main():
    stock_conc, final_conc, final_vol = get_input()
    stock_vol, diluent_vol = calculate(stock_conc, final_conc, final_vol)
    print(f"Mix {stock_vol:.2f} mL of stock solution with {diluent_vol:.2f} mL water")


main()