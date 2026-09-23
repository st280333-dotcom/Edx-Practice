import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                stripped = line.strip()

                if not stripped:
                    continue

                if stripped.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
