# sudoku-solver

This is a script to solve 9x9 sudoku matrix using python.

### How to use it?

1. edit app.py to add your sudoku matrix. (Fill `0` for empty cells.)

```
For example,

[[8, 1, 0, 0, 3, 0, 0, 2, 7],
[0, 6, 2, 0, 5, 0, 0, 9, 0],
[0, 7, 0, 0, 0, 0, 0, 0, 0],
[0, 9, 0, 6, 0, 0, 1, 0, 0],
[1, 0, 0, 0, 2, 0, 0, 0, 4],
[0, 0, 8, 0, 0, 5, 0, 7, 0],
[0, 0, 0, 0, 0, 0, 0, 8, 0],
[0, 2, 0, 0, 1, 0, 7, 5, 0],
[3, 8, 0, 0, 7, 0, 0, 4, 2]]
```

2.  run the script.

```
python3 app.py
```

3. This will give you output on the console. Output will contain the input sudoku matrix and the solved sudoku matrix.

```
INPUT =>



8 1 0 | 0 3 0 | 0 2 7
0 6 2 | 0 5 0 | 0 9 0
0 7 0 | 0 0 0 | 0 0 0
---------------------
0 9 0 | 6 0 0 | 1 0 0
1 0 0 | 0 2 0 | 0 0 4
0 0 8 | 0 0 5 | 0 7 0
---------------------
0 0 0 | 0 0 0 | 0 8 0
0 2 0 | 0 1 0 | 7 5 0
3 8 0 | 0 7 0 | 0 4 2



OUTPUT =>



8 1 9 | 4 3 6 | 5 2 7
4 6 2 | 7 5 1 | 3 9 8
5 7 3 | 2 9 8 | 4 1 6
---------------------
2 9 4 | 6 8 7 | 1 3 5
1 5 7 | 9 2 3 | 8 6 4
6 3 8 | 1 4 5 | 2 7 9
---------------------
7 4 5 | 3 6 2 | 9 8 1
9 2 6 | 8 1 4 | 7 5 3
3 8 1 | 5 7 9 | 6 4 2
```
