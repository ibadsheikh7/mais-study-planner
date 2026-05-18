# Subject classes - shows Inheritance, Abstraction, Method Overloading

from abc import ABC, abstractmethod


class BaseSubject(ABC):
    """Abstract class - shows Abstraction."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_level(self):
        pass


class Subject(BaseSubject):
    """Normal Subject - inherits BaseSubject."""

    def __init__(self, name, marks=0):
        super().__init__(name)
        self.marks = marks

    def get_level(self):
        if self.marks < 50:
            return "Weak"
        elif self.marks < 75:
            return "Average"
        else:
            return "Strong"

    # Operator Overloading: add marks of two subjects
    def __add__(self, other):
        return self.marks + other.marks

    # Operator Overloading: compare subjects
    def __lt__(self, other):
        return self.marks < other.marks

    def __str__(self):
        return f"{self.name} ({self.marks})"


# Multilevel Inheritance examples
class WeakSubject(Subject):
    def __init__(self, name, marks):
        super().__init__(name, marks)

    def suggestion(self):
        return f"Give more time to {self.name}, practice daily."


class StrongSubject(Subject):
    def __init__(self, name, marks):
        super().__init__(name, marks)

    def suggestion(self):
        return f"You are good in {self.name}, keep revising weekly."
