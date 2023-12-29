from skew import skew
from neighbors import Neighbors
from reverse_complement import reverse_complement
from max_map import MaxMap
def FrequentWordsWithMismatches_ReverseComplements(Text, k, d):
  Patterns = []
  freqMap = {}
  combined = {}
  estimate_loc = skew(Text)
  for loc in estimate_loc:
    start = loc
    n = start + 500
    for i in range(start, n-k+1):
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