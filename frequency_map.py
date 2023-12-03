def FrequencyMap(Text, k):
    """Takes in a string Text and kmer length k and outputs a dictionary,
    freq, with the frequency of every kmer in Text"""
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
             freq[Pattern] = 1    
    return freq