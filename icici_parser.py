"""
Hand-written parser for ICICI bank statements.
"""

import pandas as pd
import pdfplumber


def parse(pdf_path: str) -> pd.DataFrame:
    """Parse ICICI bank statement PDF into a DataFrame."""
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text().split("\n")
            # Skip header row
            for line in text[1:]:
                cols = line.split()
                rows.append(cols)

    # Adjust schema to match icici_sample.csv
    df = pd.DataFrame(rows, columns=["Date", "Txn Details", "Debit", "Credit", "Balance"])
    return df
