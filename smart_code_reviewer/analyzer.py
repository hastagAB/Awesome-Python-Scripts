"""
analyzer.py - Core AST analysis engine for Smart Code Reviewer.

Uses Python's built-in `ast` module to walk the syntax tree and
collect structured findings across three categories:
  - Complexity   : nested loops, while-loop termination risk
  - Best Practices: missing docstrings, too many arguments
  - Style        : long functions, naming conventions
"""

import ast
from dataclasses import dataclass, field
from typing import List, Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    """Represents a single issue found during analysis."""

    category: str           # "Complexity" | "Best Practices" | "Style"
    severity: str           # "error" | "warning" | "info"
    line: Optional[int]     # Source line number (1-based), None for file-level
    message: str            # Human-readable description
    symbol: str = ""        # Function / class name (if applicable)

    def __str__(self) -> str:
        loc = f"line {self.line}" if self.line else "file-level"
        sym = f" [{self.symbol}]" if self.symbol else ""
        return f"  [{self.severity.upper():7s}] {loc}{sym}: {self.message}"


@dataclass
class AnalysisResult:
    """Aggregated results for a single file."""

    filepath: str
    findings: List[Finding] = field(default_factory=list)
    total_functions: int = 0
    total_classes: int = 0
    total_lines: int = 0

    # Convenience helpers
    def by_category(self, category: str) -> List[Finding]:
        return [f for f in self.findings if f.category == category]

    def error_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "error")

    def warning_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "warning")

    def info_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "info")


# ---------------------------------------------------------------------------
# Configuration (thresholds)
# ---------------------------------------------------------------------------

class ReviewConfig:
    """Centralised thresholds so they're easy to tune."""

    MAX_FUNCTION_LINES: int = 50
    MAX_FUNCTION_ARGS: int = 5
    CATEGORIES = ("Complexity", "Best Practices", "Style")


# ---------------------------------------------------------------------------
# Visitor
# ---------------------------------------------------------------------------

class CodeAnalyzerVisitor(ast.NodeVisitor):
    """
    Walks an AST and accumulates findings.

    Call `.visit(tree)` then read `.findings`, `.func_count`, `.class_count`.
    """

    def __init__(self, source_lines: List[str], config: ReviewConfig):
        self._lines = source_lines
        self._cfg = config
        self.findings: List[Finding] = []
        self.func_count: int = 0
        self.class_count: int = 0

        # Tracks nesting depth so we can flag nested loops.
        self._loop_depth: int = 0

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _add(
        self,
        category: str,
        severity: str,
        line: Optional[int],
        message: str,
        symbol: str = "",
    ) -> None:
        self.findings.append(
            Finding(
                category=category,
                severity=severity,
                line=line,
                message=message,
                symbol=symbol,
            )
        )

    def _function_line_count(self, node: ast.FunctionDef) -> int:
        """Return the number of source lines spanned by a function node."""
        return node.end_lineno - node.lineno + 1  # type: ignore[attr-defined]

    def _has_docstring(self, node: ast.AST) -> bool:
        """Return True if the first statement is a string literal (docstring)."""
        body = getattr(node, "body", [])
        if body and isinstance(body[0], ast.Expr):
            val = body[0].value
            return isinstance(val, ast.Constant) and isinstance(val.value, str)
        return False

    # ------------------------------------------------------------------
    # Visitors
    # ------------------------------------------------------------------

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802
        self._check_function(node)
        self.generic_visit(node)

    # async defs get the same treatment
    visit_AsyncFunctionDef = visit_FunctionDef  # type: ignore[assignment]

    def visit_ClassDef(self, node: ast.ClassDef) -> None:  # noqa: N802
        self.class_count += 1
        if not self._has_docstring(node):
            self._add(
                "Best Practices",
                "warning",
                node.lineno,
                "Class is missing a docstring.",
                symbol=node.name,
            )
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:  # noqa: N802
        self._check_loop(node, loop_type="for")

    def visit_While(self, node: ast.While) -> None:  # noqa: N802
        self._check_loop(node, loop_type="while")

    # ------------------------------------------------------------------
    # Check helpers
    # ------------------------------------------------------------------

    def _check_function(self, node: ast.FunctionDef) -> None:
        self.func_count += 1
        name = node.name

        # --- Style: long function ---
        line_count = self._function_line_count(node)
        if line_count > self._cfg.MAX_FUNCTION_LINES:
            self._add(
                "Style",
                "warning",
                node.lineno,
                f"Function is {line_count} lines long "
                f"(threshold: {self._cfg.MAX_FUNCTION_LINES}).",
                symbol=name,
            )

        # --- Best Practices: missing docstring ---
        if not self._has_docstring(node) and not name.startswith("_"):
            self._add(
                "Best Practices",
                "warning",
                node.lineno,
                "Public function is missing a docstring.",
                symbol=name,
            )

        # --- Best Practices: too many arguments ---
        n_args = len(node.args.args)
        if n_args > self._cfg.MAX_FUNCTION_ARGS:
            self._add(
                "Best Practices",
                "warning",
                node.lineno,
                f"Function has {n_args} arguments "
                f"(threshold: {self._cfg.MAX_FUNCTION_ARGS}). "
                "Consider using a config object or dataclass.",
                symbol=name,
            )

        # --- Style: naming convention (should be snake_case) ---
        if not _is_snake_case(name) and not name.startswith("__"):
            self._add(
                "Style",
                "info",
                node.lineno,
                f"Function name '{name}' does not follow snake_case convention.",
                symbol=name,
            )

    def _check_loop(self, node: ast.AST, loop_type: str) -> None:
        if self._loop_depth > 0:
            # We're already inside a loop — this is a nested loop.
            self._add(
                "Complexity",
                "warning",
                node.lineno,  # type: ignore[attr-defined]
                f"Nested {loop_type}-loop detected. "
                "This may indicate O(n²) or worse time complexity.",
            )

        if loop_type == "while":
            self._add(
                "Best Practices",
                "info",
                node.lineno,  # type: ignore[attr-defined]
                "while-loop found. Ensure the termination condition is "
                "guaranteed to prevent infinite loops.",
            )

        # Recurse with incremented depth.
        self._loop_depth += 1
        self.generic_visit(node)
        self._loop_depth -= 1


