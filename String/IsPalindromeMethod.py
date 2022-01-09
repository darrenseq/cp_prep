# Write a function to determine if a string was a palindrome. 
# After completion, also asked how it would need to be changed to ignore spaces, 
# and also how to write a separate function to determine the longest palindrome contained in a string.

import string

input = 'abccba'
input = input.replace(' ','')

def isPalindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

if isPalindrome(input):
    print(f'{input} is a Palindrome')
else:
    print(f'{input} is not a Palindrome')

def longestPalSubstr(input):
     
    length = len(input)
    maxLength = 1   # All subStrings of length 1 are palindromes
    start = 0

    # Nested loop to mark start and end index
    for i in range(length):
        for j in range(i, length):
            flag = 1
            print(f'i = {i}\nj = {j}\n')
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                # print(f'((j - i) // 2) + 1 => {((j - i) // 2) + 1}')
                # print(f'i => {i}')
                # print(f'k => {k}')
                # print(f'j => {j}')
                # print(f'input[i + k] => {input[i + k]}')
                # print(f'input[j - k] => {input[j - k]}')
                if (input[i + k] != input[j - k]):
                    # print('Set flag 0')
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
                 
    print("Longest palindrome subString is: ", end = "")
    print(f'=====>{input}  {start}  {start + maxLength - 1}')
 
    # Return length of LPS
    return maxLength

print(longestPalSubstr(input))