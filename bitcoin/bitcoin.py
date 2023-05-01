import requests
import sys

    # if len(sys.argv) !=2:
    #     sys.exit()

def main():
    if len(sys.argv) !=2:
        sys.exit("Missing command-line argument")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = response.json()["bpi"]["USD"]["rate"]
        rate = rate.replace(",", "")
        userAmount = float(sys.argv[1])
        amount = float(rate)*userAmount
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not number")

if __name__ == "__main__":
    main()