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
  persist: false
# use UnoCSS (experimental)
wakeLock: "build"
# aspect ratio for the slides
aspectRatio: 16/9
css: unocss
---

# New Features in WTP 2025

Clemens Bachmann

---
layout: wtp-2-cols
code: |
  import sqlite3

  DB = "fk_demo.db"

  with sqlite3.connect(DB) as conn:
      conn.execute("PRAGMA foreign_keys = ON;")  # must enable FK enforcement in SQLite

      # Parent table (authors) and child table (books) with a foreign key constraint
      conn.executescript("""
      CREATE TABLE IF NOT EXISTS authors (
          id INTEGER PRIMARY KEY,    -- parent primary key
          name TEXT NOT NULL
      );
      CREATE TABLE IF NOT EXISTS books (
          id INTEGER PRIMARY KEY,
          title TEXT NOT NULL,
          author_id INTEGER,         -- child column that references authors.id
          FOREIGN KEY(author_id) REFERENCES authors(id)
      );
      """)

      # Clear tables for repeated runs
      conn.execute("DELETE FROM books;")
      conn.execute("DELETE FROM authors;")

      # Insert one valid parent row
      conn.execute("INSERT INTO authors (id, name) VALUES (?, ?);", (1, "A. Writer"))

      # Valid insert: author_id matches existing authors.id
      conn.execute("INSERT INTO books (title, author_id) VALUES (?, ?);", ("Good Book", 1))
      print("Inserted book with valid author_id=1")

      # Invalid insert: author_id 999 does not exist — this will raise sqlite3.IntegrityError
      try:
          conn.execute("INSERT INTO books (title, author_id) VALUES (?, ?);", ("Bad Book", 999))
      except sqlite3.IntegrityError as e:
          print("Failed to insert book with invalid author_id=999:", e)

      # Show current rows
      print("authors:", conn.execute("SELECT * FROM authors;").fetchall())
      print("books:", conn.execute("SELECT * FROM books;").fetchall())
      conn.commit()
---

# Database

- Foreign Keys
- Peaking
- Semester Thesis by Selin Baris

---
layout: wtp-2-cols
code: |
  # rowYourBoat.py
  # Demonstrates how to build a musical canon.
  
  from music import *
  
  # Create the necessary musical data
  rowYourBoatScore = Score("Row Your Boat", 108.0)  # tempo is 108 bpm
  
  flutePart    = Part(FLUTE, 0)        # flute part on channel 0
  trumpetPart  = Part(TRUMPET, 1)      # trumpet part on channel 1
  clarinetPart = Part(CLARINET, 2)     # clarinet part on channel 2
  
  themePhrase = Phrase(0.0)            # theme starts at the beginning
  
  # "Row, row, row your boat gently down the stream"
  pitches1   = [C4, C4, C4,  D4, E4, E4,  D4, E4,  F4, G4]
  durations1 = [QN, QN, DEN, SN, QN, DEN, SN, DEN, SN, HN]
  
  # "merrily, merrily, merrily, merrily"
  pitches2   = [C5,  C5,  C5,  G4,  G4,  G4,  E4,  E4,  E4,  C4,
                C4,  C4]
  durations2 = [ENT, ENT, ENT, ENT, ENT, ENT, ENT, ENT, ENT, ENT,
                ENT, ENT]
  
  # "life is but a dream."
  pitches3   = [G4,  F4, E4,  D4, C4]
  durations3 = [DEN, SN, DEN, SN, HN]
  
  # add the notes to the theme
  themePhrase.addNoteList(pitches1, durations1)
  themePhrase.addNoteList(pitches2, durations2)
  themePhrase.addNoteList(pitches3, durations3)
  
  # make two new phrases and change start times to make a round
  response1Phrase = themePhrase.copy()
  response2Phrase = themePhrase.copy()
  
  response1Phrase.setStartTime(4.0)     # start after 4 quarter notes
  response2Phrase.setStartTime(8.0)     # start after 8 quarter notes
  
  # play different parts in different registers
  Mod.transpose(themePhrase, 12)         # one octave higher
  Mod.transpose(response2Phrase, -12)    # one octave lower
  
  # play each phrase twice
  Mod.repeat(themePhrase, 2)
  Mod.repeat(response1Phrase, 2)
  Mod.repeat(response2Phrase, 2)
  
  # add phrases to corresponding parts
  flutePart.addPhrase(themePhrase)
  trumpetPart.addPhrase(response1Phrase)
  clarinetPart.addPhrase(response2Phrase)
  
  # add parts to score
  rowYourBoatScore.addPart(flutePart)
  rowYourBoatScore.addPart(trumpetPart)
  rowYourBoatScore.addPart(clarinetPart)
  
  # play score
  Play.midi(rowYourBoatScore)
---

# JythonMusic

- 127 Instruments
- WebMidi Support
- Midi export
- Bachelor Thesis by Natasha Savic

---
layout: wtp-2-cols
code: |
  from rootRobot import * 

  repeat 4:
      forward(100)
      left(90)
device: RootRobot (Beta)
---

# RootRobot

- Same syntax as turtle
- Draw turtle images on whiteboard
- IPA by Justin Calle

---
layout: wtp-2-cols
code: |
  # Gp7a.py
  from gpanel import *
  from gturtle import *

  makeGPanel(-30, 30, 0, 60)

  x = -30
  while x <= 30:
      if x <= 0:
          setColor("magenta")
      else:    
          setColor("cyan")
      line(0, 50, x, 0)
      x = x + 1
      delay(50)

  makeTurtle()
  setFillColor("magenta")
  setPenColor("magenta")
  startPath()
  repeat 5:
      fd(160)
      rt(144)
  fillPath()
