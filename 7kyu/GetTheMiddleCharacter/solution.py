# We need to return the middle element of the string if the length of the string is odd
# If the length is even, then we need to return the middle two elements
# If the len is odd, we divide the len(s) by 2
# And if the len is even, then we divide the len(s) by 2 and find the elements between (len(s)/2)-1 and (len(s)/2)+1
# So to make a online solution for both cases, we can use the below code
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]