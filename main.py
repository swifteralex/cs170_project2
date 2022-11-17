def main():
    filename = input("Type in the name of the file to test:\n")
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append([float(number) for number in line.split()])

    algorithm = input("\nType the number of the search algorithm you'd like to use:\n"
                      " 1) Forward Selection\n"
                      " 2) Backward Elimination\n")

    print("\nThis dataset has " + str(len(data[0]) - 1) + " features with " + str(len(data)) + " instances.")


if __name__ == "__main__":
    main()
