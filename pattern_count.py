def PatternCount(Text: str, Pattern: str) -> int:
  """Counts the number of occurences of Pattern in Text"""
  count = 0
  for i in  range(len(Text) - len(Pattern) +1):
    if Text[i:i+len(Pattern)] == Pattern:
      count += 1
  return count

Text = 'ACTGTACGATGATGTGTGTCAAAG'

Pattern = 'TGT'
PatternCount(Text, Pattern)