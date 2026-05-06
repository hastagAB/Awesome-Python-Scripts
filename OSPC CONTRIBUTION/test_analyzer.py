"""
tests/test_analyzer.py - Unit tests for Smart Code Reviewer.

Run with:
    python -m unittest discover -s tests
    # or directly:
    python tests/test_analyzer.py
"""

import os
import sys
import textwrap
import unittest

# Ensure the package root is importable regardless of where tests are run.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analyzer import FileAnalyzer, ReviewConfig


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _analyze_source(source: str, **config_kwargs) -> list:
    """
    Parse *source* from a string and return the list of findings.

    Writes a temporary file because :class:`FileAnalyzer` works on paths.
    Uses a fixed temporary file name that is cleaned up after each test.
    """
    import tempfile

    config = ReviewConfig()
    for key, value in config_kwargs.items():
        setattr(config, key.upper(), value)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(textwrap.dedent(source))
        tmp_path = tmp.name

    try:
        result = FileAnalyzer(tmp_path, config=config).analyze()
        return result.findings
    finally:
        os.unlink(tmp_path)


def _categories(findings) -> list:
    return [f.category for f in findings]


def _messages(findings) -> list:
    return [f.message for f in findings]


def _severities(findings) -> list:
    return [f.severity for f in findings]


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestMissingDocstrings(unittest.TestCase):
    """Missing docstring checks (Best Practices)."""

    def test_function_without_docstring_flagged(self):
        source = """\
            def add(a, b):
                return a + b
        """
        findings = _analyze_source(source)
        self.assertTrue(
            any("docstring" in m.lower() for m in _messages(findings)),
            "Expected a missing-docstring finding.",
        )

    def test_function_with_docstring_not_flagged(self):
        source = """\
            def add(a, b):
                \"\"\"Return the sum of a and b.\"\"\"
                return a + b
        """
        findings = _analyze_source(source)
        # Only check function-level docstring findings (exclude file-level)
        bp_msgs = [
            f.message for f in findings
            if f.category == "Best Practices"
            and "docstring" in f.message.lower()
            and f.line is not None          # file-level findings have line=None
        ]
        self.assertEqual(bp_msgs, [], "Clean function should not be flagged.")

    def test_private_function_docstring_not_required(self):
        source = """\
            def _helper(x):
                return x * 2
        """
        findings = _analyze_source(source)
        bp_msgs = [
            f.message for f in findings
            if "docstring" in f.message.lower()
            and f.line is not None          # exclude file-level module finding
        ]
        self.assertEqual(bp_msgs, [], "Private functions should not require a docstring.")

    def test_class_without_docstring_flagged(self):
        source = """\
            class MyClass:
                pass
        """
        findings = _analyze_source(source)
        self.assertTrue(
            any("docstring" in m.lower() for m in _messages(findings))
        )


class TestLongFunctions(unittest.TestCase):
    """Long function detection (Style)."""

    def test_long_function_flagged(self):
        # 10 real lines + 1 def + 1 docstring = 12 lines, but we force threshold low.
        body = "\n".join(f"    x_{i} = {i}" for i in range(10))
        source = f'def long_func():\n    """Docstring."""\n{body}\n'
        findings = _analyze_source(source, max_function_lines=5)
        style_msgs = [f for f in findings if f.category == "Style"]
        self.assertTrue(
            any("lines long" in m.message for m in style_msgs),
            "Expected a 'lines long' style finding.",
        )

    def test_short_function_not_flagged(self):
        source = """\
            def short():
                \"\"\"Docstring.\"\"\"
                return 1
        """
        findings = _analyze_source(source, max_function_lines=50)
        style_msgs = [f for f in findings if f.category == "Style" and "lines long" in f.message]
        self.assertEqual(style_msgs, [])


