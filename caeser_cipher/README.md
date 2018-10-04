# Simple Caeser Cipher [En,De]coder

A simple implementation of a CLI tool to work with caeser ciphers.  The default implementation is ROT-13, but can be 
adjusted for any offset.  Works on files and string arguments passed via CLI.  

```bash
python3 caeser.py

usage: caeser.py [-h] [-d] [-o OFFSET] (-f FILE | -s STRING)
caeser.py: error: one of the arguments -f/--file -s/--string is required
``` 

```bash
python3 caeser.py -s "have you tried turning it off and on again?"
unir lbh gevrq gheavat vg bss naq ba ntnva?
```

```bash
python3 caeser.py -d -s "unir lbh gevrq gheavat vg bss naq ba ntnva?" 
have you tried turning it off and on again?
```

```bash
python3 caeser.py -s "have you tried turning it off and on again?" -o -4
dwra ukq pneaz pqnjejc ep kbb wjz kj wcwej?
```

