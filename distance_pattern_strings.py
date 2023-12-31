from hamming_distance import HammingDistance
def DistanceBetweenPatternAndStrings(Pattern: str, dna: list) -> int:
  """Returns the hamming distances between the string Pattern and all strings in dna."""
  total_distance = 0
  k = len(Pattern)
  for motif in dna:
    n = len(motif)
    for i in range(n-k+1):
      new_pattern = motif[i:i+k]
      if i == 0:
        min_distance = HammingDistance(Pattern,new_pattern)  
      else:
        distance = HammingDistance(Pattern, new_pattern)
        if distance < min_distance:
          min_distance = distance
    total_distance += min_distance
  return total_distance