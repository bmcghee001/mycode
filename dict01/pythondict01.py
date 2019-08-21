#!/usr/bin/env python3
print()
print()
## Create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print(switch['hostname'])

print(switch['ip'])

## request a 'fake' key
#print(switch['lynx'])

## request a 'fake' key with .get() method
print()
print("First test - .get()" )
print(switch.get('lvnx'))

print()
print("Second test - .get()" )
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print()
print("Third test - .get()" )
print(switch.get('version'))

print()
print ("Sixth test - .pop()")
switch.pop('version') #removes this key (and value) pair 
print(switch.keys()) #notice the value of version is gone
print(switch.values()) #notice the value 1.2

print()
print("Seventh test - ADD a new value")
switch['adminlogin'] = 'kar108'
print(switch.keys())
print(switch.values())

print()
print("Eight test - ADDa new value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())
print()
print()

