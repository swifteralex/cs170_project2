def k_fold_cross_validation(data, features):
    correct_count = 0

    for removed_row in data:
        shortest_distance = 999999999.9
        nearest_class = 1
        for comparison_row in data:
            if removed_row == comparison_row:
                continue

            distance = 0
            for feature in features:
                distance += (removed_row[feature] - comparison_row[feature]) ** 2
            distance = distance ** 0.5
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_class = comparison_row[0]

        if abs(nearest_class - removed_row[0]) < 0.0001:
            correct_count += 1

    return correct_count / len(data)


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

    print(k_fold_cross_validation(data, [18, 25, 34]))


if __name__ == "__main__":
    main()
