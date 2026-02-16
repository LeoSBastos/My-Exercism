"""
Isogram
"""

def is_isogram(string):
    """
    Isogram test
    """
    filteredString = "".join(filter(lambda x: x.isalpha(), string)).lower()
    return len(filteredString) == len(set(filteredString))