# ---------------------------------------------------------------------------
# Module-level checks (run on the whole tree, not per-node)
# ---------------------------------------------------------------------------

def _check_module_docstring(tree: ast.Module) -> Optional[Finding]:
    """Return a finding if the module lacks a module-level docstring."""
    body = tree.body
    if body and isinstance(body[0], ast.Expr):
        val = body[0].value
        if isinstance(val, ast.Constant) and isinstance(val.value, str):
            return None  # has docstring
    return Finding(
        category="Best Practices",
        severity="info",
        line=None,
        message="Module is missing a module-level docstring.",
    )


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _is_snake_case(name: str) -> bool:
    """
    Return True when *name* looks like valid Python snake_case.

    Dunder methods like __init__ are excluded by the caller.
    """
    return name == name.lower() and not name[0].isdigit()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

class FileAnalyzer:
    """
    High-level interface: parse a file and return an :class:`AnalysisResult`.

    Example::

        result = FileAnalyzer("mymodule.py").analyze()
        for finding in result.findings:
            print(finding)
    """

    def __init__(self, filepath: str, config: Optional[ReviewConfig] = None):
        self.filepath = filepath
        self.config = config or ReviewConfig()

    def analyze(self) -> AnalysisResult:
        """
        Read, parse, and analyse the target file.

        Raises:
            FileNotFoundError: if the file path does not exist.
            SyntaxError: if the file contains invalid Python syntax.
            OSError: for other I/O related errors.
        """
        source = self._read_source()
        tree = self._parse(source)
        source_lines = source.splitlines()

        result = AnalysisResult(
            filepath=self.filepath,
            total_lines=len(source_lines),
        )

        # Module-level docstring check
        mod_finding = _check_module_docstring(tree)
        if mod_finding:
            result.findings.append(mod_finding)

        # Walk AST
        visitor = CodeAnalyzerVisitor(source_lines, self.config)
        visitor.visit(tree)

        result.findings.extend(visitor.findings)
        result.total_functions = visitor.func_count
        result.total_classes = visitor.class_count

        return result

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _read_source(self) -> str:
        """Read the file and return its content as a string."""
        with open(self.filepath, "r", encoding="utf-8") as fh:
            return fh.read()

    def _parse(self, source: str) -> ast.Module:
        """Parse source into an AST, raising SyntaxError on failure."""
        return ast.parse(source, filename=self.filepath)
