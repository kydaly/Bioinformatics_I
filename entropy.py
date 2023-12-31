import math
from motif_profile import Profile
def Entropy(Motifs: list) -> int:
  """Calculates the total combined entropy of Motifs.
  The formula for entropy: Summation (probability * log base 2(probability)"""
  n = len(Motifs)
  profile = Profile(Motifs)
  entropy = 0
  for nuc in profile:
    nuc_list = profile[nuc]
    for j in range(len(nuc_list)):
      value = nuc_list[j]
      if value == 0:
        entropy += 0
      else:
        entropy += -(value*math.log(value, 2))
  return entropy