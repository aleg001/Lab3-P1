import json


def NodeSelect():
    print("\nSelect node from list ")
    file_name = input("Enter the file name (without txt extension): ")
    file_name_with_extension = file_name + ".txt"

    try:
        with open(file_name_with_extension, "r") as file:
            data = json.load(file)

        data = data["config"]

        while True:
            print("\nSelect node from list: ")
            keys = list(value for key, value in data.items())
            for i, key in enumerate(keys):
                print(f"{i + 1}. {key}")

            try:
                node = int(input("Enter the node number: "))
                if 1 <= node <= len(data):
                    return keys[node - 1]
                else:
                    print("Please enter a valid number.")

            except ValueError:
                print("Please enter a valid number.")

    except FileNotFoundError:
        print(
            f"File '{file_name_with_extension}' not found. Please make sure the file exists."
        )
        return None
