def response(hey_bob):
    
    hey_bob = hey_bob.strip()
    question = False
    caps = False
    
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    
    if hey_bob.endswith("?"):
        question = True
    if hey_bob.isupper() and hey_bob.upper() != hey_bob.lower():
        caps = True
    
    if caps and question:
        return "Calm down, I know what I'm doing!"
    
    if question:
        return "Sure."
    
    if caps:
        return "Whoa, chill out!"
    
    return "Whatever."
