import math


def validate_temperature(val):
    if isinstance(val, (int, float)) and math.isfinite(val):
        if val < -20 or val > 100:
            raise ValueError("Rejected invalid numeric, out of the range -20 and 100°C ")
        return val

    
    else:
        raise ValueError(f"Rejected invalid numeric value: {val}")
