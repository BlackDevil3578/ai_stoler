import Levenshtein


def calculate_ocr_accuracy(actual_text, ocr_text):

    # Calculate the Levenshtein distance
    levenshtein_distance = Levenshtein.distance(actual_text, ocr_text)

    # Calculate the maximum possible distance (length of the longest text)
    max_length = max(len(actual_text), len(ocr_text))

    if max_length == 0:
        return 100.0  # Both strings are empty, so accuracy is 100%

    # Calculate the accuracy
    accuracy_percentage = (1 - levenshtein_distance / max_length) * 100

    return accuracy_percentage


actual_text="""
actual text
"""


ocr_text="""
ocr text
"""
print(calculate_ocr_accuracy(actual_text,ocr_text))