from distance_pattern_strings import DistanceBetweenPatternAndStrings
def MedianString(Dna: list, k: int) -> str:
  """Outputs a k-mer that minimizes hamming distance of all possible k-mers."""
  min_distance = 100000000000
  # Patterns = Neighbors('A'*k, k)
  Patterns = []
  for string in Dna:
    for i in range(len(string)-k+1):
      Patterns.append(string[i:i+k])
  n = len(Patterns)
  for j in range(n):
    pattern = Patterns[j]
    distance = DistanceBetweenPatternAndStrings(pattern, Dna)
    if distance < min_distance:
      min_distance = distance
      median = pattern
  print(min_distance)   
  return median