from hamming_distance import HammingDistance
def ApproximateCount(Text: str, Pattern: str, k: str) -> int:
  """Instead of returning the positions, the number of instances is returned"""
  d = len(Pattern)
  
  # initializing list of positions
  count = 0 
  
  #initialize a looking window of len(Pattern)
  for i in range(len(Text) - d + 1): 

    #check the Hamming Distance of each window 
    if HammingDistance(Text[i:i+d], Pattern) <= k:  
      count += 1
  return count
