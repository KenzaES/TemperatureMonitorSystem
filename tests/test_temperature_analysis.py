import unittest
from Temperature_monitor_project.temperature_analysis import maximum, minimum, average, StatusCount

temperatures = [12, 25.5, -5, 40]


class TestTemperatureAnalysis(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(minimum(temperatures), -5)
        self.assertEqual(minimum([]), None)
    
    def test_maximum(self):
        self.assertEqual(maximum(temperatures), 40)
        self.assertEqual(maximum([]), None)
        
    def test_average(self):
        self.assertEqual(average(temperatures), 18.12)
        self.assertEqual(average([]), None)
       
    def test_counterStatus(self):
        statuses = [
            "Critical Temperature 🚨",
            "Warning ❗",
            "Normal Temperature ✅",
            "Critical Temperature 🚨"
        ]
        self.assertEqual(StatusCount(statuses), (2, 1))
        self.assertEqual(StatusCount([]), (0, 0))