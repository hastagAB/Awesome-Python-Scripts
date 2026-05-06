# Smart Code Reviewer 🔍
BY AVANTHIKA

A zero-dependency Python static analysis tool that reviews your Python source
files and reports on **code quality**, **time-complexity patterns**, and
**best-practice violations** — all from the command line.

Built entirely with the Python standard library (`ast`, `argparse`, `json`).

---

## Features

| Category | Check |
|---|---|
| **Complexity** | Nested loops (possible O(n²)) |
| **Best Practices** | Missing module / class / function docstrings |
| **Best Practices** | `while` loops without obvious termination |
| **Best Practices** | Functions with too many arguments (>5) |
| **Style** | Long functions (>50 lines) |
| **Style** | Non-snake_case function names |

Additional capabilities:

- ✅ Analyse **multiple files** in one command
- ✅ **JSON output** mode (`--json`) for CI/CD pipelines
- ✅ **Adjustable thresholds** (`--max-lines`, `--max-args`)
- ✅ Colour output with `NO_COLOR` support
- ✅ Meaningful exit codes for scripting

---

## Requirements

- Python **3.8+**
- No external packages

---

## Installation

```bash
# Clone / download the project
git clone https://github.com/yourname/smart-code-reviewer.git
cd smart-code-reviewer

# (Optional) make the CLI executable
chmod +x reviewer.py
```

No `pip install` step required.

---

## Usage

### Basic review

```bash
python reviewer.py myfile.py
```

### Review multiple files

```bash
python reviewer.py src/main.py src/utils.py src/models.py
```

### Glob expansion (shell feature)

```bash
python reviewer.py src/*.py
```

### JSON output (great for CI)

```bash
python reviewer.py myfile.py --json
```

### Custom thresholds

```bash
# Flag functions longer than 30 lines, or with more than 4 args
python reviewer.py myfile.py --max-lines 30 --max-args 4
```

### Disable colour (e.g. when piping output)

```bash
python reviewer.py myfile.py --no-color
# or use the standard env var:
NO_COLOR=1 python reviewer.py myfile.py
```

### Full help

```bash
python reviewer.py --help
```

---

## Example output

```
================================================================
  Smart Code Reviewer  examples/sample_bad.py
================================================================
  Lines: 72  Functions: 4  Classes: 1
  Found 8 issues: 2 warnings, 3 warnings, 3 infos

  ── Complexity ──────────────────────────────────────────────
  ⚠ WARNING        line 18  [process_data]
    Nested for-loop detected. This may indicate O(n²) or worse time complexity.

  ── Best Practices ──────────────────────────────────────────
  ⚠ WARNING        line 12  [DataLoader]
    Class is missing a docstring.

  ⚠ WARNING        line 25  [process_data]
    Public function is missing a docstring.

  ⚠ WARNING        line 40  [connect]
    Function has 6 arguments (threshold: 5). Consider using a config object or dataclass.

  ℹ INFO            line 34
    while-loop found. Ensure the termination condition is guaranteed to prevent infinite loops.

  ── Style ────────────────────────────────────────────────────
  ⚠ WARNING        line 25  [process_data]
    Function is 52 lines long (threshold: 50).

  ℹ INFO            line 60  [loadData]
    Function name 'loadData' does not follow snake_case convention.

================================================================
```

### JSON output

```json
[
  {
    "filepath": "examples/sample_bad.py",
    "summary": {
      "total_lines": 72,
      "total_functions": 4,
      "total_classes": 1,
      "total_issues": 7,
      "errors": 0,
      "warnings": 5,
      "infos": 2
    },
    "findings": [
      {
        "category": "Complexity",
        "severity": "warning",
        "line": 18,
        "symbol": "process_data",
        "message": "Nested for-loop detected. This may indicate O(n²) or worse time complexity."
      }
    ]
  }
]
```

---

## Running the tests

```bash
# From the project root
python -m unittest discover -s tests -v
```

Expected output:

```
test_acceptable_arg_count_not_flagged (test_analyzer.TestTooManyArguments) ... ok
test_camel_case_function_flagged (test_analyzer.TestNamingConvention) ... ok
test_class_without_docstring_flagged (test_analyzer.TestMissingDocstrings) ... ok
...
----------------------------------------------------------------------
Ran 18 tests in 0.042s

OK
```

---

## Project structure

```
smart-code-reviewer/
├── reviewer.py          # CLI entry point (argparse, exit codes)
├── analyzer.py          # Core AST visitor + data model
├── utils.py             # Colour output, report formatting, JSON helpers
├── requirements.txt     # No external deps — standard library only
├── README.md
└── tests/
    └── test_analyzer.py # 18 unit tests covering all checks
```

---

## Exit codes

| Code | Meaning |
|---|---|
| `0` | No issues found |
| `1` | Warnings / info found |
| `2` | Errors found |
| `3` | File read / parse failure |
| `4` | Bad CLI arguments |

Useful for CI pipelines:

```bash
python reviewer.py src/main.py || echo "Review failed"
```

---

## Configuration reference

| Flag | Default | Description |
|---|---|---|
| `--json` | off | Output results as JSON |
| `--no-color` | off | Disable ANSI colour |
| `--max-lines N` | 50 | Max lines per function |
| `--max-args N` | 5 | Max function arguments |

---

## Extending the tool

All analysis logic lives in `analyzer.py` as an `ast.NodeVisitor` subclass.
To add a new check:

1. Add a `visit_<NodeType>` method to `CodeAnalyzerVisitor`.
2. Call `self._add(category, severity, line, message)` to record a finding.
3. Add a corresponding unit test in `tests/test_analyzer.py`.

---

## Contributing

Pull requests are welcome. Please:
- Follow PEP 8
- Add tests for any new check
- Keep zero external dependencies

---

## License

MIT © 2026
