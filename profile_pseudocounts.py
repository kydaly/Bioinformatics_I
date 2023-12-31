from motif_count import Count
def ProfileWithPseudocounts(Motifs: list) -> dict:
    """Computes a profile matrix using pseudocounts."""
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    for key in profile:
        for value in range(k):
            profile[key][value] = profile[key][value] / (t + 4)
    return profile