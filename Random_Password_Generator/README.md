# Programs
## [PasswordGenerator.py](./PasswordGenerator.py)
This program randomly generates a secure password using a mix of letters, both caps on and off, numbers, and punctuation, then outputs the results and saves them as a text document.

## [createPassword.py](./createPassword.py)
This program uses the Python 3 module `secrets` to create a pseudo random password with alphanumeric, numbers, and special characters. The output will be printed into the terminal.

# Requirements
* [PasswordGenerator.py](./PasswordGenerator.py) can use Python 3 and higher or Python 2 and higher
* [createPassword.py](./createPassword.py) can run on python 3.6 or higher or for Python 2 do:
  * `cd Random_Password_Generator/` to change directory into this folder. 
  * Create virtual environment with `virtualvenv env`
  * do `source venv/bin/activate` to activate virtual environment.
  * do `pip install -r requirements.txt` to install python2-secrets
  * **TIP**: to deactivate virtual environment, do `deactivate`. 

# Usage

For Windows users:

```bash
$ python PasswordGenerator.py
```

For Mac/Linux/Unix users:

```bash
$ ./PasswordGenerator.py
```