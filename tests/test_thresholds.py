import unittest
from Temperature_monitor_project.thresholds import monitor_temp

class TestTempStatus(unittest.TestCase):
    def test_normal_threshold(self):
        self.assertEqual(monitor_temp(17.1),"Normal Temperature ✅")
        self.assertEqual(monitor_temp(30),"Normal Temperature ✅")
        
    def test_low_threshold(self):
        self.assertEqual(monitor_temp(0),"Low Temperature 🌫️")
        self.assertEqual(monitor_temp(17),"Low Temperature 🌫️")
        
    def test_warning_threshold(self):
        self.assertEqual(monitor_temp(30.5), "Warning ❗")
        self.assertEqual(monitor_temp(36), "Warning ❗")
    
    def test_high_threshold(self):
            self.assertEqual(monitor_temp(36.1), "High Temperature ⚠️")
            self.assertEqual(monitor_temp(45), "High Temperature ⚠️")
            
    def test_critical_threshold(self):
            self.assertEqual(monitor_temp(45.1), "Critical Temperature 🚨")
            self.assertEqual(monitor_temp(100), "Critical Temperature 🚨")