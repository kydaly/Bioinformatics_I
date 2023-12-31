from neighbors import Neighbors
def MotifEnumeration(Dna: list, k: int, d: int) -> list: #Dna is a list of strings, k is length of each pattern, d is the amount of mismatches
  """Outputs motifs with length k, and a hamming distance d in a list Dna."""
  kmer = [] # holding a list of all the k patterns created
  for l, genome in enumerate(Dna): # index and gene string in list Dna
    kmer.append(set(Neighbors(genome[0:0+k], d)))
    for i in range(1, len(genome)-k+1): # going through 
      kmer[l].update(set(Neighbors(genome[i:i+k], d))) # each pattern in current string of Dna
    if l == 0:
      Patterns = kmer[l]
    else:
      Patterns = Patterns & kmer[l]  
  return Patterns
