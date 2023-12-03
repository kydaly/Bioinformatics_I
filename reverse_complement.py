from complement import complement
from reverse import reverse
def reverse_complement(seq):
  complement_seq = complement(seq)
  print(complement_seq)
  reverse_seq = reverse(complement_seq)
  return reverse_seq
