def find_anagrams(word, candidates):
    wordList = list(word.lower())
    wordList.sort()
    anagrams = []
    for candidate in candidates:
        if len(candidate) != len(word) or candidate.lower() == word.lower():
            continue
        candidateList = list(candidate.lower())
        candidateList.sort()
        matches = True
        for w, c in zip(wordList, candidateList):
            if not w == c:
                matches = False
                continue
        if matches:
            anagrams.append(candidate)
    return anagrams
