def is_pangram(sentence):
    return all(item in sentence.lower() for item in "abcdefghijklmnopqrstuvwxyz")