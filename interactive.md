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


## 10. Add Reset Button

### Import Button Widget

```python
from matplotlib.widgets import Button
```

---

### Create Button Axis

```python
ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
```

Position format:

```
[left, bottom, width, height]
```

* Places button at bottom-right of the figure

---

### Create Button

```python
button = Button(ax_button, 'Reset')
```

* Label: **Reset**

---

### Define Reset Function

```python
def reset(event):
    slider.reset()
```

* Resets slider to its initial value
* Automatically updates the graph

---

### Connect Button to Function

```python
button.on_clicked(reset)
```

* Executes `reset()` when button is clicked

---

## Output

* A **Reset button** appears on the plot
* Clicking it:

  * Restores slider to default value
  * Graph returns to original shape

---

## Summary

* `Button` widget adds interactivity
* Useful for restoring default state
* Works with sliders and other controls

---
## 11. Add Radio Buttons (Function Selector)

### Import RadioButtons

```python id="k3m9za"
from matplotlib.widgets import RadioButtons
```

---

### Create Radio Button Axis

```python id="z7p2bx"
ax_radio = plt.axes([0.02, 0.5, 0.15, 0.15])
```

Position format:

```id="0a9lqk"
[left, bottom, width, height]
```

* Places radio buttons on the left side of the figure

---

### Create Radio Buttons

```python id="p1xv8s"
radio = RadioButtons(ax_radio, ('sin', 'cos'))
```

* Two options:

  * `sin`
  * `cos`

---

### Define Update Function

```python id="q8d3nt"
def update_function(label):
    if label == 'sin':
        line.set_ydata(np.sin(x))
    else:
        line.set_ydata(np.cos(x))
    fig.canvas.draw_idle()
```

* `label` → selected option
* Updates graph based on selection:

  * sine wave
  * cosine wave

---

### Connect Radio Button to Function

```python id="f6y2wc"
radio.on_clicked(update_function)
```

* Calls function when selection changes

---

## Output

* Radio buttons appear on the plot
* Selecting:

  * **sin** → shows sine wave
  * **cos** → shows cosine wave

---

## Summary

* `RadioButtons` allow selection between options
* Useful for switching datasets or functions
* Adds interactive control to visualization

---

## Practice Tasks

1. Add more options (e.g., `tan`)
2. Combine with slider (amplitude + function change)
3. Display label on graph (current function)

---
