# ___fuctions for anlyzing temperature_monitor data; min, max, average, counters of status
# calculate min
def minimum(T):
    if not T:
        return None
    return min(T)


# calculate max
def maximum(T):
    if not T:
        return None
    return max(T)


# calculate average
def average(T):
    if not T:
        return None
    else:
        total = sum(T)
        count = len(T)
        averageValue = round((total / count), 2)
        return averageValue
    

# count statuses
def StatusCount(T):
    data = T
    counterC = 0
    counterW = 0

    for x in data:
        if "critical" in x.lower():
            counterC += 1

        elif "warning" in x.lower():
            counterW += 1

    return counterC, counterW
