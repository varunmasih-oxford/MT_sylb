# Section 10: Histograms and Density Plots

## 1. Creating Histograms

A histogram displays the frequency of data within specified intervals called **bins**.

### Example

```python
import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 22, 25, 28, 30, 32, 35, 38, 40]

plt.hist(data)
plt.title("Basic Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
```

### Output

* Bars represent the number of values in each interval.
* Taller bars indicate higher frequency.

---

## 2. Setting Bin Sizes

The **bins** parameter controls how the data is grouped.

### Example 1: Fixed Number of Bins

```python
import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 22, 25, 28, 30, 32, 35, 38, 40]

plt.hist(data, bins=5)
plt.title("Histogram with 5 Bins")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
```

### Example 2: More Bins

```python
plt.hist(data, bins=10)
plt.title("Histogram with 10 Bins")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
```

### Key Point

* **Fewer bins** → Simpler, less detail.
* **More bins** → More detailed distribution.

---

## 3. Density Plots with `histtype='step'`

Using `histtype='step'` creates an outline-style histogram instead of filled bars.

### Example

```python
import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 22, 25, 28, 30, 32, 35, 38, 40]

plt.hist(data, bins=6, histtype='step')
plt.title("Density Plot using Step Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
```

### Explanation

* `histtype='step'` draws only the borders of the histogram.
* Useful when comparing multiple datasets.

---

## 4. Cumulative Histograms

A cumulative histogram shows the running total of frequencies.

### Example

```python
import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 22, 25, 28, 30, 32, 35, 38, 40]

plt.hist(data, bins=6, cumulative=True)
plt.title("Cumulative Histogram")
plt.xlabel("Values")
plt.ylabel("Cumulative Frequency")
plt.show()
```

### Explanation

* Each bar includes the count of all previous bins.
* Useful for analyzing cumulative distributions.

---

## 5. Density Histogram

Setting `density=True` normalizes the histogram so that the total area equals 1.

### Example

```python
import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 22, 25, 28, 30, 32, 35, 38, 40]

plt.hist(data, bins=6, density=True)
plt.title("Density Histogram")
plt.xlabel("Values")
plt.ylabel("Density")
plt.show()
```

### Explanation

* Shows probability density instead of raw frequency.
* Useful for comparing datasets of different sizes.

---

# Key Points

* **`plt.hist()`** → Creates a histogram.
* **`bins`** → Controls the number of intervals.
* **`histtype='step'`** → Creates an outline (step) histogram.
* **`cumulative=True`** → Displays cumulative frequencies.
* **`density=True`** → Normalizes the histogram to show probability density.
* Histograms are useful for understanding the **distribution, spread, and frequency** of numerical data.
