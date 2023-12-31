from neighbors import Neighbors
def MotifEnumeration(Dna: list, k: int, d: int) -> list: 
  """Outputs motifs with length k, and a hamming distance d in a list Dna."""
  kmer = [] 

  # index and gene string in list Dna
  for l, genome in enumerate(Dna): 
    kmer.append(set(Neighbors(genome[0:0+k], d)))
    for i in range(1, len(genome)-k+1): 
      kmer[l].update(set(Neighbors(genome[i:i+k], d))) 
      Patterns = kmer[l]
    else:
      Patterns = Patterns & kmer[l]  
  return Patterns
