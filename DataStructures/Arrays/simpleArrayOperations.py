strings = ['a', 'b', 'c', 'd']
# 32 bit system: 4 items * 4 bytes = 16 bytes of memory

# Lookup
print(strings[2]) # O(1), looks up item at specified index

# Push/Append
strings.append('e') # O(1), adds item to end of list
print(strings)

# Pop
strings.pop() # O(1), removes last item
print(strings)

strings.pop(1)
print(strings) # O(n), removes item at specified index

# Unshift (JavaScript)
# strings.unshift('x') <-- Adds 'x' to beginning of array, O(n)

# Splice (JavaScript)
# strings.splice(2, 0, 'alien') <-- Goes to an index of 2, removes 0 elements, and adds the string 'alien', O(n)

# Insert
strings.insert(2, 'y') # O(n), inserts item at specified index
print(strings)

# Delete/Remove
strings.remove('c') # O(n), removes specified item from array
print(strings)