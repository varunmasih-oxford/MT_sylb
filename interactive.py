## 1. Import Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
```

* `numpy` → for numerical operations
* `matplotlib.pyplot` → for plotting
* `Slider` → for interactive control

---

## 2. Create Data

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
```

* Generates 100 values between 0 and 10
* Computes sine values

---

## 3. Create Figure and Adjust Layout

```python
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
```

* Creates figure and axes
* Adds space at the bottom for slider

---

## 4. Plot the Graph

```python
line, = plt.plot(x, y)
```

* Plots sine wave
* Stores line object for updates

---

## 5. Create Slider Axis

```python
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
```

Position format:

```
[left, bottom, width, height]
```

---

## 6. Create Slider

```python
slider = Slider(ax_slider, 'Amplitude', 0.1, 2.0, valinit=1)
```

* Label: Amplitude
* Min: 0.1
* Max: 2.0
* Default: 1

---

## 7. Define Update Function

```python
def update(val):
    line.set_ydata(np.sin(x) * slider.val)
    fig.canvas.draw_idle()
```

* Updates sine wave based on slider value
* Redraws plot

---

## 8. Connect Slider to Function

```python
slider.on_changed(update)
```

* Calls `update()` when slider changes

---

## 9. Show Plot

```python
plt.show()
```

* Displays interactive plot

---

## Output

* Interactive sine wave
* Slider controls amplitude
* Real-time updates

---

## Practice Tasks

1. Modify code to control **frequency**
2. Add another slider for **phase shift**
3. Change sine wave to **cosine**
4. Add grid and labels

---

## Example Extension

```python
np.sin(freq * x + phase) * amplitude
```

---

## Summary

* Sliders make plots interactive
* Useful for visualization and teaching
* Can control multiple parameters dynamically

---
