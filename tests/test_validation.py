import unittest
from Temperature_monitor_project.validation import validate_temperature

class Temp_validation_test(unittest.TestCase):
    def test_valid_temperature(self):
        self.assertEqual(validate_temperature(100), 100)
        self.assertEqual(validate_temperature(-20), -20)
        with self.assertRaises(ValueError):
            validate_temperature(101)
        with self.assertRaises(ValueError):
            validate_temperature(-21)
        with self.assertRaises(ValueError):
            validate_temperature(float("nan"))
        with self.assertRaises(ValueError):
            validate_temperature(float("inf"))
        with self.assertRaises(ValueError):
            validate_temperature("hello")