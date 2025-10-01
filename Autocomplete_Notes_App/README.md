# Autocomplete Notes App

## Overview

The Autocomplete Notes App is a simple graphical user interface (GUI) application that allows users to take notes efficiently. It features an autocomplete functionality, where suggestions for completing words are displayed as the user types. This app is built using Python and the Tkinter library for the GUI, with the addition of word suggestions from a predefined word list.

## Features

- **Text Input**: A large text area for users to enter notes.
- **Autocomplete**: As users type, a suggestion box displays the full word based on the entered text.
- **Tab Functionality**: Users can press the Tab key to automatically fill in the suggested word into the text area.
- **Save Notes**: Users can choose a filename to save their notes to a `.txt` file.
- **Dynamic Sizing**: The app window resizes based on user actions.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- A `wordlist.txt` file containing words for autocomplete suggestions.

## Installation

1. Clone the repository or download the source code files.
2. Ensure you have Python 3.x installed on your machine.
3. Make sure `wordlist.txt` is in the same directory as the application code. This file should contain words, each on a new line.

## Usage

1. Open a terminal or command prompt and navigate to the directory containing the application code.
2. Run the application using the command:
   ```bash
   python app.py
