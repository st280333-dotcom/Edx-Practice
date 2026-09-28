from fractions import Fraction

def main():
    while True:
        try:
            # Take input as fraction (e.g., 3/4)
            frac = Fraction(input("Fraction: "))

            # Reject invalid inputs: negative or > 1
            if 0 <= frac <= 1:
                break
        except (ValueError, ZeroDivisionError):
            pass

    # Convert fraction to percentage
    percent = int(frac * 100)

    # Output rules
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

if __name__ == "__main__":
    main()

