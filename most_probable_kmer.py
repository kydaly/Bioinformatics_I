from probability import pr
def ProfileMostProbableKmer(Text: str, k: int, Profile: dict) -> str:
  """Given a string , Text, k-mer length, k and a probability matrix, Profile,
  generate the highest probability k-mer."""
  n = len(Text)

  # for k go through each kmer in text
  for i in range(n-k+1):
    kmer = Text[i:i+k]
    if i == 0:
      best_probability = pr(kmer, Profile)
      best_kmer = kmer
    else: 
      probability = pr(kmer, Profile)
      if probability > best_probability:
        best_probability = probability
        best_kmer = kmer
  return best_kmer