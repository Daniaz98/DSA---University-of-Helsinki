# def count_even(numbers):
#   result = 0
#   for x in numbers:
#     if x % 2 == 0:
#       result += 1
#   return result

# print(count_even([1, 2, 4, 8, 3]))

def find_max(numbers):
  maxv = numbers[0]
  for y in numbers:
    if y > maxv:
      maxv = y
  return maxv

print(find_max([1, 3, 4, 5, 9, 8]))

#--------------------------------------------------------------------------

#Complexity time 

#Constant time - O(1)
##If an algorithm has no loops and it executes the same steps independent of the input, its time complexity is O(1)
def middle(numbers):
  n = len(numbers)
  return numbers[n // 2]

#Single loop - O(n)
##If the algorithm contains a single loop that goes through all elements of the input, its time complexity is O(n)

def calc_sum(numbers):
  result = 0
  for x in numbers:
    result += x
  return result

#Nested loops - O(n**2)
##If an algorithm contains a loop inside a loop, each of which goes through all elements of the input

def has_sum(numbers, x):
  for a in numbers:
    for b in numbers:
      if a + b == x:
        return True
  return False

#Sequential code segments 
##If the algorithm consists of multiple code segments in sequence, the whole time complexity is the maximum of the segment time complexities.

