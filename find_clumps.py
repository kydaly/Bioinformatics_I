from frequency_map import FrequencyMap
def FindClumps(Text, k, L, t):
  """Outputs clumps of patterns with a value of t or higher. Inputs are a string Text, kmer length k,
  window length L, and frequency t."""
  # initiate a dictionary Patterns 
  Patterns = {}
  n = len(Text)

  # loop from positions 0 to n - L 
  for i in range(n - L):
    Window = Text[i:i+L]

  # use the FrequencyMap function to build array of all patterns
    freqMap = FrequencyMap(Window, k)

  # loop on keys in FrequencyMap and if the value is greater or equal to t
    for key in freqMap:
      if freqMap[key] >= t:
        Patterns[key] = freqMap[key]
  return Patterns.keys()