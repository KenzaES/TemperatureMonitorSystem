# Frozen temperature -- Range of <0
# Low temparature -- Range of [0,17]
# normal temperatue -- Range of ]17,30]
# Warning -- Range of ]30,36]
# high temperature -- Range of ]36, 45]
# critical temperature -- Range of >45


def monitor_temp(Tthreshold):

    if Tthreshold < 0:
        return "Frozen Temperature ❄️"

    elif 0 <= Tthreshold <= 17:
        return "Low Temperature 🌫️"

    elif 17 < Tthreshold <= 30:
        return "Normal Temperature ✅"

    elif 30 < Tthreshold <= 36:
        return "Warning ❗"

    elif 36 < Tthreshold <= 45:
        return "High Temperature ⚠️"

    else:
        return "Critical Temperature 🚨"
