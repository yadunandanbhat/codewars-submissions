# Here we need to find an integer's divisors
# Divisors can be found by checking if a number, when divided by the given integer, has a remainder or not
# If it doesn't have a remainder, then it's a divisor
# If a number is divisor, it is then sent to the 'divisor' list
# So if the 'divisor' list contains elements, then the integer is not a prime number and the 'divisor' list is returned
# If the 'divisor' list doesn't contain any element, then the given integer is a prime number

def divisors(integer):
    divisor = [ num for num in range(2, integer) if integer%num==0]
    return str(integer)+" is prime" if len(divisor)==0 else divisor