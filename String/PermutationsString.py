# Permutations of string

def toString(List): 
    print(''.join(List))  
    
def permute(input, s, l): 
    if s == l: 
        toString(input) 
    else: 
        for i in range(s, l+1): 
            # print(f's => {s} input[s] => {input[s]}')
            # print(f'i => {i} input[i] => {input[i]}')
            input[s], input[i] = input[i], input[s] 
            # print(f'Before permute {i}')
            permute(input, s+1, l)
            # print(f'After permute {i}')
            input[s], input[i] = input[i], input[s] # backtrack 
            # print(f's => {s} input[s] => {input[s]}')
            # print(f'i => {i} input[i] => {input[i]}\n\n')

input = "abc"
length = len(input) 
input = list(input) 
start = 0
permute(input, start, length - 1) 