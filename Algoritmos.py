from abc import ABC, abstractmethod

# Defining the Algorithm abstract base class
class Algorithm(ABC):
    @abstractmethod
    def send_message(self, message, receipient):
        pass

    @abstractmethod
    def receive_message(self, message, sender, visitedTables):
        pass
