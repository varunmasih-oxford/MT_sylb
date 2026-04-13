# Section 3: Working with Figures and Axes

## 1. Figure and Axes Concepts

- Figure: The entire canvas or window where plots are drawn.
- Axes: The actual plotting area inside the figure.

Think of it like:
- Figure = Page
- Axes = Graph on that page

### Example
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3], [10, 20, 15])
ax.set_title("Simple Plot")

plt.show()
````

---

## 2. Creating Multiple Subplots

You can create multiple plots in one figure.

### Example (1 row, 2 columns)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].plot([1, 2, 3], [1, 4, 9])
ax[0].set_title("Plot 1")

ax[1].plot([1, 2, 3], [9, 4, 1])
ax[1].set_title("Plot 2")

plt.show()
```

---

## 3. Using add_subplot() vs subplots()

### Method 1: add_subplot()

```python
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot([1, 2, 3], [1, 2, 3])
ax2.plot([1, 2, 3], [3, 2, 1])

plt.show()
```

### Method 2: subplots() (Recommended)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1)

ax[0].plot([1, 2, 3], [1, 4, 9])
ax[1].plot([1, 2, 3], [9, 4, 1])

plt.show()
```

---

## 4. Figure Size and DPI

* figsize: Controls width and height of the figure
* dpi: Controls resolution

### Example

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4), dpi=100)

ax.plot([1, 2, 3], [10, 20, 15])

plt.show()
```

---
