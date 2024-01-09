from most_probable_kmer import ProfileMostProbableKmer
def most_probable_motifs(Profile: dict, Dna: list) -> list:
    """Modifies motifs function to implement most_probable_kmer to 
    create the most probable motifs"""
    motifs = []
    k = len(Profile['A'])
    t = len(Dna)
    for i in range(t):
        motifs.append(ProfileMostProbableKmer(Dna[i], k, Profile))
    return motifs