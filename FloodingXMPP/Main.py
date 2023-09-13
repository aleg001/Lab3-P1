from AlgoritmoFlooding import *
from NodeSelection import *


def main():
    while True:
        print("\n\n1. ✉️ Use Flooding Algorithm")
        print("2. 🚪 Exit")
        option = input("Enter your choice: ")

        if option == "1":
            usuario = NodeSelect()
            server = Flooding(usuario, "123")
            server.connect(disable_starttls=True)
            server.process(forever=False)
        elif option == "2":
            print("Goodbye my friend! 👋")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
