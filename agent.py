import argparse
import importlib
import subprocess
import sys
from pathlib import Path


def run_tests(bank: str) -> bool:
    """Run pytest for the given bank parser."""
    print(f"✅ Running tests for {bank} parser...")
    result = subprocess.run(
        ["pytest", "-q", f"tests/test_{bank}.py"], capture_output=True, text=True
    )
    print(result.stdout)
    print(result.stderr)
    return result.returncode == 0


def generate_parser(bank: str) -> None:
    """Generate a new parser file for the given bank."""
    parser_path = Path(f"custom_parsers/{bank}_parser.py")

    if parser_path.exists():
        print(f"⚠️ Parser {parser_path} already exists. Overwriting...")

    template_code = f'''"""
Auto-generated parser for {bank.upper()} bank statements.
"""

import pandas as pd
import pdfplumber


def parse(pdf_path: str) -> pd.DataFrame:
    \"\"\"Parse the {bank.upper()} bank statement PDF into a DataFrame.\"\"\"
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
