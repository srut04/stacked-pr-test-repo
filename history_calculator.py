# history_calculator.py
from calculator import Calculator

class HistoryCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = super().subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result
