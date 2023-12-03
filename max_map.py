def MaxMap(pattern_dict):
  """Takes in a dictionary of strings and outputs the max frequency"""
  max_value = max(pattern_dict.values())
  return max_value

pattern = {'ATG': 2, 'CTG': 1, 'AGG': 4}
MaxMap(pattern)