def PatternMatching(Pattern, Genome):
    """Returns the positions where Pattern appears in Genome"""
    positions = []
    k = len(Pattern)
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    return positions