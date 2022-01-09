# Find the first duplicate character in a string

def firstDuplicateChar(input): 
    if len(input) <= 0:
        return ''

    h = {} # Create empty hash 
    for char in input: 
        # If char is already present in hash, return it 
        if char in h: 
            return char; 
        # Add it to the hash 
        else: 
            h[char] = 0

print(firstDuplicateChar('')) 
