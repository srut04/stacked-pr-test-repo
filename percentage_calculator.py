# percentage_calculator.py
from calculator import Calculator
from history_calculator import HistoryCalculator

class PercentageCalculator(HistoryCalculator):
    def percentage(self, part, whole):
        ratio = self.divide(part, whole)
        return self.multiply(ratio, 100)

    def divide(self, a, b):
        return super().divide(a, b)
