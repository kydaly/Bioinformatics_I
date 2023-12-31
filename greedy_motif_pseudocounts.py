from profile_pseudocounts import ProfileWithPseudocounts
from most_probable_kmer import ProfileMostProbableKmer
from score import Score
def GreedyMotifSearchPseudo(Dna: list, k: int, t: int) -> list:
  """Greedy Motif Seach with pseudocounts incorporated."""
  BestMotifs = []
  n = len(Dna[0])
  for i in range(t):
    BestMotifs.append(Dna[i][0:k])
  for i in range(n-k+1):
     Motif = []
     Motif.append(Dna[0][i:i+k])
     for j in range(1, t):
      P = ProfileWithPseudocounts(Motif)
      Motif.append(ProfileMostProbableKmer(Dna[j], k, P))
     if Score(Motif) < Score(BestMotifs):
       BestMotifs = Motif
  return BestMotifs
