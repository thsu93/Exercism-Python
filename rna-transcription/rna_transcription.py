def to_rna(dna_strand):
    matches = {"C":"G", "G":"C", "T":"A", "A":"U"}
    return "".join([matches[letter] for letter in dna_strand])