import unittest
from Temperature_monitor_project.validation import validate_temperature
from Temperature_monitor_project.thresholds import monitor_temp


class TestTemperatureIntegration(unittest.TestCase):
    def test_valid_temperature_warning(self):
        valTemp= validate_temperature(33)
        
        self.assertEqual(monitor_temp(valTemp), "Warning ❗" )
    
    def test_invalid_temperature_rejected(self):
        with self.assertRaises(ValueError):
            validate_temperature(150)
    def test_upper_boundary_temperature(self):
        maxLimit= validate_temperature(100)
        self.assertEqual(monitor_temp(maxLimit), "Critical Temperature 🚨")