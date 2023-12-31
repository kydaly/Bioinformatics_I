from complement import complement
from reverse import reverse
def reverse_complement(seq: str) -> str:
  """Outputs the reverse complement of seq."""
  complement_seq = complement(seq)
  reverse_seq = reverse(complement_seq)
  return reverse_seq
