## Finding an address on google maps using command line
mapit.py launches the map in the browser of an address from the command line or clipboard

### Libraries required:
1.pyperclip
`$pip install pyperclip`
2. webbrowser
used to redirect to google maps
### Batch file:
`@ stored/python.exe stored/scriptfolder/mapit.py`

### Usage:
1. Open the command prompt and go to the directory where the mapit script is stored 
2. If you have an address copied to the clipboard you just need to open command prompt and 
Run command: `$mapit`
This will automatically redirect you to the address on google maps
3. You can also type the address and 
Run command: `$mapit Address`

### Example:
`$mapit 123, xyz place, abc country, pin:123456`
