# Section 1. 01 Introduction to Matplotlib

- What is Matplotlib?
- Installation and setup
- Basic import conventions
- Matplotlib vs Seaborn vs Plotly



## 1. What is Matplotlib?

Matplotlib is a Python library used to create graphs and charts.

### Example: Simple Line Chart

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# Plot
plt.plot(x, y)

# Labels
plt.title("Basic Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show
plt.show()
```

---

## 2. Installation and Setup

### Install using pip

```bash
pip install matplotlib
```

### Check Installation

```python
import matplotlib
print("Matplotlib Version:", matplotlib.__version__)
```

---

## 3. Basic Import Conventions

### Standard Import

```python
import matplotlib.pyplot as plt
```

### Example: Multiple Lines

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

plt.plot(x, [10, 20, 30, 40], label="Line 1")
plt.plot(x, [40, 30, 20, 10], label="Line 2")

plt.legend()
plt.title("Multiple Lines")
plt.show()
```

---

## 4. Matplotlib vs Seaborn vs Plotly

### 4.1 Matplotlib Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

plt.bar(x, y)
plt.title("Bar Chart - Matplotlib")
plt.show()
```

---

### 4.2 Seaborn Example

```python
import seaborn as sns
import matplotlib.pyplot as plt

data = [5, 10, 15, 20]

sns.lineplot(data=data)
plt.title("Line Plot - Seaborn")
plt.show()
```

---

### 4.3 Plotly Example

```python
import plotly.express as px

x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

fig = px.bar(x=x, y=y, title="Interactive Bar Chart - Plotly")
fig.show()
```

---

## 5. Combined Example

```python
# Matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Matplotlib Plot")
plt.show()

# Seaborn
import seaborn as sns

sns.lineplot(x=x, y=y)
plt.title("Seaborn Plot")
plt.show()

# Plotly
import plotly.express as px

fig = px.line(x=x, y=y, title="Plotly Plot")
fig.show()
```

