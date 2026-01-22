from itertools import product

def generate_variable_combinations(variables):
    """
    Generate all possible combinations of True and False values for a given list of variables.

    Args:
        variables (list): A list of variable names.

    Returns:
        list of tuples: A list of tuples where each tuple represents a combination of True and False
        values for the variables.

    Example:
    >>> generate_variable_combinations(['A', 'B'])
    [(False, False), (False, True), (True, False), (True, True)]
    
    >>> generate_variable_combinations(['X', 'Y', 'Z'])
    [(False, False, False), (False, False, True), (False, True, False),
     (False, True, True), (True, False, False), (True, False, True),
     (True, True, False), (True, True, True)]
    """
    return list(product([False, True], repeat=len(variables)))

if __name__ == "__main__":
    input_variables = input("Enter a list of space-separated variables: ").strip()
    variables = input_variables.split()
    combinations = generate_variable_combinations(variables)
    for combo in combinations:
        print(dict(zip(variables, combo)))
