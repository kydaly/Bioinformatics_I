from score import Score
from profile_pseudocounts import ProfileWithPseudocounts
from most_probable_motifs import most_probable_motifs
from random_motifs import RandomMotif


def RandomizedMotifSearch(Dna, k, t):
  motif = RandomMotif(Dna, k, t)
  bestmotifs = motif.copy()
  while True:
    profile = ProfileWithPseudocounts(motif)
    motif = most_probable_motifs(profile, Dna)
    if Score(motif) < Score(bestmotifs):
      bestmotifs = motif.copy()
    else:
      return bestmotifs

Dna = ['TTACCTTAAC',
       'GATGTCTGTC',
       'CCGGCGTTAG',
       'CACTAACGAG',
       'CGTCAGAGGT'
       ] 

# set t equal to the number of strings in Dna, k equal to 15, and N equal to 100.
t = len(Dna)
k = 4
N = 12

# Call RandomizedMotifSearch(Dna, k, t) N times, storing the best-scoring set of motifs
# resulting from this algorithm in a variable called BestMotifs
BestMotifs = RandomizedMotifSearch(Dna, k, t)
for i in range(N):
    m = RandomizedMotifSearch(Dna, k, t)
    print(Score(m))
    if Score(m) < Score(BestMotifs):
        BestMotifs = m
print(BestMotifs)
