#Importance Checker

A simple program to check for a person or topic's "importance" by checking whether the search value's possible Wikipedia page appears in the top *x* Google search results, where *x* is set to 10 by default.

##Instructions

Type these commands in the terminal:

`pip install beautifulsoup`
 
`pip install google`
 
 
Now type:

`ImportanceChecker.py`

The program will run, and test a user-inputted value if in *main*. Use `import ImportanceChecker` to use it in your python project.


###Notes:
* *ImportanceChecker* runs relatively slow to help prevent Google from blocking the user's IP address. One can modify the time delay in between requests to speed the function up by changing the third parameter to something other than its default, *1*.