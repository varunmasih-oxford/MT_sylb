# Section 15: Interactive Plots

## 1. Introduction

Interactive plots allow users to interact with visualizations dynamically using controls like sliders, buttons, and mouse events.

---

## 2. Matplotlib Widgets

Matplotlib provides built-in widgets for interactivity.

### Import Widgets

```python
from matplotlib.widgets import Slider, Button, RadioButtons
```

---

## 3. Slider Widget

Used to dynamically update a plot.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

line, = plt.plot(x, y)

# Slider axis
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Amplitude', 0.1, 2.0, valinit=1)

def update(val):
    line.set_ydata(np.sin(x) * slider.val)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
```

---

## 4. Button Widget

Used to trigger actions like resetting the plot.

```python
from matplotlib.widgets import Button

ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_button, 'Reset')

def reset(event):
    slider.reset()

button.on_clicked(reset)
```

---

## 5. Radio Buttons

Used to switch between options.

```python
from matplotlib.widgets import RadioButtons

ax_radio = plt.axes([0.02, 0.5, 0.15, 0.15])
radio = RadioButtons(ax_radio, ('sin', 'cos'))

def update_function(label):
    if label == 'sin':
        line.set_ydata(np.sin(x))
    else:
        line.set_ydata(np.cos(x))
    fig.canvas.draw_idle()

radio.on_clicked(update_function)
```

---

## 6. Interactive Navigation Toolbar

Matplotlib provides a default toolbar with:

* Zoom in / Zoom out
* Pan (move plot)
* Save figure
* Reset view

This toolbar appears automatically in most environments like Jupyter Notebook or Python IDEs.

---

## 7. Event Handling and Callbacks

You can respond to user actions like mouse clicks or key presses.

---

### Mouse Click Event

```python
def onclick(event):
    print(f"Mouse clicked at ({event.xdata}, {event.ydata})")

fig.canvas.mpl_connect('button_press_event', onclick)
```

---

### Key Press Event

```python
def onkey(event):
    print(f"Key pressed: {event.key}")

fig.canvas.mpl_connect('key_press_event', onkey)
```

---

## Key Points

* Widgets make plots interactive and user-friendly
* `Slider` → controls continuous values
* `Button` → triggers actions
* `RadioButtons` → selects between options
* `mpl_connect()` → used for event handling
* `draw_idle()` → updates plot efficiently

---
