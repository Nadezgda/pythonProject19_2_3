import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division_calculate_correctly(self):
        assert  self.calc.division(self, 8, 2) == 4

    def test_subtraction_calculate_correctly(self):
        assert  self.calc.substraction(self, 7, 4) == 3

    def test_adding_calculate_correctly(self):
        assert  self.calc.adding(self, 4, 5) == 9

    def test_adding_failed(self):
        assert self.calc.adding(self, 1, 2) == 6