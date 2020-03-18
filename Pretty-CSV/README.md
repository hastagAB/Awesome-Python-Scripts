# Pretty CSV

This script pretty-prints CSV input into a table output for easier readibility. The script reads from stdin and writes into stdout for pipe compatibility.

## Examples
Read from local file
```sh
python3 pretty-csv.py < csv-file.csv
```

Read from `curl`
```sh
curl -fsSL https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv | python3 pretty-csv.py
```

Pipe to `less` for better navigation
```sh
python3 pretty-csv.py < long-csv-file.csv | less -S
```
