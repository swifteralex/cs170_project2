import copy


def k_fold_cross_validation(data, features):
    correct_count = 0
    for removed_row in data:
        shortest_distance, nearest_class = 999999999.9, 1.0
        for comparison_row in data:
            if removed_row != comparison_row:
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
    num_features = len(data[0]) - 1
    algorithm = input("\nType the number of the search algorithm you'd like to use:\n"
                      " 1) Forward Selection\n"
                      " 2) Backward Elimination\n")
    print("\nThis dataset has " + str(num_features) + " features with " + str(len(data)) + " instances.")
    print("\nBeginning search...\n")

    best_set_overall = []
    best_accuracy_overall = 0.5
    if algorithm == '1':
        current_set = []
        unused_features = [number + 1 for number in range(num_features)]
        while len(unused_features) > 0:
            best_feature, best_accuracy = 0, 0
            for feature in unused_features:
                current_set.append(feature)
                accuracy = k_fold_cross_validation(data, current_set)
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_feature = feature
                if accuracy > best_accuracy_overall:
                    best_accuracy_overall = accuracy
                    best_set_overall = copy.deepcopy(current_set)
                print("    Using feature set " + str(current_set) + " gives an accuracy of " + str(accuracy) + ".")
                current_set.pop()
            unused_features.remove(best_feature)
            current_set.append(best_feature)
            print("\nFeature set " + str(current_set) + " was best with an accuracy of " + str(best_accuracy) + ".\n")
    elif algorithm == '2':
        current_set = [number + 1 for number in range(num_features)]
        best_set_overall = [number + 1 for number in range(num_features)]

        accuracy = k_fold_cross_validation(data, current_set)
        print("    Using feature set " + str(current_set) + " gives an accuracy of " + str(accuracy) + ".")
        print("\nFeature set " + str(current_set) + " was best with an accuracy of " + str(accuracy) + ".\n")

        while len(current_set) > 1:
            best_feature, best_accuracy = 0, 0
            current_set_copy = copy.deepcopy(current_set)
            for feature in current_set_copy:
                current_set.remove(feature)
                accuracy = k_fold_cross_validation(data, current_set)
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_feature = feature
                if accuracy > best_accuracy_overall:
                    best_accuracy_overall = accuracy
                    best_set_overall = copy.deepcopy(current_set)
                print("    Using feature set " + str(current_set) + " gives an accuracy of " + str(accuracy) + ".")
                current_set.append(feature)
            current_set.remove(best_feature)
            print("\nFeature set " + str(current_set) + " was best with an accuracy of " + str(best_accuracy) + ".\n")

    print("Finished search! The best set of features found was " +
          str(best_set_overall) + " with an accuracy of " + str(best_accuracy_overall) + ".")


if __name__ == "__main__":
    main()
