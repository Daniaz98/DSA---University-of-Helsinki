numbers = [1, 3, 5, 7, 9, 12]

numbers.insert(1, 98)
numbers.append(30)
numbers.pop(1)
x = numbers[2]

print(numbers)


# a = [2, 3, 5, 7, 9]
# b = a
# a.append(11)

# print(a)
# print(b)

a = [2, 3, 5, 7, 9]
b = a.copy()
a.append(11)

print(a) # [2, 3, 5, 7, 9, 11]
print(b) # [2, 3, 5, 7, 9]

#Indexing ([])    	             O(1)
#Size(len)                       O(1)
#Is element on list?(in)         O(n)
#Searching(index)                O(n)
#Counting(count)                 O(n)
#Adding to end (append)          O(1)
#Adding to middle (insert)       O(n)
#Removing from end (pop)         O(1)
#Removing from middle (pop)      O(n)
#Searching and removing (remove) O(n)


## Functions
def double(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers)) # [2, 4, 6, 8]
print(numbers) # [1, 2, 3, 4]


## Slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6]) # [3, 4, 5, 6]