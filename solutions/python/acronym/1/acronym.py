"""
Abbreviate
"""

import re
from string import punctuation
def abbreviate(words):
    """
    I need to abbreviate
    """
    filteredStr = re.findall('[A-Z]+[a-z]*|[a-z]+', words)
    return "".join([word.strip(punctuation)[0].upper() for word in re.split(r'[\s|-]', words) if word != ''])