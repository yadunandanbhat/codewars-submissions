# We need to square each and every element by looping through the each element of the string
# And join that square value to a string so that we can return it
def square_digits(num):
    result = ""
    for n in str(num):
        result = result + str(int(n)**2)
    return int(result)

#One line version
def square_digits(num):
    return int(''.join(str(int(n)**2) for n in str(num)))