# Section 2. 02 Basic Plotting

- Creating your first plot
- Line plot
- Adding labels and title
- Saving plots to files

# Section 2.02 – Basic Plotting

## 1. Creating Your First Plot

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# Create plot
plt.plot(x, y)

# Display plot
plt.show()
```

---

## 2. Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Line Plot Example")
plt.show()
```

---

## 3. Adding Labels and Title

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

plt.plot(x, y)

# Adding labels and title
plt.title("Sales Growth")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.show()
```

---

## 4. Saving Plots to Files

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Saved Plot Example")

# Save plot as image
plt.savefig("plot.png")

plt.show()
```

### Save in Different Formats

```python
plt.savefig("plot.jpg")
plt.savefig("plot.pdf")
```

