from hamming_distance import HammingDistance
def Motifs(Pattern: list, dna: str) -> list:
  """Creates a list of motifs that most closely matches a string, dna from a list, Pattern."""
  motifs = []
  k = len(Pattern)
  for motif in dna:
    n = len(motif)
    for i in range(n-k+1):
      new_pattern = motif[i:i+k]
      if i == 0:
        min_distance = HammingDistance(Pattern,new_pattern)
        min_pattern = new_pattern  
      else:
        distance = HammingDistance(Pattern, new_pattern)
        if distance < min_distance:
          min_distance = distance
          min_pattern = new_pattern
    motifs.append(min_pattern)
  return motifs