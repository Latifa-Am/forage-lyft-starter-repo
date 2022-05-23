from abc import ABC, abstractmethod

#Defining the interface Battery and the abstract method needs_service()
class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass