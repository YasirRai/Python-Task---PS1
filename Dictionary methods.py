dic = {"name": "Yasir", "age": 32, "city": "punjab"}
# Methods of Dictionary
print(' #1 ============= get() ============= ')        # to return values from Dictionary for the given key
print(dic.get("age"))                   # it will return 'age' value that is '32'

print(' #2 ============= values() ============= ')

print(dic.values())                     # return all values from dictionary, that is 'yasir' , '32' , 'punjab'

print(' #3 ============= keys() ============= ')
print(dic.keys())                       # return keys that containing values/data, like 'name', 'age' , 'city'

print(' #4 ============= items() ============= ')
print(dic.items())                      # Returns a list containing a tuple for each key value pair like (name , Yasir)

print(' #5 ============= copy() ============= ')
print(dic.copy())                       # Return copy of the dictionary

print(' #6 ============= setdefault() ============= ')  # returns the value of the item with the specified key

print(dic.setdefault('course', 'python'))           # add new key 'course' and its value 'python' in dictionary

print(' #7 ============= fromkeys() ============= ')
print(dic.fromkeys("ab", 1))             # it will return new dictionary with the specified keys and value like,

print(' #8 ============= items() ============= ')
print(dic.pop('age'))               # Delete the required key data. it will delete 'age'


print(' #9 ============= popitem() ============= ')          # it will delete the last item
print("this is Original dictionary ", dic)                  # before the popitem
y = dic.popitem()
print('After using the popitem method', dic, ' delete this item',y)                  # after popitem


print(' #10 ============= update() ============= ')   # Updates the dictionary with the elements from another vales
print("this is Original dictionary ", dic)

y1 = dic.update(city='multan')              # it will update city to Multan
print("After update method ", dic)

print(' #11 ============= Clear() ============= ')  # it will delete the all items in dictionary
print(dic.clear())
