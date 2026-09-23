import sys
import csv
from tabulate import tabulate

def main():
    # Check for exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # Ensure the file ends with .csv
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        # Read the CSV file
        with open(filename, "r") as file:
            reader = csv.reader(file)
            # Convert to list for tabulate
            table = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print table using tabulate in grid format
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
