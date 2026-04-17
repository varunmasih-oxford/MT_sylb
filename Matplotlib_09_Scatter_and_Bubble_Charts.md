# Section 9: Scatter and Bubble Charts

## 1. Scatter Plots

Scatter plots are used to show the relationship between two numerical variables.

---

### Basic Scatter Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

---

## 2. Adding Color Encoding

Colors can represent an additional variable.

```python
colors = [100, 200, 300, 400, 500]

plt.scatter(x, y, c=colors)
plt.title("Scatter Plot with Color Encoding")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

---

## 3. Adding Size Encoding

Marker size can represent another dimension of data.

```python
sizes = [50, 100, 150, 200, 250]

plt.scatter(x, y, s=sizes)
plt.title("Scatter Plot with Size Encoding")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

---

## 4. Scatter Plot with Color and Size

Combining multiple encodings for better insights.

```python
colors = [100, 200, 300, 400, 500]
sizes = [50, 100, 150, 200, 250]

plt.scatter(x, y, c=colors, s=sizes)
plt.title("Scatter Plot with Color and Size")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

---

## 5. Bubble Chart

A bubble chart is an extension of a scatter plot where the size of each point represents a third variable.

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
sizes = [100, 300, 200, 500, 400]

plt.scatter(x, y, s=sizes)
plt.title("Bubble Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

---

## Key Points

* `plt.scatter()` → Used to create scatter plots
* `c` parameter → Controls color of points
* `s` parameter → Controls size of points (important for bubble charts)
* Bubble chart = Scatter plot + size encoding
* Useful for showing relationships and patterns in data

---
