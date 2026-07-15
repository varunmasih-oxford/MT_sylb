# Section 11: Box and Violin Plots

## 1. Box Plot

A **box plot** (or **box-and-whisker plot**) is used to visualize the distribution of numerical data. It displays the minimum, first quartile (Q1), median, third quartile (Q3), maximum, and possible outliers.

### Basic Box Plot

```python
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.boxplot(data)
plt.title("Basic Box Plot")
plt.ylabel("Values")
plt.show()
```

### Output

A box plot showing:

* Median (middle line)
* Quartiles (box)
* Whiskers (range)
* Outliers (if any)

---

## 2. Creating Multiple Box Plots

You can compare the distributions of multiple datasets.

```python
import matplotlib.pyplot as plt

data1 = [10, 12, 15, 18, 20]
data2 = [15, 18, 22, 28, 35]
data3 = [8, 11, 14, 17, 19]

plt.boxplot([data1, data2, data3])

plt.title("Multiple Box Plots")
plt.xticks([1, 2, 3], ["Group A", "Group B", "Group C"])
plt.ylabel("Values")

plt.show()
```

---

# 3. Customizing Box Plot Appearance

Matplotlib provides several options to customize box plots.

### Colored Box Plot

```python
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.boxplot(
    data,
    patch_artist=True,
    boxprops=dict(facecolor="lightblue", color="blue"),
    medianprops=dict(color="red", linewidth=2),
    whiskerprops=dict(color="green"),
    capprops=dict(color="black"),
    flierprops=dict(marker="o", markerfacecolor="orange", markersize=8)
)

plt.title("Customized Box Plot")
plt.ylabel("Values")

plt.show()
```

### Customization Parameters

| Parameter           | Purpose                      |
| ------------------- | ---------------------------- |
| `patch_artist=True` | Fills the box with color     |
| `boxprops`          | Changes box color and border |
| `medianprops`       | Styles the median line       |
| `whiskerprops`      | Styles whiskers              |
| `capprops`          | Styles whisker caps          |
| `flierprops`        | Styles outliers              |

---

# 4. Horizontal Box Plot

```python
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.boxplot(data, vert=False)

plt.title("Horizontal Box Plot")
plt.xlabel("Values")

plt.show()
```

---

# 5. Violin Plot

A **violin plot** combines a box plot with a density plot. It shows:

* Distribution shape
* Median
* Quartiles
* Data density

It is useful when you want to understand how data is distributed.

### Basic Violin Plot

```python
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.violinplot(data)

plt.title("Basic Violin Plot")
plt.ylabel("Values")

plt.show()
```

---

# 6. Multiple Violin Plots

```python
import matplotlib.pyplot as plt

data1 = [10, 12, 15, 18, 20]
data2 = [15, 18, 22, 28, 35]
data3 = [8, 11, 14, 17, 19]

plt.violinplot([data1, data2, data3])

plt.title("Multiple Violin Plots")
plt.xticks([1, 2, 3], ["Group A", "Group B", "Group C"])
plt.ylabel("Values")

plt.show()
```

---

# 7. Customizing Violin Plot

```python
import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]

violin = plt.violinplot(data, showmeans=True, showmedians=True)

for body in violin['bodies']:
    body.set_facecolor("lightgreen")
    body.set_edgecolor("green")
    body.set_alpha(0.7)

plt.title("Customized Violin Plot")
plt.ylabel("Values")

plt.show()
```

### Useful Parameters

| Parameter          | Description                           |
| ------------------ | ------------------------------------- |
| `showmeans=True`   | Displays the mean                     |
| `showmedians=True` | Displays the median                   |
| `showextrema=True` | Displays min and max values (default) |

---

# Difference Between Box Plot and Violin Plot

| Feature            | Box Plot                | Violin Plot                      |
| ------------------ | ----------------------- | -------------------------------- |
| Shows Median       | ✔                       | ✔                                |
| Shows Quartiles    | ✔                       | ✔                                |
| Shows Outliers     | ✔                       | ✘ (not directly)                 |
| Shows Data Density | ✘                       | ✔                                |
| Best For           | Comparing distributions | Understanding distribution shape |

---

# Key Points

* `plt.boxplot()` → Creates box plots.
* `patch_artist=True` → Enables box coloring.
* `boxprops`, `medianprops`, `whiskerprops`, `capprops`, and `flierprops` customize box plot appearance.
* `plt.violinplot()` → Creates violin plots.
* `showmeans=True` displays the mean.
* `showmedians=True` displays the median.
* **Box plots** summarize data using quartiles and outliers.
* **Violin plots** show both summary statistics and the full data distribution, making them useful for identifying patterns such as skewness or multiple peaks.
