# 1. create and print set that contain some fruits
# 2. add more elements to set with add() method
# 3. try to add a duplicate element in set, does it gets added?  

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