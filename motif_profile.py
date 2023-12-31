from motif_count import Count
def Profile(Motifs: list) -> dict:
    """Outputs a dictionary with the percentage of each nucleotide in each location given list Motifs"""
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    for key in profile:
        for value in range(k):
            profile[key][value] = profile[key][value] / t
    return profile