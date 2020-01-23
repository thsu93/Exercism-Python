def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("mismatched lengths")
    for i in range(0,len(strand_b)):
        if strand_b[i] != strand_a[i]:
            count+=1
    return count

"""
Use sum (x!=y for i, j in zip(strand_a,strand_b)) to simplify
"""