import tkinter as tk
from tkinter import simpledialog, messagebox
from Algoritmos import Algorithm


global recipient


class Flooding(Algorithm):
    """
    A class representing the Flooding Algorithm for message propagation in a network.
    """

    def __init__(self, node_name=None, neighbors=None):
        """
        Initializes the FloodingAlgorithm class by requesting user input.
        """
        if node_name and neighbors:
            self.node_name = node_name
            self.neighbors = neighbors.split(",")
        else:
            self.request_input()

    def request_input(self):
        """
        Requests user input for the current node's name and its neighbors.
        """
        self.node_name = input("🌟 Enter the name of the current node: ")
        neighbors = input("🌐 Enter the neighbors separated by commas: ")
        self.neighbors = neighbors.split(",")

    def send_message(self, message, recipient):
        """
        Sends a message to the specified recipient and logs the action.

        Args:
            message (str): The message to be sent.
            recipient (str): The recipient's name.
        """
        print(f"📤 Sending message to neighbors: {', '.join(self.neighbors)}")
        print(f"💌 Message to {recipient} from {self.node_name}: {message}")
        print(f"🚶‍♂️ Visited nodes: [{self.node_name}]")

    def receive_message(self, message, sender, visited_nodes):
        """
        Receives and processes a message from a sender.

        Args:
            message (str): The received message.
            sender (str): The sender's name.
            visited_nodes (list): List of visited nodes in the message propagation.
        """
        if recipient == self.node_name:
            print(f"📬 Message received from {sender}: {message}")
        elif self.node_name in visited_nodes:
            print("⚠️ Message already sent, no need to resend.")
        else:
            print(f"📤 Sending message to neighbors: {', '.join(self.neighbors)}")
            print(f"💌 Recipient: {recipient}, Sender: {sender}")
            print(f"🚶‍♂️ Visited nodes: [{', '.join(visited_nodes)}, {self.node_name}]")


class FloodingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flooding Algorithm")
        self.flooding = Flooding()
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for Node Name
        tk.Label(self.root, text="Name of the node:").grid(
            row=0, column=0, sticky=tk.W, padx=10, pady=5
        )
        self.node_name_var = tk.StringVar(value=self.flooding.node_name)
        tk.Entry(self.root, textvariable=self.node_name_var).grid(
            row=0, column=1, padx=10, pady=5
        )

        # Label and Entry for Neighbors
        tk.Label(self.root, text="Neighbors (comma separated):").grid(
            row=1, column=0, sticky=tk.W, padx=10, pady=5
        )
        self.neighbors_var = tk.StringVar(value=",".join(self.flooding.vecinos))
        tk.Entry(self.root, textvariable=self.neighbors_var).grid(
            row=1, column=1, padx=10, pady=5
        )

        # Send Message Section
        tk.Label(self.root, text="Send Message:").grid(
            row=2, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.message_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.message_var, width=40).grid(
            row=2, column=1, padx=10, pady=10
        )
        self.destination_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.destination_var, width=40).grid(
            row=2, column=2, padx=10, pady=10
        )
        tk.Button(self.root, text="Send", command=self.send_message).grid(
            row=2, column=3, padx=10, pady=10
        )

        # Receive Message Section
        tk.Label(self.root, text="Receive Message:").grid(
            row=3, column=0, sticky=tk.W, padx=10, pady=10
        )
        self.recv_message_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.recv_message_var, width=40).grid(
            row=3, column=1, padx=10, pady=10
        )
        self.sender_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.sender_var, width=40).grid(
            row=3, column=2, padx=10, pady=10
        )
        self.visited_tables_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.visited_tables_var, width=40).grid(
            row=3, column=3, padx=10, pady=10
        )
        tk.Button(self.root, text="Receive", command=self.receive_message).grid(
            row=3, column=4, padx=10, pady=10
        )

    def send_message(self):
        self.flooding.node_name = self.node_name_var.get()
        self.flooding.vecinos = self.neighbors_var.get().split(",")
        self.flooding.send_message(self.message_var.get(), self.destination_var.get())
        messagebox.showinfo("Message Sent", "Message has been sent! 📤")

    def receive_message(self):
        self.flooding.node_name = self.node_name_var.get()
        self.flooding.vecinos = self.neighbors_var.get().split(",")
        self.flooding.receive_message(
            self.recv_message_var.get(),
            self.sender_var.get(),
            self.visited_tables_var.get().split(","),
        )
        messagebox.showinfo("Message Received", "Message has been received! 📬")


""" 
# Run the tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = FloodingApp(root)
    root.mainloop()
"""
