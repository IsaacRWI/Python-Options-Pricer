from blackScholesCalc import BlackScholesCalc

while True:
    selection = input("""Please select options pricing model:
    1. Black Scholes Model
    Selection: """)
    match selection:
        case "1":
            print("Black Scholes")
        case _:
            print("no matches")
