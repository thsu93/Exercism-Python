def abbreviate(words):
    import re
    outputstring = ""
    return outputstring.join([i[0] for i in re.split(' |-|_|,', words.upper()) if i!=''])
