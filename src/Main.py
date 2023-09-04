from AlgoritmoFlooding import *


def main():
    while True:
        print("\n\n1. ✉️ Use Flooding Algorithm")
        print("2. 📋 Use Algorithm 2")
        print("3. 🔄 Use Algorithm 3")
        print("4. 🚪 Exit")
        option = input("Enter your choice: ")

        if option == "1":
            # Code for using the Flooding algorithm
            Execute()
        elif option == "2":
            # Code for using Algorithm 2
            pass
        elif option == "3":
            # Code for using Algorithm 3
            pass
        elif option == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
