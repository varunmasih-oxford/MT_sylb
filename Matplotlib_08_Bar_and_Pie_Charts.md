# Section 8: Bar and Pie Charts

## 1. Bar Charts

Bar charts are used to compare values across categories.

---

### Vertical Bar Chart

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values)
plt.title("Vertical Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

---

### Horizontal Bar Chart

```python
plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()
```

---

## 2. Grouped Bar Chart

Used to compare multiple datasets side by side.

```python
import numpy as np

x = np.arange(4)
width = 0.3

values1 = [10, 20, 15, 25]
values2 = [12, 18, 10, 22]

plt.bar(x - width/2, values1, width, label='Dataset 1')
plt.bar(x + width/2, values2, width, label='Dataset 2')

plt.xticks(x, ['A', 'B', 'C', 'D'])
plt.legend()
plt.title("Grouped Bar Chart")
plt.show()
```

---

## 3. Stacked Bar Chart

Used to show contribution of different parts to a whole.

```python
values1 = [10, 20, 15, 25]
values2 = [5, 10, 5, 10]

plt.bar(categories, values1, label='Part 1')
plt.bar(categories, values2, bottom=values1, label='Part 2')

plt.legend()
plt.title("Stacked Bar Chart")
plt.show()
```

---

## 4. Pie Chart

Used to represent proportions.

---

### Basic Pie Chart

```python
labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels)
plt.title("Pie Chart")
plt.show()
```

---

### Pie Chart with Percentages

```python
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart with Percentages")
plt.show()
```

---

## 5. Exploded Pie Chart

Used to highlight a specific section.

```python
explode = [0, 0.1, 0, 0]  # explode 2nd slice

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
plt.title("Exploded Pie Chart")
plt.show()
```

---

## Key Points

* `plt.bar()` → Vertical bar chart
* `plt.barh()` → Horizontal bar chart
* `bottom` parameter → Used in stacked bar chart
* `autopct` → Displays percentage in pie chart
* `explode` → Highlights a slice in pie chart
* `legend()` → Helps in comparing multiple datasets

---
