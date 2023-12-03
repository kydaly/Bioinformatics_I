def reverse(seq):
  """Returns the reverse of the input string seq"""
  reverse_seq = ""
  for char in seq:
    reverse_seq = char + reverse_seq
  return reverse_seq
