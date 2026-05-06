#!/usr/bin/env python3
"""
reviewer.py - CLI entry point for Smart Code Reviewer.

Usage examples:
    python reviewer.py myfile.py
    python reviewer.py src/main.py src/utils.py
    python reviewer.py *.py --json
    python reviewer.py myfile.py --no-color
"""

import argparse
import os
import sys

# Allow running from any working directory (add package root to path).
sys.path.insert(0, os.path.dirname(__file__))

from analyzer import FileAnalyzer, ReviewConfig
from utils import print_json, print_multi_summary, print_report


# ---------------------------------------------------------------------------
# Exit codes (follow UNIX conventions)
# ---------------------------------------------------------------------------

EXIT_OK          = 0   # No issues found
EXIT_ISSUES      = 1   # Issues found (warnings / infos)
EXIT_ERRORS      = 2   # Hard errors found
EXIT_IO_ERROR    = 3   # File read / parse failure
EXIT_USAGE_ERROR = 4   # Bad CLI arguments


# ---------------------------------------------------------------------------
# CLI definition
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """Return the configured argument parser."""
    parser = argparse.ArgumentParser(
        prog="reviewer",
        description=(
            "Smart Code Reviewer — static analysis tool for Python files.\n"
            "Analyses code quality, time complexity heuristics, and best-practice violations."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python reviewer.py myfile.py
  python reviewer.py src/a.py src/b.py
  python reviewer.py myfile.py --json
  python reviewer.py myfile.py --max-lines 30 --max-args 4
        """,
    )

    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="+",
        help="One or more Python source files to analyse.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        default=False,
        help="Output results as JSON instead of the human-readable report.",
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="Disable ANSI colour output.",
    )

    parser.add_argument(
        "--max-lines",
        metavar="N",
        type=int,
        default=ReviewConfig.MAX_FUNCTION_LINES,
        help=(
            f"Maximum lines per function before a style warning is raised "
            f"(default: {ReviewConfig.MAX_FUNCTION_LINES})."
        ),
    )

    parser.add_argument(
        "--max-args",
        metavar="N",
        type=int,
        default=ReviewConfig.MAX_FUNCTION_ARGS,
        help=(
            f"Maximum function arguments before a best-practice warning is raised "
            f"(default: {ReviewConfig.MAX_FUNCTION_ARGS})."
        ),
    )

    return parser


# ---------------------------------------------------------------------------
# Core runner
# ---------------------------------------------------------------------------

def run(args: argparse.Namespace) -> int:
    """
    Execute the review for all specified files.

    Returns an exit code (see module-level constants).
    """
    # Honour --no-color by patching the environment variable that utils.py
    # respects without needing to pass state through function arguments.
    if args.no_color:
        os.environ["NO_COLOR"] = "1"

    # Build shared config from CLI flags.
    config = ReviewConfig()
    config.MAX_FUNCTION_LINES = args.max_lines
    config.MAX_FUNCTION_ARGS  = args.max_args

    results = []
    had_io_error = False

    for filepath in args.files:
        # Validate extension (allow but warn on non-.py files).
        if not filepath.endswith(".py"):
            _warn(f"'{filepath}' does not appear to be a Python file. Skipping.")
            continue

        try:
            analyzer = FileAnalyzer(filepath, config=config)
            result   = analyzer.analyze()
            results.append(result)

        except FileNotFoundError:
            _error(f"File not found: {filepath}")
            had_io_error = True

        except SyntaxError as exc:
            _error(
                f"Syntax error in '{filepath}' at line {exc.lineno}: {exc.msg}"
            )
            had_io_error = True

        except OSError as exc:
            _error(f"Cannot read '{filepath}': {exc.strerror}")
            had_io_error = True

    if not results:
        _error("No files were successfully analysed.")
        return EXIT_IO_ERROR if had_io_error else EXIT_USAGE_ERROR

    # ---- Output ----
    if args.json:
        print_json(results)
    else:
        for result in results:
            print_report(result)
        if len(results) > 1:
            print_multi_summary(results)

    # ---- Determine exit code ----
    if had_io_error:
        return EXIT_IO_ERROR

    total_errors = sum(r.error_count() for r in results)
    if total_errors:
        return EXIT_ERRORS

    total_issues = sum(len(r.findings) for r in results)
    if total_issues:
        return EXIT_ISSUES

    return EXIT_OK


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _warn(message: str) -> None:
    print(f"[WARNING] {message}", file=sys.stderr)


def _error(message: str) -> None:
    print(f"[ERROR] {message}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = build_parser()
    args   = parser.parse_args()
    sys.exit(run(args))


if __name__ == "__main__":
    main()
