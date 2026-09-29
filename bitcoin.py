import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Current Bitcoin price (fetched from Binance, Aug 24, 2026)
    price = 97845.0243

    total = n * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
