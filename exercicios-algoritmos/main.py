
## Exercicio 1 - Função Soma
# def sum(list):
#   if not list:
#     return 0
#   return list[0] + sum(list[1:])

# nums = [2, 4, 6]
# print(sum(nums))
# print(nums[1:])

## Exercicio 2 - contagem de elementos em uma lista
# def countList(list):
#   if not list:
#     return 0
#   return 1 + countList(list[1:])

# nums = [2, 4, 5, 6, 7, 10]

# print(countList(nums))


## Exercicio 3 - encontre o valor mais alto da lista
# def highValue(list):
#   if len(list) == 1:
#     return list[0]
#   high_rest = highValue(list[1:])
#   return list[0] if list[0] > high_rest else high_rest
  
# nums = [2, 4, 6, 8, 10, 12, 9]
# print(highValue(nums))


## Quicksort
def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivo = array[0]
  menores = [i for i in array[1:] if i <= pivo]
  maiores = [i for i in array[1:] if i > pivo]
  return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))

