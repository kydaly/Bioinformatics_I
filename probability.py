def pr(gene: str, Profile: dict) -> float:
  """Computes the probability of a string, gene given a profile probability matrix, Profile."""
  probability = 1
  for i, char in enumerate(gene):
    probability *= Profile[char][i]
    print(probability)
  return probability