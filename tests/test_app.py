"""Tests for the greeting function and command-line entry point."""
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from app import greet, main


class TestApp(unittest.TestCase):
    def test_greet_world(self):
        self.assertEqual(greet("World"),
                         "Hello, World from Mohammad Kourani!")

    def test_greet_name(self):
        self.assertEqual(greet("Nour"), "Hello, Nour from Mohammad Kourani!")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello,  from Mohammad Kourani!")

    def test_main(self):
        output = StringIO()
        with redirect_stdout(output):
            main()
        self.assertEqual(output.getvalue(),
                         "Hello, World from Mohammad Kourani!\n")

    def test_command_line(self):
        app = Path(__file__).resolve().parents[1] / "app.py"
        result = subprocess.run([sys.executable, str(app)], check=True,
                                capture_output=True, text=True)
        self.assertEqual(result.stdout,
                         "Hello, World from Mohammad Kourani!\n")


if __name__ == "__main__":
    unittest.main()
