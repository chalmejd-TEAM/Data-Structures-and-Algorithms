def scream ():
    print('Ahhh')

user = {
    'age': 54,
    'name': 'John',
    'magic': True,
    'scream': scream 
}

print(user['age']) # Access value from dict
user['scream']() # Run function from dict
user['spell'] = 'abra kadabra' # Add key/value to dict
print(user)