---
# try also 'default' to start simple
theme: bricks
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://source.unsplash.com/collection/94734566/1920x1080
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# persist drawings in exports and build
drawings:
  persist: true
# use UnoCSS (experimental)
wakeLock: "build"
# aspect ratio for the slides
aspectRatio: 16/9
css: unocss
canvasWidth: 900
---

# WebTigerPython

## A Low-Floor High-Ceiling Python IDE for the Browser
## SIGCSE 2026

**Clemens Bachmann**, Alexandra Maximova, Tobias Kohn, Dennis Komm

---
layout: two-cols-header
---

# Who am I

::left::
- Name: Clemens Bachmann (he/him)
- Occupation: Doctoral Student
- University: ETH Zürich (Switzerland)
- Email: clemens.bachmann@inf.ethz.ch

::right::

<img src="./images/Clemens_Flaechen.svg" style="filter: brightness(0) saturate(100%) invert(80%);" width=270/>

[Illustration by Anna Staub](https://www.instagram.com/anna.staub.illustration/?hl=en)

---
layout: two-cols-header
---

# Educational IDEs - Problem Statement

::left::

<v-clicks>

- Easy to set up
  - no installation / login
- Works on any device
  - BYOD
- Simple UI
- Reliable
  - Replit Education

</v-clicks>

::right::

<v-click at="+2">

| High Ceiling |  |
|----|----|
| <img src="https://matplotlib.org/_static/logo_dark.svg" width="120"> | <img src="https://scipy.org/images/logo.svg" width="70"> |

</v-click>

<br>
<br>
<br>

<v-click at="-1">

| Low Floor |  |
|----|----|
| <img src="https://dfimg.dfrobot.com/enshop/ROB0148-EN/ROB0148-EN_Main_01_1220x813.jpg.webp" width="120"> | <img src="https://python-online.ch/turtle/bilder/Tu10.PNG" width="60"> |

</v-click>

<!--
mention trinket.io
-->

---
layout: two-cols-header 
zoom: 1.1
---

# Implementation WebTigerPython

::left::

- Easy to set up -> Web Based
- Works on any device -> Web Based
- Reliable -> Open Source

<img src="./images/webtigerpython_bild.svg"> </img>

::right::

<v-click>

### Architecture

<img src="./images/system_overview.svg"> </img>

</v-click>

---
layout: wtp-2-cols
code: |
  from turtle import *

  for color in ["red", 
                "blue", 
                "darkgreen", 
                "orange"]:
      pencolor(color)
      repeat 4:
          forward(100)
          right(90)
      right(90)
---
# Low Floor 1 - Turtle

- TKinter does not work in the browser
- PixiJS
  - Fast 2d graphics rendering library

---
layout: wtp-2-cols
code: |
  from mbrobot_plusV3 import *

  forward()
  repeat:
      d = getDistance()
      print(d)    
      if d < 20:
          stop()    
      delay(200)
---
# Low Floor 2 - Physical Computing

- WebUSB
  - Only in Chrome
- Simulation

---
layout: wtp-2-cols
code: |
  import numpy as np
  import matplotlib.pyplot as plt

  x = np.arange(0, 10.01, 0.01)
  f1 = np.sin(x)
  f2 = np.cos(x)
  f3 = 0.01 * x**2 + 0.15 * x - 1

  plt.plot(x, f1, color="red")
  plt.plot(x, f2, color="blue")
  plt.plot(x, f3, color="green")

  plt.show()
---
# High Ceiling 1 - Scientific Python

- NumPy / SciPy / Matplotlib
  - Thanks to Pyodide
- Use agg (Anti-Grain Geometry) to render
- Limitation: no direct access to the DOM
  - No events
  - No animations

---
layout: wtp-2-cols
code: |
  from gturtle import *
  from time import *
  from random import randrange


  breite = Screen().window_width()
  hoehe = Screen().window_height()
  fps = 10
  farbeSchlange = "green"
  farbeEssen = "red"

  spc("white")
  dot(1000)

  def createFood():
      pos = getPos()
      done = False
      spc(farbeEssen)
      while not done:
          x = randrange(-breite//20*10,breite//20*10,10)
          y = randrange(-hoehe//20*10,hoehe//20*10,10)
          setPos(x,y)
          color = getPixelColorStr()
          if color == "white":
              dot(8)
              setPos(pos)
              spc(farbeSchlange)
              done = True

  def richtungsWechsel(x):
      if x == "a":
          setHeading(-90)
      elif x == "d":
          setHeading(90)
      elif x == "w":
          setHeading(0)
      elif x == "s":
          setHeading(180)

  def teleport():
      x = getX()
      if x > breite/2 or x < -breite/2:
          setX(-x)
      y = getY()
      if y > hoehe/2 or y < -hoehe/2:
          setY(-y)

  def putzen():
      pos.append(getPos())
      if len(pos) > laenge:
          setPos(pos[0])
          spc("white")
          dot(15)
          setPos(pos[-1])
          del pos[0]
          spc(farbeSchlange)

  spw(8)
  spc(farbeSchlange)
  ht()
  createFood()
  points = 0
  name = input("Wie heisst du?")
  pause = False

  laenge = 5
  pos = []

  repeat:
      x = getKey()
      richtungsWechsel(x)

      if x == "p":
          pause = True

      while pause:
          delay(50)
          if getKey() == "p":
              pause = False

      putzen()
      
      penUp()
      forward(10)
      color = getPixelColorStr()
      back(10)
      if color == farbeSchlange :
          pd()
          forward(5)
          break
      elif color == "red":
          createFood()
          points += 1
          fps *= 1
          laenge += 3
      penDown()

      # Bewegen
      forward(10)
      delay(1000/fps)

      teleport()

  print(name, "you scored", points, "points")
  if points > 10:
      print("WON")
  else:
      print("LOST")
---
# High Ceiling 2 - Interactive Programming

- Input listeners
  - Keyboard
  - Mouse

---
zoom: 0.9
---

# Evaluation 1 - Computing Benchmark

## Mandelbrot Set Computation
**Test Case:** 200×200 pixel image with 4,000,000 iterations of z′ = z² + c

| Platform | Execution Time | Performance vs CPython |
|----------|---|---|
| **Native Python** | 0.16 s | Baseline |
| **WebTigerPython** | 0.38 s | ~2.4× slower |
| **PyodideU** | 118 s | ~738× slower |
| **trinket.io** (Skulpt) | 43 s | ~269× slower |

---
layout: two-cols 
---
# Evaluation 2 - Graphics Benchmark

<v-click at="2">

- WTP outperforms Native Python in this benchmark

<img width="300px" src="./images/balls_benchmark.jpg"></img>

</v-click>

::right::
  
<div style="display: flex; gap: 20px; align-items: center;">
  <SlidevVideo v-click="1" autoplay controls width="220px">
    <source src="/pythonballs.mp4" type="video/mp4" />
  </SlidevVideo>
  <p>Native Python</p>
</div>

<div style="display: flex; gap: 20px; align-items: center;">
  <SlidevVideo v-click="1" autoplay controls width="220px">
    <source src="/wtpballs.mp4" type="video/mp4" />
  </SlidevVideo>
  <p>WebTigerPython</p>
</div>

---
zoom: 1.3
---
# Evaluation 3 - Teacher Survey

<v-clicks>

- Userbase 12 years and above
  - Most Users 15 - 17 years
- URL Sharing was liked
- Easy integratable into other tools
- Simple

</v-clicks>

---
zoom: 1.3
---
# More to explore!

<v-clicks>

- Debugger
- Robotics Simulator
- Pygame out of the box
- Music

</v-clicks>

---
zoom: 1.3
---

# Future Work

- Multifile
- Robots over WiFi

---
layout: wtp-2-cols
code: |
  from turtle import *


  speed(0)
  penup()
  hideturtle()

  q = 100

  goto(-100, (-100 ** 2) / 50 + q)

  pendown()

  for x in range(-100, 101):
      width(abs(x/10) + 5)
      y = -(x ** 2) / 50
      goto(x, y + q)

  penup()
  goto(0,-20)
  color("orange")
  write("THANK YOU SIGCSE!", 
        align="center", 
        font=("Brush Script MT", 
              40, 
              'normal')
      )

---

# WebTiger-
# Python

- [webtigerpython.ethz.ch](https://webtigerpython.ethz.ch)
- Low Floor (Turtle, Robotics)
- High Ceiling (Events, Scientific Computing)
- Benchmarks
  - 2-3 Times slower than Native Python
  - Fast Rendering
