"""
utils.py - Helper utilities for Smart Code Reviewer.

Contains:
  - ANSI colour helpers for terminal output
  - JSON serialisation helpers
  - Summary statistics builder
"""

import json
import os
import sys
from typing import Dict, List

from analyzer import AnalysisResult, Finding


# ---------------------------------------------------------------------------
# Terminal colour support
# ---------------------------------------------------------------------------

# Respect NO_COLOR env var (https://no-color.org/) and non-TTY streams.
_COLOUR_ENABLED: bool = (
    sys.stdout.isatty()
    and os.environ.get("NO_COLOR") is None
    and os.environ.get("TERM") != "dumb"
)


class Colour:
    """ANSI escape codes used throughout the reporter."""

    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    MAGENTA = "\033[95m"
    WHITE   = "\033[97m"
    GREY    = "\033[90m"

    @staticmethod
    def apply(code: str, text: str) -> str:
        """Wrap *text* in *code* if colour output is enabled."""
        if not _COLOUR_ENABLED:
            return text
        return f"{code}{text}{Colour.RESET}"

    # Convenience shortcuts
    @staticmethod
    def bold(text: str) -> str:
        return Colour.apply(Colour.BOLD, text)

    @staticmethod
    def red(text: str) -> str:
        return Colour.apply(Colour.RED, text)

    @staticmethod
    def yellow(text: str) -> str:
        return Colour.apply(Colour.YELLOW, text)

    @staticmethod
    def cyan(text: str) -> str:
        return Colour.apply(Colour.CYAN, text)

    @staticmethod
    def green(text: str) -> str:
        return Colour.apply(Colour.GREEN, text)

    @staticmethod
    def grey(text: str) -> str:
        return Colour.apply(Colour.GREY, text)

    @staticmethod
    def magenta(text: str) -> str:
        return Colour.apply(Colour.MAGENTA, text)


# ---------------------------------------------------------------------------
# Severity helpers
# ---------------------------------------------------------------------------

_SEVERITY_COLOUR: Dict[str, str] = {
    "error":   Colour.RED,
    "warning": Colour.YELLOW,
    "info":    Colour.CYAN,
}

_SEVERITY_ICON: Dict[str, str] = {
    "error":   "✖",
    "warning": "⚠",
    "info":    "ℹ",
}


def format_severity(severity: str) -> str:
    """Return a coloured, icon-prefixed severity label."""
    icon = _SEVERITY_ICON.get(severity, "·")
    colour = _SEVERITY_COLOUR.get(severity, "")
    label = f"{icon} {severity.upper()}"
    return Colour.apply(colour, label)


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

CATEGORIES = ("Complexity", "Best Practices", "Style")

_CATEGORY_COLOUR: Dict[str, str] = {
    "Complexity":      Colour.MAGENTA,
    "Best Practices":  Colour.CYAN,
    "Style":           Colour.YELLOW,
}


def format_finding(finding: Finding) -> str:
    """Format a single :class:`Finding` as a human-readable string."""
    sev_label = format_severity(finding.severity)
    loc = (
        Colour.grey(f"line {finding.line}")
        if finding.line
        else Colour.grey("file-level")
    )
    sym = (
        f"  {Colour.bold(finding.symbol)}" if finding.symbol else ""
    )
    return f"  {sev_label:<22}  {loc}{sym}\n    {finding.message}"


def print_report(result: AnalysisResult) -> None:
    """Print a full human-readable report for one :class:`AnalysisResult`."""
    # ---- Header ----
    print()
    print(Colour.bold("=" * 64))
    print(
        Colour.bold("  Smart Code Reviewer")
        + "  "
        + Colour.grey(result.filepath)
    )
    print(Colour.bold("=" * 64))

    # ---- Stats line ----
    stats = (
        f"  {Colour.grey('Lines:')} {result.total_lines}"
        f"  {Colour.grey('Functions:')} {result.total_functions}"
        f"  {Colour.grey('Classes:')} {result.total_classes}"
    )
    print(stats)

    total = len(result.findings)
    if total == 0:
        print()
        print(Colour.green("  ✔  No issues found. Great work!"))
        print()
        return

    # Summary counts
    errors   = result.error_count()
    warnings = result.warning_count()
    infos    = result.info_count()
    summary_parts = []
    if errors:
        summary_parts.append(Colour.red(f"{errors} error{'s' if errors > 1 else ''}"))
    if warnings:
        summary_parts.append(Colour.yellow(f"{warnings} warning{'s' if warnings > 1 else ''}"))
    if infos:
        summary_parts.append(Colour.cyan(f"{infos} info"))

    print(f"  Found {total} issue{'s' if total > 1 else ''}: {', '.join(summary_parts)}")

    # ---- Category sections ----
    for category in CATEGORIES:
        findings = result.by_category(category)
        if not findings:
            continue

        cat_colour = _CATEGORY_COLOUR.get(category, "")
        print()
        print(Colour.apply(cat_colour, Colour.bold(f"  ── {category} ")))
        print(Colour.apply(cat_colour, "  " + "─" * 58))
        for finding in findings:
            print(format_finding(finding))
            print()

    # ---- Footer ----
    print(Colour.bold("=" * 64))
    print()


def print_multi_summary(results: List[AnalysisResult]) -> None:
    """Print a brief aggregate summary when multiple files are reviewed."""
    if len(results) <= 1:
        return

    total_issues = sum(len(r.findings) for r in results)
    total_errors = sum(r.error_count() for r in results)
    total_warns  = sum(r.warning_count() for r in results)

    print()
    print(Colour.bold("═" * 64))
    print(Colour.bold("  Aggregate Summary"))
    print(Colour.bold("═" * 64))
    print(f"  Files analysed : {len(results)}")
    print(f"  Total issues   : {total_issues}")
    print(
        f"  Errors         : {Colour.red(str(total_errors))}"
        f"   Warnings : {Colour.yellow(str(total_warns))}"
    )
    clean = sum(1 for r in results if len(r.findings) == 0)
    print(f"  Clean files    : {Colour.green(str(clean))}")
    print(Colour.bold("═" * 64))
    print()


# ---------------------------------------------------------------------------
# JSON serialisation
# ---------------------------------------------------------------------------

def result_to_dict(result: AnalysisResult) -> dict:
    """Convert an :class:`AnalysisResult` to a plain dict (JSON-serialisable)."""
    return {
        "filepath": result.filepath,
        "summary": {
            "total_lines":     result.total_lines,
            "total_functions": result.total_functions,
            "total_classes":   result.total_classes,
            "total_issues":    len(result.findings),
            "errors":          result.error_count(),
            "warnings":        result.warning_count(),
            "infos":           result.info_count(),
        },
        "findings": [
            {
                "category": f.category,
                "severity": f.severity,
                "line":     f.line,
                "symbol":   f.symbol,
                "message":  f.message,
            }
            for f in result.findings
        ],
    }


def print_json(results: List[AnalysisResult]) -> None:
    """Serialise results to JSON and write to stdout."""
    payload = [result_to_dict(r) for r in results]
    print(json.dumps(payload, indent=2))
