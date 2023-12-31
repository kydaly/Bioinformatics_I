from motif_consensus import Consensus
def Score(Motifs: list) -> int:
    count = 0
    consensus = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])

    # initialize loop to go through each row(list) of Motifs
    for i in range(t):

      # initialize loop to go through each index of each list
       for j in range(k):
        
        # use an if statement to check if character is the same character of the same index of consensus
        if Motifs[i][j] != consensus[j]:
          count += 1
    return count