from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, numbers: str) -> int:
        pass
