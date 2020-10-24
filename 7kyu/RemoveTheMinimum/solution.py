# We are supposed to find out the minimum elemetn in the list and remove that
# To do that, we create another list and if that list is empty, it simply returns the list
# If it isn't empty then it return the list with it's minimum element removed
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

# One-line solution
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []