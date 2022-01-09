# Write a method to check if a string is a palindrome

input = 'amaama'
mid = int(len(input) / 2)

# split input into half
if len(input) % 2 == 0:
    start_half = input[:mid]
    last_half = input[mid:]
else:
    start_half = input[:mid]
    last_half = input[mid + 1:]

# check if palindrome
if start_half == last_half[::-1]:
    result = True
else: 
    result = False 

# Print answer
if result:
    print(f'{input} is a Palindrome')
else: 
    print(f'{input} is not a Palindrome')