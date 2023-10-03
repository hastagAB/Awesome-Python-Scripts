<h1 align="center">Variable Combinations Generator</h1>
<br>
This Python script provides a simple way to generate all possible combinations of True and False values for a given list of variables. It uses the itertools.product function to create these combinations and displays the result in a user-friendly format.
<br>

## Usage

- Make sure you have Python installed on your system.
- Clone or download this repository to your local machine.
- Navigate to the directory where the script is located using the command line.
- Run the script using the following command:
  ```python variable_combinations_generator.py```
- Follow the on-screen instructions to enter a list of space-separated variable names. Press Enter when you're done.
- The script will generate all possible combinations of True and False values for the given variables and display the results in a human-readable format.

## Example

<br>
Let's say you want to generate combinations for variables A, B, and C. You would input the following:
<br>

```Enter a list of space-separated variables: A B C```
<br>

The script will then produce the following output:

```
{'A': False, 'B': False, 'C': False}
{'A': False, 'B': False, 'C': True}
{'A': False, 'B': True, 'C': False}
{'A': False, 'B': True, 'C': True}
{'A': True, 'B': False, 'C': False}
{'A': True, 'B': False, 'C': True}
{'A': True, 'B': True, 'C': False}
{'A': True, 'B': True, 'C': True}
```
## Function documentation

```generate_variable_combinations(variables)```

Generate all possible combinations of True and False values for a given list of variables.

Arguments:
variables (list): A list of variable names.

Returns:
list of tuples: A list of tuples where each tuple represents a combination of True and False values for the variables.

Example:

```
>>> generate_variable_combinations(['A', 'B'])
[(False, False), (False, True), (True, False), (True, True)]

>>> generate_variable_combinations(['X', 'Y', 'Z'])
[(False, False, False), (False, False, True), (False, True, False),
 (False, True, True), (True, False, False), (True, False, True),
 (True, True, False), (True, True, True)]
```
