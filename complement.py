def complement(seq):
  """Takes in a Dna string seq and returns the complementary seq"""
  complement_seq = ""
  for letter in seq:
    if letter == 'A' or 'T' or 'C' or 'G':
      if letter == 'A':
        opposite = 'T'
        complement_seq += opposite
      elif letter == 'T':
        opposite = 'A'
        complement_seq += opposite
      elif letter == 'G':
        opposite = 'C'
        complement_seq += opposite
      elif letter == 'C':
        opposite = 'G'
        complement_seq += opposite
    else:
      print("Sequence entered was incorrect")
  return complement_seq