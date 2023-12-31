def CountWithPseudocounts(Motifs:list) -> dict:
    """Implements pseudocounts by initializing all matrix positions at 1."""
    count = {} 
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
              count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
