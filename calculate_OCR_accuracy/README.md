# OCR Accuracy Calculator

This script calculates the accuracy of OCR (Optical Character Recognition) output by comparing it with the actual text using the Levenshtein distance. The Levenshtein distance is a metric for measuring the difference between two sequences. The script computes the accuracy as a percentage, indicating how closely the OCR text matches the actual text.

## Features

- **Levenshtein Distance Calculation**: Measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another.
- **Accuracy Calculation**: Provides the accuracy percentage of the OCR output by comparing it with the actual text.

## Requirements

- Python 3.x
- [Levenshtein](https://pypi.org/project/python-Levenshtein/) library

## Installation

To install the necessary package, you can use `pip`:

```bash
pip install python-Levenshtein
