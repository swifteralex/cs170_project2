def main():
    filename = input("Type in the name of the file to test: ")
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append([float(number) for number in line.split()])
    print(data)


if __name__ == "__main__":
    main()
