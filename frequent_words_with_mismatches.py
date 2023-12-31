from neighbors import Neighbors
from max_map import MaxMap
def FrequentWordsWithMismatches(Text: str, k: int, d: int) ->list:
  """Outputs k-mers with the highest frequency in string, Text
  with hamming distance of at most d.""" 
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
  m = MaxMap(freqMap)
  for key in freqMap:
    if freqMap[key] == m:
      Patterns.append(key)
  return Patterns
