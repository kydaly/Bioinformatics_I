from motif_profile import Profile
from score import Score
from most_probable_kmer import ProfileMostProbableKmer
def GreedyMotifSearch(Dna, k, t):
  """Using a greedy algorithm search for the highest probability k-mer
  from each string in Dna."""
  BestMotifs = []
  n = len(Dna[0])
  for i in range(t):
    BestMotifs.append(Dna[i][0:k])
  for i in range(n-k+1):
     Motif = []
     Motif.append(Dna[0][i:i+k])
     for j in range(1, t):
      P = Profile(Motif)
      Motif.append(ProfileMostProbableKmer(Dna[j], k, P))
     if Score(Motif) < Score(BestMotifs):
       BestMotifs = Motif
  return BestMotifs