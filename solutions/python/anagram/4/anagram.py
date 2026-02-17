"""
Anagrams
"""

def find_anagrams(word, candidates):
    """
    Anagrams function
    """
    wordList = list(word.lower())
    wordList.sort()
    anagrams = []
    for candidate in candidates:
        if len(candidate) != len(word) or candidate.lower() == word.lower():
            continue
        candidateList = list(candidate.lower())
        candidateList.sort()
        if wordList == candidateList:
            anagrams.append(candidate)
    return anagrams
