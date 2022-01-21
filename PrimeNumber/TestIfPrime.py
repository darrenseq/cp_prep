# write a program to test to output all the prime numbers 1-100

def isprime(num):
    # 1,2,3 skip the loop
    # 4 enteres loop 
    # num**0.5 is power of 0.5 i.e. sqare root of number
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return 'Not Prime'
    return 'Prime'
i = 10
for n in range(1, i+1):
    print(f'{n} is {isprime(n)}')