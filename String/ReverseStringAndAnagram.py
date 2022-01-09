# reverse string, 
# check two strings are anagrams

def reverse(input):
    return input[::-1]

print(reverse('hello world'))

def isAnagram(first, second):
    if len(first) != len(second):
        return False
    first, second = sorted(first), sorted(second)
    if first == second:
        return True
    else: 
        return False

first = 'raqce'
second = 'care'
if isAnagram(first, second):
    print(f'{first} and {second} are Anagrams')
else:
    print(f'{first} and {second} are NOT Anagrams')