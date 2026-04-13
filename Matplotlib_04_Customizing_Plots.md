
# Section 4: Customizing Plots

## 1. Colors, Markers, and Line Styles

### Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color='red', linestyle='--', marker='o')

plt.show()
```

---

## 2. Legends and Labels

### Example

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15], label='Sales')
plt.plot([1, 2, 3], [8, 18, 12], label='Profit')

plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Company Data")

plt.legend()

plt.show()
```

---

## 3. Setting Axis Limits and Ticks

### Example

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])

plt.xlim(0, 5)
plt.ylim(0, 25)

plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 10, 20, 30])

plt.show()
```

---

## 4. Gridlines and Background Customization

### Example

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])

plt.grid(True)

ax = plt.gca()
ax.set_facecolor("#f2f2f2")

plt.show()
```

---

# Final Combined Example

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

ax.plot(x, y, color='blue', marker='o', linestyle='--', label='Data')

ax.set_title("Customized Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.set_xlim(0, 5)
ax.set_ylim(0, 30)

ax.grid(True)
ax.legend()

plt.show()
```

---
