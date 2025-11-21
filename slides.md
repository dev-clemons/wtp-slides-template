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

---
layout: wtp-2-cols
code: |
  from rootRobot import * 

  repeat 4:
      forward(100)
      left(90)
---

# RootRobot

- Same syntax as turtle
- Draw turtle images on whiteboard

---

# Invisible improvements

- Better cacheing (full offline usage)
- Increase in the URL link size limit
- Python 3.13.2
- PixiJS7 -> PixiJS8 (Performance)