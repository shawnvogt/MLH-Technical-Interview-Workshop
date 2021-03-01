# MLH Hack the Technical Interview Workshop
# Solutions by Shawn Vogt

import math

"""
Write a function that takes a single
input, a number, and prints out 1
through the number. If the number
being printed is divisible by 3, print
"Fizz" instead of the number itself. If
the number being printed is divisible
by 5, print "Buzz." If the number being
printed is divisible by 3 AND 5, print
"FizzBuzz."
"""
def fizzbuzz(n):
  # Iterate through a range of number from 1 up to and including n
  for i in range(1,n+1):
    # If number is divisible by 3 and 5 it will be divisible by 3 * 5: print FizzBuzz
    if i % 15 == 0:
      print("FizzBuzz")
    # Else if number is divisible by 5: print Buzz
    elif i % 5 == 0:
      print("Buzz")
    # Else if number is divisible by 3: print Fizz
    elif i % 3 == 0:
      print("Fizz")
    # Else: print i
    else:
      print(i)

# Test FizzBuzz 
print("*"*50,"\ntesting fizzbuzz(32)")
fizzbuzz(32)
# does it work with negative? 
print("*"*50,"\ntesting fizzbuzz(-32)")
fizzbuzz(-32)
# it does not. If I wanted it to work with negative how could I modify the code to accomplish that?
# I will make the assumption that if n is negative we want to iterate from -1 to n. If we were to  
# iterate from 1 to n on a negative number we would have to handle 0 as 0 % anynumber = zero and will
# incorrectly print FizzBuzz.

def fizzbuzz2(n):
  # Iterate through a range of number from 1 up to and including n
  # step is introduced to allow reverse iteration and can also be used to change
  # the start and stop of the range
  step = 1 if n > 0 else -1
  for i in range(1, n + step, step):
    # 0 modululo 3 or 5 will return 0 so we need to test if i is 0
    if i == 0:
      print(i)
    # If number is divisible by 3 and 5 it will be divisible by 3 * 5: print FizzBuzz
    elif i % 15 == 0:
      print("FizzBuzz")
    # Else if number is divisible by 5: print Buzz
    elif i % 5 == 0:
      print("Buzz")
    # Else if number is divisible by 3: print Fizz
    elif i % 3 == 0:
      print("Fizz")
    # Else: print i
    else:
      print(i)

# does fizzbuzz still work with positive n
print("*"*50,"\ntesting fizzbuzz2(32)")
fizzbuzz2(32)
# does fizzbuzz now work with negative n
print("*"*50,"\ntesting fizzbuzz2(-32)")
fizzbuzz2(-32)
# what happens if I try fizzbuzz2(0)? 
# It should print 1 and 0
print("*"*50,"\ntesting fizzbuzz2(0)")
fizzbuzz2(0)

"""
Write a function that takes in
two string inputs, and returns
true if they are a rotation of
each other.
"""
# I had intended to use iteration to solve this problem but as I was 
# writing down a string on a piece of paper it occured to me that I 
# could instead double one of the strings and test if the other string
# is within the doubled string. The doubled string will catch all rotations.
def is_rotation(s1, s2):
  # if the length of s1 and s2 are different, we know the strings are not rotations of each other
  if len(s1) != len(s2):
    return False
  # if s1 is in s2 doubled we know that the strings are rotations of each other
  if s1 in (s2 * 2):
    return True
  else:
    return False

# The code could refactored down to a signle line
# return len(s1) == len(s2) and s1 in s2 * 2

# Test with strings that are rotations
print("*"*50,'\ntesting is_rotation("ABCD","DABC") should return True\n')
print(is_rotation("ABCD","DABC"))

# Test with strings where a rotation is contained but strings are different length
print("*"*50,'\ntesting is_rotation("ABCD","DABCD") should return False\n')
print(is_rotation("ABCD","DABCD"))

# Test with strings that are not rotations
print("*"*50,'\ntesting is_rotation("ABCD","DBAC") should return False\n')
print(is_rotation("ABCD","DBAC"))