---

# Tabs

- If multiple libraries have visual output
- Pygame / Gamegrid / Gpanel do not work together
- Due to databases visualizer by Selin Baris

---

# Documentation

[Open in seperate window](https://webtigerpython.ethz.ch/#?code=NobwRAdghgtgpmAXGGUCWEB0AHAnmAGjABMoAXKJMAMwCcB7GAAgHMyBXWsgGzibRjZ6XJgCoAOrXERJ0gM5wyAMTTduAYXrdhACnEooLOBAr6AlLIgKyABWObttPQaMmo5y3Ipcb5ABY6FlIQtHDYcORMAKyIlkzxTNTEOgCMAGwADEHSCUxcqQAsBdkQ1KrcvmQBJWAAvgC6QA)
- What should be improved?
- icons?

---

# Invisible improvements

- Open source (MPL v2)
- Robotics in separate repository (also open source)
- Better cacheing (full offline usage)
- Increase in the URL link size limit [Long Link](https://www.notion.so/insane-langer-link-2484286549e9802e865feedcc84e53a6?source=copy_link)
- Python 3.13.2
- PixiJS7 -> PixiJS8 (Performance)

---

# Userbase

2'500 Users on a weekday
Mostly Switerland and Germany
Many smaller coundries
  - USA
  - Austria
  - France
  - Portugal
  - Danmark

[logging ETH](https://es.kubi.inf.ethz.ch/login?next=%2F)

---
layout: wtp-2-cols
code: |
  import matplotlib.pyplot as plt
  import matplotlib.dates as mdates
  from datetime import datetime
  import numpy as np
  import requests

  # URL to request data from
  url = 'https://api.webtigerpython.ethz.ch/dailyuserscount'

  try:
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data (assuming it's in JSON format)
        data = response.json()  # Use response.text for plain text or HTML
    else:
        print(f"Error: Received status code {response.status_code}")
        data = []  # Empty data if request fails
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    data = []  # Empty data if exception occurs

  # Check if data is available
  if not data:
    print("No data available to plot.")
    exit()

  # Extract dates and values
  dates = [datetime.strptime(item['date'], '%Y-%m-%d') for item in data]
  users = [item['unique_users'] for item in data]

  # Calculate statistics
  max_users = max(users)
  min_users = min(users)
  avg_users = sum(users) / len(users)

  # Create figure and axis
  plt.figure(figsize=(14, 8))

  # Plot the data
  plt.plot(dates, users, marker='o', markersize=3, linewidth=1, alpha=0.7, color='steelblue', label='Daily Users')

  # Format x-axis to show dates properly
  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
  plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
  plt.gcf().autofmt_xdate()

  # Add labels and title
  plt.xlabel('Date', fontsize=12)
  plt.ylabel('Unique Users', fontsize=12)
  plt.title('Daily Unique Users Over Time', fontsize=14, fontweight='bold')

  # Add grid for better readability
  plt.grid(True, alpha=0.3)

  # Add a 7-day moving average to show the trend
  window_size = 7
  moving_avg = np.convolve(users, np.ones(window_size)/window_size, mode='valid')
  moving_avg_dates = dates[window_size-1:]
  plt.plot(moving_avg_dates, moving_avg, color='red', linewidth=2, label=f'{window_size}-day Moving Average')

  # Add overall average as a horizontal line
  plt.axhline(y=avg_users, color='green', linestyle='--', linewidth=2, label=f'Overall Average ({avg_users:.0f})')

  # Add legend
  plt.legend()

  # Add statistics to the plot
  plt.text(0.01, 0.87, f'Max: {max_users}\nMin: {min_users}\nAvg: {avg_users:.0f}', 
        transform=plt.gca().transAxes, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

  # Adjust layout and show plot
  plt.tight_layout()
  plt.show()
---

# User Statistics

- Daily Users (not IP)

---
layout: wtp-2-cols
code: |
  import matplotlib.pyplot as plt
  import requests
  import json

  # URL to request data from
  url = 'https://api.webtigerpython.ethz.ch/librariescount'

  try:
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data (assuming it's in JSON format)
        data = response.json()  # Use response.text for plain text or HTML
    else:
        print(f"Error: Received status code {response.status_code}")

  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

  # URL to request data from
  url = 'https://api.webtigerpython.ethz.ch/errortypescount'

  try:
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data (assuming it's in JSON format)
        data2 = response.json()  # Use response.text for plain text or HTML
    else:
        print(f"Error: Received status code {response.status_code}")

  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

  # Initialize variables for grouping
  grouped_count = 0
  grouped_label = 'Others'
  final_data = []

  total_count = sum(item['count'] for item in data2)

  print(total_count)

  # Process the data
  for library, count in data:
    if count < 200:
        grouped_count += count
    else:
        final_data.append([library, count])

  # final_data.append([grouped_label, grouped_count])

  # Extract counts and library names
  counts = [item[1] for item in final_data]
  library_names = [item[0] for item in final_data]

  # Create a bar chart
  plt.figure(figsize=(10, 6))
  bars = plt.bar(library_names, counts, color=plt.cm.Set1.colors)

  plt.ylabel('Count', fontsize=15)
  plt.title('Error Reports by Library', fontsize=20, pad=20)
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()  # Adjust layout to make room for labels

  # Add statistics to the plot
  plt.text(0.6, 0.95, f'Total collected error messages: {total_count}', 
      transform=plt.gca().transAxes, verticalalignment='top',
      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

  # Show the plot
  plt.show()
---

# Error Messages

- Only about 25% of users send error reports


---