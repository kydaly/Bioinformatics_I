from frequency_map import FrequencyMap
from max_map import MaxMap
def FrequentWords(Text: str, k: int) -> list:
    words =[]
    freq = FrequencyMap(Text, k)
    m = MaxMap(freq)
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words