class TestTooManyArguments(unittest.TestCase):
    """Excessive argument count detection (Best Practices)."""

    def test_too_many_args_flagged(self):
        source = """\
            def func(a, b, c, d, e, f):
                \"\"\"Six args.\"\"\"
                pass
        """
        findings = _analyze_source(source, max_function_args=5)
        self.assertTrue(
            any("arguments" in m.lower() for m in _messages(findings))
        )

    def test_acceptable_arg_count_not_flagged(self):
        source = """\
            def func(a, b, c):
                \"\"\"Three args — fine.\"\"\"
                pass
        """
        findings = _analyze_source(source, max_function_args=5)
        self.assertFalse(
            any("arguments" in m.lower() for m in _messages(findings))
        )


class TestNestedLoops(unittest.TestCase):
    """Nested loop / complexity detection."""

    def test_nested_for_loops_flagged(self):
        source = """\
            def process(data):
                \"\"\"Nested loops.\"\"\"
                for i in data:
                    for j in data:
                        pass
        """
        findings = _analyze_source(source)
        complexity_msgs = [f for f in findings if f.category == "Complexity"]
        self.assertTrue(
            any("nested" in m.message.lower() for m in complexity_msgs),
            "Expected a nested-loop finding.",
        )

    def test_single_loop_not_flagged(self):
        source = """\
            def process(data):
                \"\"\"Single loop.\"\"\"
                for i in data:
                    pass
        """
        findings = _analyze_source(source)
        complexity_msgs = [f for f in findings if f.category == "Complexity"]
        self.assertEqual(complexity_msgs, [])

    def test_nested_while_loop_flagged(self):
        source = """\
            def process(n):
                \"\"\"Nested while.\"\"\"
                i = 0
                while i < n:
                    j = 0
                    while j < n:
                        j += 1
                    i += 1
        """
        findings = _analyze_source(source)
        complexity_msgs = [f for f in findings if f.category == "Complexity"]
        self.assertTrue(len(complexity_msgs) >= 1)


class TestWhileLoopWarning(unittest.TestCase):
    """While loop termination warnings."""

    def test_while_loop_info_emitted(self):
        source = """\
            def run():
                \"\"\"Has a while loop.\"\"\"
                i = 0
                while i < 10:
                    i += 1
        """
        findings = _analyze_source(source)
        bp_msgs = [f for f in findings if f.category == "Best Practices"]
        self.assertTrue(
            any("while" in m.message.lower() for m in bp_msgs)
        )


class TestNamingConvention(unittest.TestCase):
    """snake_case convention checks (Style)."""

    def test_camel_case_function_flagged(self):
        source = """\
            def myFunction():
                \"\"\"Not snake_case.\"\"\"
                pass
        """
        findings = _analyze_source(source)
        style_msgs = [f for f in findings if f.category == "Style"]
        self.assertTrue(
            any("snake_case" in m.message for m in style_msgs)
        )

    def test_snake_case_function_not_flagged(self):
        source = """\
            def my_function():
                \"\"\"Proper snake_case.\"\"\"
                pass
        """
        findings = _analyze_source(source)
        style_msgs = [
            f for f in findings
            if f.category == "Style" and "snake_case" in f.message
        ]
        self.assertEqual(style_msgs, [])


class TestErrorHandling(unittest.TestCase):
    """Error handling — FileAnalyzer should raise standard exceptions."""

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileAnalyzer("/nonexistent/path/to/file.py").analyze()

    def test_syntax_error(self):
        import tempfile

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write("def broken(\n")
            tmp_path = tmp.name

        try:
            with self.assertRaises(SyntaxError):
                FileAnalyzer(tmp_path).analyze()
        finally:
            os.unlink(tmp_path)


class TestModuleDocstring(unittest.TestCase):
    """Module-level docstring check."""

    def test_module_without_docstring_flagged(self):
        source = """\
            x = 1
        """
        findings = _analyze_source(source)
        file_level = [f for f in findings if f.line is None]
        self.assertTrue(len(file_level) >= 1)

    def test_module_with_docstring_not_flagged(self):
        source = """\
            \"\"\"My module docstring.\"\"\"
            x = 1
        """
        findings = _analyze_source(source)
        file_level = [f for f in findings if f.line is None]
        self.assertEqual(file_level, [])


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)
