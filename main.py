# 1. create and print set that contain some fruits
# 2. add more elements to set with add() method
# 3. try to add a duplicate element in set, does it gets added?
# 4. from a given list my_list find all unique elements (hint: use set() function)
# 5. find the total number of elements of the set(hint: use len() function)
# 6. find elements that are different while comparing two sets(hint: use differenc() method)

# 1. create and print set that contain some fruits
my_fruit_set = {'banana', 'mango', 'orange', 'kiwi', 'apple'}
print(my_fruit_set)
print('--------------******--------------\n')

# 2. add more elements to set with add() method
my_fruit_set.add('watermelon')
print(my_fruit_set)
print('--------------******--------------\n')

# 3. try to add a duplicate element in set, does it gets added?  
#   - no, the Set has unique elements - has no duplicate elements
my_fruit_set.add('blueberry')
my_fruit_set.add('blueberry')
print(my_fruit_set)
print('--------------******--------------\n')

# 4. from a given list my_list find all unique elements (hint: use set() method)
my_list = [1,2,2,3,4,5,5,5]
print(my_list)
#use set() function and pass list as object; so, it return a set with unique values
my_set = set(my_list)
print(my_set)
print('--------------******--------------\n')

# 5. find the total number of elements of the set(hint: use len() function)
print('Total number of elements in this set are: ' + str(len(my_set)))
print('--------------******--------------\n')

# 6. find elements that are different while comparing two sets(hint: use differenc() method)
my_fruit_set = {'banana', 'mango', 'orange', 'kiwi', 'apple'}
your_fruit_set = {'melon', 'strawberry', 'banana', 'kiwi', 'grape', 'papaya', 'pear'}
print(my_fruit_set)
print(your_fruit_set)
print(my_fruit_set.difference(your_fruit_set))
print('--------------******--------------\n')
