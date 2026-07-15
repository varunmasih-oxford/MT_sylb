# Section 13: Working with Dates and Times

Many real-world datasets contain **dates and times**, such as stock prices, weather records, website traffic, and sales data. Matplotlib provides tools to easily plot and format date-based data.

---

# 1. Plotting Time Series Data

A **time series** is a sequence of data points recorded over time.

### Basic Time Series Plot

```python
import matplotlib.pyplot as plt
from datetime import datetime

# Dates
dates = [
    datetime(2024, 1, 1),
    datetime(2024, 1, 2),
    datetime(2024, 1, 3),
    datetime(2024, 1, 4),
    datetime(2024, 1, 5)
]

# Values
sales = [100, 120, 115, 140, 150]

plt.plot(dates, sales, marker='o')

plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.show()
```

### Output

A line chart where the x-axis displays dates and the y-axis displays sales values.

---

# 2. Formatting Date Ticks

Long date labels can overlap. The **matplotlib.dates** module helps format date labels for better readability.

### Formatting Dates

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

dates = [
    datetime(2024, 1, 1),
    datetime(2024, 1, 2),
    datetime(2024, 1, 3),
    datetime(2024, 1, 4),
    datetime(2024, 1, 5)
]

values = [10, 20, 15, 30, 25]

plt.plot(dates, values, marker='o')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

plt.title("Formatted Date Ticks")
plt.xlabel("Date")
plt.ylabel("Values")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

### Common Date Format Codes

| Format Code | Output Example |
| ----------- | -------------- |
| `%d`        | 01             |
| `%m`        | 01             |
| `%Y`        | 2024           |
| `%y`        | 24             |
| `%b`        | Jan            |
| `%B`        | January        |
| `%a`        | Mon            |
| `%A`        | Monday         |

---

# 3. Using `matplotlib.dates` Module

The `matplotlib.dates` module provides tools for formatting and controlling date axes.

### Setting Monthly Ticks

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

dates = [
    datetime(2024, 1, 1),
    datetime(2024, 2, 1),
    datetime(2024, 3, 1),
    datetime(2024, 4, 1),
    datetime(2024, 5, 1)
]

values = [50, 60, 55, 70, 80]

plt.plot(dates, values, marker='o')

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.title("Monthly Data")
plt.xlabel("Month")
plt.ylabel("Value")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

---

# 4. Auto Formatting Date Labels

Matplotlib can automatically rotate and align date labels.

```python
import matplotlib.pyplot as plt
from datetime import datetime

dates = [
    datetime(2024, 1, 1),
    datetime(2024, 1, 2),
    datetime(2024, 1, 3),
    datetime(2024, 1, 4),
    datetime(2024, 1, 5)
]

values = [12, 18, 15, 22, 20]

plt.plot(dates, values)

plt.title("Auto Formatted Dates")

plt.gcf().autofmt_xdate()

plt.show()
```

---

# 5. Plotting Date and Time Together

You can also plot both **date and time** values.

```python
import matplotlib.pyplot as plt
from datetime import datetime

times = [
    datetime(2024, 1, 1, 9, 0),
    datetime(2024, 1, 1, 11, 0),
    datetime(2024, 1, 1, 13, 0),
    datetime(2024, 1, 1, 15, 0),
    datetime(2024, 1, 1, 17, 0)
]

temperature = [20, 24, 28, 26, 22]

plt.plot(times, temperature, marker='o')

plt.title("Temperature Throughout the Day")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.gcf().autofmt_xdate()

plt.show()
```

---

# 6. Using Different Date Locators

The `matplotlib.dates` module provides locators to control the spacing of date ticks.

| Locator            | Purpose                   |
| ------------------ | ------------------------- |
| `DayLocator()`     | Tick every day            |
| `WeekdayLocator()` | Tick on selected weekdays |
| `MonthLocator()`   | Tick every month          |
| `YearLocator()`    | Tick every year           |
| `HourLocator()`    | Tick every hour           |
| `MinuteLocator()`  | Tick every minute         |

### Example: Year Locator

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

dates = [
    datetime(2020, 1, 1),
    datetime(2021, 1, 1),
    datetime(2022, 1, 1),
    datetime(2023, 1, 1),
    datetime(2024, 1, 1)
]

values = [40, 50, 55, 65, 75]

plt.plot(dates, values, marker='o')

plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.title("Yearly Growth")
plt.xlabel("Year")
plt.ylabel("Value")

plt.show()
```

---

# Key Points

* Time series data represents values measured over time.
* `plt.plot()` is commonly used to plot date and time data.
* `matplotlib.dates` (`mdates`) provides utilities for formatting and controlling date axes.
* `DateFormatter()` customizes how dates appear on the axis.
* `DayLocator()`, `MonthLocator()`, `YearLocator()`, and similar locators control tick intervals.
* `plt.xticks(rotation=45)` or `plt.gcf().autofmt_xdate()` improves the readability of date labels.
* `plt.tight_layout()` helps prevent date labels from overlapping or being clipped.
