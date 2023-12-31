from hamming_distance import HammingDistance
def Neighbors(Pattern: str, d: int) -> list:
  """Outputs a list of k-mers that do not exceed a hamming distance of d."""
  nucleotides = ['A', 'T', 'G', 'C']
  if d == 0:
    return Pattern
  if len(Pattern) == 1:
    return nucleotides
  neighborhood = []
  suffixPattern = Pattern[1:]
  suffixneighbors =  Neighbors(suffixPattern, d)
  for text in suffixneighbors:
    if HammingDistance(suffixPattern, text) < d:
      for x in nucleotides:
        neighborhood.append(x + text)
    else:
      neighborhood.append(Pattern[0] + text)
  return neighborhood