from Algoritmos import Algorithm


class Flooding(Algorithm):
    def __init__(self, topology):
        """
        Initialize the Flooding algorithm with the provided network topology.

        Args:
            topology (dict): A dictionary representing the network topology with nodes and their neighbors.
        """
        self.topology = topology
        self.initialize_node()

    def initialize_node(self, node_name):
        """
        Initialize the current node by prompting the user for its name and neighbors.
        """
        self.node_name = node_name
        self.neighbors = self.topology.get(node_name, [])

    def send_message(self, message, destination):
        """
        Send a message to a recipient in the network.

        Args:
            message (str): The message to be sent.
            destination (str): The recipient node's name.
        """
        print(f"📤 Sending message to neighbors: {self.neighbors}")
        print("💌 Message destination:", destination)
        print(f"📋 Visited nodes: [{self.node_name}]")
        print("📩 Message:", message)

    def receive_message(self, message, sender, visited_nodes):
        """
        Receive a message from a sender in the network.

        Args:
            message (str): The received message.
            sender (str): The sender node's name.
            visited_nodes (str): Comma-separated list of visited nodes.
        """
        destination, message, sender = (
            sender,
            message,
            self.node_name,
        )  # Swap values for the received message
        if destination == self.node_name:
            print(f"📥 Message received from: {sender}, the message is: {message}")
        elif self.node_name in visited_nodes:
            print("🚫 Message already sent, no need to resend it")
        else:
            print("📤 Sending message to neighbors:", self.neighbors)
            print(f"💌 Message destination: {destination}, sender: {sender}")
            print("📋 Visited nodes:", visited_nodes + f", {self.node_name}")


def manual_input():
    # Create an empty dictionary to store the network topology
    topology = {}

    # Prompt the user to input the network topology by specifying nodes and their neighbors
    while True:
        node_name = input("Enter a node name (or press Enter to finish): ")
        if not node_name:
            break
        neighbors = input(
            f"Enter neighbors for {node_name} separated by commas: "
        ).split(",")
        topology[node_name] = neighbors

    return topology


def automatic_input():
    # Create a network topology with hard-coded data
    return {
        "NodeA": ["NodeB", "NodeC"],
        "NodeB": ["NodeA", "NodeD"],
        "NodeC": ["NodeA", "NodeD"],
        "NodeD": ["NodeB", "NodeC"],
    }


# Define a function to create a network topology and send/receive messages using flooding protocol
def automatic_messages(nodes):
    # Send and receive messages using the Flooding algorithm
    nodes["NodeA"].send_message("Hello, NodeB!", "NodeB")
    nodes["NodeD"].receive_message("Hi there!", "NodeB", "NodeA,NodeC")
    nodes["NodeC"].send_message("Message from NodeC", "NodeD")


# Define a function to create a network topology and send/receive messages using flooding protocol
def Execute():

    op = input("Do you want to do a manual input? (s/n): ")
    if op == "s":
        topology = manual_input()
        # Create an instance of the Flooding class with the provided network topology
        flooding = Flooding(topology)
        automatic = False

    elif op == "n":
        topology = automatic_input()
        # Create an instance of the Flooding class with the provided network topology
        flooding = Flooding(topology)
        automatic = True
    else:
        print("Invalid option. Please try again.")
        return

    # Create a dictionary to store the nodes in the network
    nodes = {}
    for node_name in topology.keys():
        nodes[node_name] = Flooding(topology)

    # Function to send a message to other nodes
    def sendmessage():
        message = input("📝 Enter the message: ")
        destination = input("📬 Enter the destination: ")
        flooding.send_message(message, destination)

    # Function to receive and process a message
    def receivemessage():
        received = input(
            "📥 Enter the message in the format 'destination,message,sender': "
        )
        parts = received.split(",")
        destination = parts[0]
        message = parts[1]
        sender = parts[2]
        visited_nodes = input(
            "🌐 Enter the visited nodes in the format 'node1,node2,node3': "
        )
        flooding.receive_message(message, sender, visited_nodes)

    # Main menu for user interaction
    while True:

        print("\n\n1. ✉️ Send message")
        print("2. 📩 Receive message")
        print("3. 🚪 Exit")
        option = input("Enter your choice: ")

        # Process user's choice
        match option:
            case "1":
                sendmessage()  # Call sendmessage function
            case "2":
                receivemessage()  # Call receivemessage function
            case "3":
                return  # Exit the program
            case _:
                print("Invalid option. Please try again.")
        # If automatic mode is selected, add automatic messages
        if automatic:
            automatic_messages(nodes)
