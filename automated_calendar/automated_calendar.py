'''
THIS CODE CREATES FOLDERS FOR EACH FY OF OUR COMPANY, WHERE WE COULD
FIND 12 OTHER FOLDERS NAMED AFTER EACH MONTH OF THE YEAR.
'''

#Import modules and libraries we'll use
from pathlib import Path

#Create the folders where we'll store our automated calendar
months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i,month in enumerate(months):
    Path(f'Year1/{i+1}.{month}').mkdir(parents=True,exist_ok=True)
    Path(f'Year2/{i+1}.{month}').mkdir(parents=True,exist_ok=True)
    Path(f'Year3/{i+1}.{month}').mkdir(parents=True,exist_ok=True)
    Path(f'Year4/{i+1}.{month}').mkdir(parents=True,exist_ok=True)



