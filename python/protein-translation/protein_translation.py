def proteins(strand):
    rnaList = [strand[i:i+3] for i in range(0,len(strand),3)]
    proteinDict = {
        "AUG":	"Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA":"STOP",
    }
    proteinList = []
    for protein in rnaList:
        if (proteinDict[protein] == "STOP"):
            break
        proteinList.append(proteinDict[protein])
    return proteinList