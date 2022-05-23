from abc import ABC, abstractmethod

#Defining the interface Engine and the abstract method needs_service()
class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass