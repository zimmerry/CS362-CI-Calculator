"""
Tests for calculator app
"""

import calculator


class TestCalculatorApp:
    def test_add(self):
        assert calculator.add(3, 2) == 5

    def test_sub(self):
        assert calculator.sub(7, 2) == 5