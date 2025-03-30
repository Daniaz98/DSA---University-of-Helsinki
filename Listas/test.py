def sum_array(numbers):
  result = 0
  
  for x in numbers:
    result += x
    if not numbers:
      return 0
  return result
  


print(sum_array([]))