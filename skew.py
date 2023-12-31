def skew(genome: str) -> list:
  """Indexes the difference of G and C in each position in genome"""
  char_list = ['A', 'T', 'C', 'G']
  GC_vals = 0
  indx_vals = [0]
  for char in genome:
    if char == char_list[2]:
      GC_vals -= 1
    elif char == char_list[3]:
      GC_vals += 1
    else:
      pass
    indx_vals.append(GC_vals)
  return indx_vals