"""
Write a function that takes an
array with distinct elements
and sorts them in a zig-zag
fashion. (ie
a < b > c < d > e < f)
"""
# My idea was to sort the list and break into two separate lists
# then merge the two lists togeth low[0] high[0] low[1] high[1] etc. 
# important to ensure that the first list is the shorter list on 
# odd length lists or the last merged number will be incorrect
def zigzag(nums):
    nums_sorted = sorted(nums)
    nums_low = nums_sorted[0:math.ceil(len(nums_sorted)/2)]
    nums_high = nums_sorted[math.ceil(len(nums_sorted)/2):]      
    nums_zigzag = []

    # Instead of iterating with a for loop I decided to use a while Loop
    # and pop the first value from each list into a new list until the first list is empty
    while len(nums_low) > 0:
        nums_zigzag.append(nums_low.pop(0))
        if len(nums_high) > 0: nums_zigzag.append(nums_high.pop(0))
        
    return nums_zigzag


# Test with even legth list
print("*"*50,'\ntesting zigzag([4, 3, 7, 8, 6, 2, 1, 1])\n')
print(zigzag([4, 3, 7, 8, 6, 2, 1, 1]))

# Test with odd legth list
print("*"*50,'\ntesting zigzag([4, 3, 7, 8, 6, 2, 1])\n')
print(zigzag([4, 3, 7, 8, 6, 2, 1]))

# Test with some more lists
print("*"*50,'\ntesting zigzag(list) with a bunch of lists\n')
print(zigzag([4, 3, 7, 8, 6, 2, 1, 1, 1, 2, 2, 2, 15, 16, 20, 20, 7]))
print(zigzag([1, 4, 3, 2, 1]))

# The above works but what if we want to accomplish the same task with a 
# better time complexity than nlogn?
# The below solution was shown to me, and is not my own. I have found that
# although it has a better time complexity it does not appear to work when 
# there are duplicate numbers in the list. My slower function handles these
# fine. 

def ziggyzag(arr, n):
  flag = True
  for i in range(n-1):
    if flag is True:
      if arr[i] > arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
    else:
      if arr[i] < arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
    flag = bool(1 - flag) # I would have used flag = not flag
  print(arr)

def ziggy(arr):
  ziggyzag(arr, len(arr))

# Test with even legth list
print("*"*50,'\ntesting ziggy([4, 3, 7, 8, 6, 2, 1, 1])')
ziggy([4, 3, 7, 8, 6, 2, 1, 1])

# Test with odd legth list
print("*"*50,'\ntestingy([4, 3, 7, 8, 6, 2, 1])')
ziggy([4, 3, 7, 8, 6, 2, 1])

# Test with some more lists
print("*"*50,'\ntesting ziggy(list) with a bunch of lists')
ziggy([4, 3, 7, 8, 6, 2, 1, 1, 1, 2, 2, 2, 15, 16, 20, 20, 7])
ziggy([1, 4, 3, 2, 1])


"""
Write a function that takes an
array of elements and returns
“Yes” if there is a pythagorean
triplet ((a, b, c) that satisfies a2
+ b2 = c2), “No” otherwise.
"""

# My solution takes the list argument and convertis it
# to a sorted list of numbers squared. Starting from the largest number
# check if the number that need to be added to the next smaller number
# exists in list until at the smallest number
def triplet(nums):
  a = [n**2 for n in sorted(nums)]
  for i in range(len(a)-1, 1, -1):
    for j in range(i-1,0,-1):
      lookingfor = a[i] - a[j]
      if lookingfor in a[0:j]:
        return "Yes"
  return "No"

print("*"*50,'\ntesting triplet function')
t = [10, 4, 6, 12, 5]
print(f'{t} contains pythagorean triplet = {triplet(t)}')
t = [3, 1, 4, 6, 5]
print(f'{t} contains pythagorean triplet = {triplet(t)}')


"""
Write a function that takes two
inputs, a pair of strings, and proves
if they are anagrams (contain all the
same letters) of each other.
"""
def anagram(s1,s2):
  return len(s1) == len(s2) and "".join(sorted(s1.lower())) == "".join(sorted(s2.lower()))

