
def main():
    size_input = input("Enter the size of the pattern: ")
    size = int(size_input)

    row = 0
    while row < size:
        # Print '*' characters for the current row without moving to a new line
        for _ in range(size):
            print("*", end="")
        # Move to the next line after completing the row
        print()
        row += 1

if __name__ == "__main__":
    main()