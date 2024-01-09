from random import randint
def RandomMotif(Dna: list, k: int, t: int):
  """Generates random kmers with length, k from a list, Dna"""
  motifs = []
  j = len(Dna[0])
  for i in range(t):
    r = randint(0, j-k)
    motifs.append(Dna[i][r:r+k])
  return motifs