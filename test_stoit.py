#!/usr/bin/env python3
"""
Tests for stoit.py
"""

import unittest
from stoit import is_worth_it


class TestStoit(unittest.TestCase):
    """Test cases for the is_worth_it function."""
    
    def test_worth_it_when_value_greater(self):
        """Test when value is greater than cost."""
        self.assertTrue(is_worth_it(100, 50))
    
    def test_worth_it_when_value_equal(self):
        """Test when value equals cost."""
        self.assertTrue(is_worth_it(50, 50))
    
    def test_not_worth_it_when_value_less(self):
        """Test when value is less than cost."""
        self.assertFalse(is_worth_it(30, 50))
    
    def test_with_zero_values(self):
        """Test with zero values."""
        self.assertTrue(is_worth_it(0, 0))
    
    def test_with_negative_values(self):
        """Test with negative values."""
        self.assertTrue(is_worth_it(-10, -20))
        self.assertFalse(is_worth_it(-20, -10))


if __name__ == "__main__":
    unittest.main()
