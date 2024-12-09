import sys
import os
import pytest
import math

# Add src/ directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import calculate_summary

def test_calculate_summary_with_data():
    data = [10, 20, 30, 40, 50]
    expected = {
        "mean": 30.0,
        "median": 30.0,
        "std": 15.811388300841896
    }
    result = calculate_summary(data)
    assert result == pytest.approx(expected)

def test_calculate_summary_empty_data():
    data = []
    expected = {
        "mean": None,
        "median": None,
        "std": None
    }
    result = calculate_summary(data)
    assert result == expected


def test_calculate_summary_single_value():
    data = [25]
    expected = {
        "mean": 25.0,
        "median": 25.0,
        "std": float("nan")  # Use NaN for undefined standard deviation
    }
    result = calculate_summary(data)
    assert result["mean"] == expected["mean"]
    assert result["median"] == expected["median"]
    assert math.isnan(result["std"])  # Correctly check for NaN
