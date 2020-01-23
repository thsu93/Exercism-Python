def count_words(sentence):
    lowered = sentence.lower()
    phrase = lowered.split()
    words = {word: phrase.count(word) for word in sorted(set(phrase), key=phrase.index)}
    return words
