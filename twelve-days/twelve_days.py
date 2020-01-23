def recite(start_verse, end_verse):
    starter="On the %s day of Christmas my true love gave to me: "
    numericals=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    days = ["a Partridge in a Pear Tree.", "two Turtle Doves, and ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]
    output = []
    for i in range(start_verse, end_verse+1):
        tempstring = (starter % numericals[i-1])
        for j in reversed(range(0,i)):
            tempstring+=days[j]
        output.append(tempstring)
    return output
    
