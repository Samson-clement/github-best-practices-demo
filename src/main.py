# src/main.py

import pandas as pd

import pandas as pd
import math

def calculate_summary(data):
    """
    Calculate summary statistics (mean, median, std) for a numeric dataset.
    
    Args:
        data (list): List of numeric values.
    
    Returns:
        dict: Summary statistics including mean, median, and std.
    """
    if not data:
        return {"mean": None, "median": None, "std": None}

    df = pd.DataFrame(data, columns=["value"])
    std_value = df["value"].std()
    summary = {
        "mean": df["value"].mean(),
        "median": df["value"].median(),
        "std": std_value if not math.isnan(std_value) else float("nan")
    }
    return summary


if __name__ == "__main__":
    # Example dataset
    sample_data = [10, 20, 30, 40, 50]
    summary = calculate_summary(sample_data)
    print("Summary Statistics:", summary)
