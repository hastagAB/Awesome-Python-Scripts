
# Directory Tree Visualizer

This project is useful for visualizing the relationship between files and directories and making their positioning easy to comprehend.

## Libraries Used

* Docopt
* Argparse
* os
* walkdir

## Usage

Directory Tree Generator depends on third party libraries and you will first need to install the application's dependencies:

```bash
pip install walkdir
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/hastagAB/Awesome-Python-Scripts.git
```

Go to the project directory

```bash
  cd Awesome-Python-Scripts\Directory_Tree_Generator
```

Run ```directory_tree_generator.py```. You will have to provide the absolute path of the directory you want to visualize

```python
  python directory_tree_generator.py "path\to\directory" 
```

A full visualizer would be displayed along with the levels.

```bash
 1 - D:\\Cheatsheet Template
  2 - CPP
   3 - Beginnig Level Programs
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - New Category 2
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - New Category 3
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - New Category4
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
  2 - Python
   3 - Arrays
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - Easy String prog
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - File Handling Programs
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - Good Programs to Practise
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - Miscellaneous
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - New Category 3 (another copy)
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - New Category 3 (copy)
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - Regex Programs
    4 - index.html
    4 - prism.css
    4 - prism.js
   3 - Searching Algorithm
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
   3 - Sorting Algortihm
    4 - index.html
    4 - prism.css
    4 - prism.js
    4 - style.css
```
