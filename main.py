def main():
    f = open("CS170_Small_Data__97.txt", "r")
    print([float(number) for number in f.readline().split()])


if __name__ == "__main__":
    main()
