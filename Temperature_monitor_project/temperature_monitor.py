from validation import validate_temperature
from thresholds import monitor_temp
from temperature_analysis import minimum, maximum, average, StatusCount
from datetime import datetime
import csv

stored_value = []
# start by a while loop to check if the input is a number, continue the loop just after the condition is true
while True:
    try:
        UserInput = input("please enter the current temperature in celcius: ")
        if UserInput.strip().lower() == "exit":
            print(f"You typed: {UserInput}")
            print("Exiting the loop...")
            break

        Tstart = float(UserInput)

        # check if the value is finite value and a number
        validate_test = validate_temperature(Tstart)
        print("The current temperature in celsius is: ", validate_test, "°C")
        

        # analyze temperature and show the statue
        Tanalyzed = monitor_temp(validate_test)
        print("System temperature status: ", Tanalyzed)

        Temp_status = {"Temperature": validate_test, "Status": Tanalyzed}
        Temp_status["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        stored_value.append(Temp_status)
        print(stored_value)
        

    except ValueError as e:
        print(e)

# storing data on CSV file using DictWriter because it's list of dict
if stored_value:
    # with open, to open and close automatically, further the encoding here is for the emojis in my status
    with open(
        "storedTemperature_values.csv", "w", newline="", encoding="utf-8"
    ) as CSV_value:
        # extract the keys from dict
        fieldnames = stored_value[0].keys()
        CSV_data = csv.DictWriter(CSV_value, fieldnames=fieldnames)

        CSV_data.writeheader()
        CSV_data.writerows(stored_value)
    print(" Data successfully saved to storedTemperature_values.csv")

    # create an empty list for the Temperature values
    Temp = [i["Temperature"] for i in stored_value]

    Status = [i["Status"] for i in stored_value]
    print("The temperatures scored at this simulation are:", Temp)

    minValue = minimum(Temp)
    maxValue = maximum(Temp)
    averageValue = average(Temp)
    # unpacking retunring value of my function
    critical_counter, warning_counter = StatusCount(Status)
    print("As results we obtain: ")
    print("The High temperature scored is: ", maxValue)
    print("The Low temperature scored is: ", minValue)
    print("The average temperature scored: ", averageValue)
    print(
        "In this simulation we have scored ",
        warning_counter,
        "warning cases &",
        critical_counter,
        "critical cases.",
    )
else:
    print("No data to save.")


print("Loop has ended.")
