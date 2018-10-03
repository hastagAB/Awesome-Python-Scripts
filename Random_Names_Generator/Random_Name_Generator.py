#! /usr/bin/env python3
from pathlib import Path
import argparse
import random

""" Generate a random line from a file without reading the entire file
    Inspired from: https://stackoverflow.com/a/35579149 """
def random_line(file_path):
    line_num = 0
    selected_line = ''
    with file_path.open(mode="r") as fp:
        while 1:
            line = fp.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()

""" Output a given number of random names """
def random_names(number_of_names = 1):
    first_names_file = Path("CSV_Database_Of_First_And_Last_Names/CSV_Database_of_First_Names.csv") 
    last_names_file = Path("CSV_Database_Of_First_And_Last_Names/CSV_Database_of_Last_Names.csv")
    if first_names_file.is_file() and last_names_file.is_file(): # Check if file exists
        for i in range(number_of_names):
            random_first_name = random_line(first_names_file)
            random_last_name = random_line(last_names_file)
            print(f'{random_first_name} {random_last_name}')

if __name__ == '__main__':
    # Accept command line argument for number of names required where default is 1
    parser = argparse.ArgumentParser(description='Generate Random Names')
    parser.add_argument('num', nargs='?', type=int, default=1)
    args = parser.parse_args()
    random_names(args.num)

