# Temperature Monitoring System 🌡️

A Python-based temperature monitoring application developed as a practical learning project to explore Python programming, input validation, exception handling, modular design, and automated testing.

The application allows users to enter temperature measurements in Celsius, validates the input, and determines the corresponding temperature status based on predefined thresholds. It also supports repeated measurements until the user chooses to exit.

## 📌 Project Overview

The Temperature Monitoring System is designed to demonstrate the fundamental principles of building a reliable, maintainable, and testable Python application.

The project was developed incrementally, starting with basic temperature classification and progressing to input validation, error handling, integration testing, and the exploration of temperature history storage.

### Objectives

- Practice Python fundamentals and control flow.
- Implement reusable functions and modular code.
- Validate user input and handle exceptions.
- Classify temperature measurements using predefined thresholds.
- Allow continuous interaction until the user enters `exit`.
- Develop and execute automated unit and integration tests.
- Apply software development practices using Git and GitHub.

## ✨ Features

- **Temperature classification:** Assigns a status to a temperature measurement according to predefined ranges.
- **Input validation:** Accepts numerical temperature values within the permitted input range.
- **Exception handling:** Handles invalid numerical input, such as text that cannot be converted to a floating-point number.
- **Continuous monitoring:** Repeats the input process until the user enters `exit`.
- **Modular architecture:** Separates temperature classification, validation, and user interaction into dedicated Python modules.
- **Automated testing:** Includes tests for invalid inputs, boundary values, and expected temperature classifications.
- **Temperature history development:** Provides a foundation for exploring the storage of measurements and timestamps.

## 🌡️ Temperature Classification

The application uses the following temperature thresholds:

| Temperature (°C) | Status |
|---|---|
| T < 0 | Frozen |
| 0 < T ≤ 17 | Low |
| 17 < T ≤ 30 | Normal |
| 30 < T ≤ 36 | Warning |
| 36 < T ≤ 45 | High |
| T > 45 | Critical |

**Note:** The exact value of `0°C` needs an explicit classification in the current threshold logic. It should be assigned a status before the application is considered complete.

## 🛡️ Input Validation

The application validates temperature measurements before processing them.

The permitted input range is:

- Minimum: `-20°C`
- Maximum: `100°C`

Both limits are inclusive.

Inputs outside this range are rejected, and the user is prompted to enter another value.

The application also handles invalid numerical input through Python's `ValueError` exception handling. This prevents text that cannot be converted to a number from being processed as a valid temperature.

The monitoring loop supports the `exit` command, allowing the user to terminate the application without closing the terminal manually.

## 🏗️ Project Structure

The project is organized into separate modules to improve readability and maintainability.

```text
TemperatureMonitoringSystem/
│
├── temperature_monitor.py
├── thresholds.py
├── validation.py
├── tests/
│   └── test_temperature_integration.py
├── README.md
└── .gitignore
```

### Module Responsibilities

**`temperature_monitor.py`**

The main application entry point. It collects temperature input from the user, manages the monitoring loop, handles the exit command, and displays the corresponding temperature status.

**`thresholds.py`**

Contains the `monitor_temp()` function, which determines the temperature status according to the predefined classification ranges.

**`validation.py`**

Contains the `validate_temperature()` function, responsible for checking temperature values before they are processed. The validation logic uses Python's `math.isfinite()` to reject non-finite values such as `NaN` and infinity.

**`tests/`**

Contains automated tests used to verify application behavior, including invalid temperature rejection, boundary conditions, and expected status classifications.

*Adjust this structure if your final repository contains additional files or uses different filenames.*

## ⚙️ Requirements

- Python 3.10 or later
- Git (optional, for version control)
- A terminal or code editor, such as Visual Studio Code

The project uses Python's standard library for its core functionality. No third-party package is required for the basic monitoring application unless additional dependencies have been introduced.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KenzaES/TemperatureMonitorSystem.git
```

### 2. Navigate to the project directory

```bash
cd TemperatureMonitorSystem
```

### 3. Run the application

```bash
python temperature_monitor.py
```

On Windows, if the `python` command is unavailable, try:

```powershell
py temperature_monitor.py
```

Follow the instructions displayed in the terminal to enter a temperature measurement.

### 4. Exit the application

Enter:

```text
exit
```

The application should stop the monitoring loop.

## 🧪 Testing

Automated testing is an important part of this project. Tests help verify that the application behaves correctly under normal conditions, invalid inputs, and temperature boundary conditions.

The integration tests can be executed from the project root using:

```bash
python -m unittest tests.test_temperature_integration -v
```

The test suite developed during the project includes checks for:

- Rejection of invalid temperature input.
- Correct handling of the upper validation boundary.
- Correct classification of temperatures in the warning range.
- Integration between the validation, classification, and user-interaction components.

Run the test suite after modifying the validation or classification logic to identify regressions.

## 🧠 Key Concepts Practiced

Throughout this project, the following Python concepts have been explored:

- Variables and data types.
- User input and type conversion.
- Conditional statements (`if`, `elif`, and `else`).
- Loops (`while`).
- Exception handling (`try` and `except`).
- Functions and module imports.
- Input validation and Boolean conditions.
- Floating-point numbers and non-finite values.
- Unit testing and integration testing.
- Git version control and GitHub repository management.

## 🔮 Potential Future Improvements

The project can be extended with additional features as development progresses:

- Store temperature measurements with timestamps.
- Maintain a temperature history using lists or dictionaries.
- Export measurement history to a CSV file.
- Calculate minimum, maximum, and average temperatures.
- Add automated alerts for critical temperature conditions.
- Develop a graphical user interface or a real-time monitoring dashboard.
- Integrate a physical temperature sensor or a simulated sensor.
- Explore integration with embedded systems, MATLAB/Simulink, or ROS 2.

These are potential extensions and should not be considered implemented features unless they are added to the repository.

## 🎯 Learning Outcomes

This project represents a practical step toward developing stronger programming and software engineering skills, with a focus on reliability, modularity, validation, and testing.

It provides a foundation for future projects involving embedded systems, sensor monitoring, automation, and intelligent control systems.

## 👩‍💻 Author

**Kenza Es-Diri**

- GitHub: [@KenzaES](https://github.com/KenzaES)
- Project repository: [TemperatureMonitorSystem](https://github.com/KenzaES/TemperatureMonitorSystem)

---

*Developed as a practical Python learning project.*
