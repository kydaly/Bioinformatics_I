def HammingDistance(p: str, q: str) -> int:
  """Outputs the number of differences between strings p and q"""
  count = 0
  for i in range(len(p)):
    if p[i] !=  q[i]:
      count += 1
  return count