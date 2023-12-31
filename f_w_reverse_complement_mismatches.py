from neighbors import Neighbors
from max_map import MaxMap
from reverse_complement import reverse_complement
def FrequentWordsWithMismatches_ReverseComplements(Text: str, k: int, d: int) -> list:
  """Returns the k-mers that are most frequent in Text with up to d mismatches and include reverse complements"""
  Patterns = []
  freqMap = {}
  combined = {}
  n = len(Text)
  for i in range(n-k+1):
    Pattern = Text[i:i+k]
    Neighborhood = Neighbors(Pattern, d)
    for j in range(len(Neighborhood)):
      neighbor = Neighborhood[j]
      if neighbor not in freqMap:
        freqMap[neighbor] = 1
      else:
        freqMap[neighbor] += 1
  for key in freqMap:
    if reverse_complement(key) in freqMap: 
      combined[key] = freqMap[key] + freqMap[reverse_complement(key)]
  m = MaxMap(combined)
  for key in combined:
    if combined[key] == m:
      Patterns.append(key)
  return Patterns
