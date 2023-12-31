from hamming_distance import HammingDistance
def ApproximatePatternMatching(Text: str, Pattern: str, d: int) -> list:
  """Returns the positions that have a hamming distance less than or equal to d"""
  # initialize  list of positions
  positions = []

  # initialize a looking window of len(Pattern) 
  for i in range(len(Text) - len(Pattern) + 1):  
    if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d: 
      positions.append(i)
  return positions