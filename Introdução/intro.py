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