# Program to illustrate the use of 'is' identity operator

# Example 1: Comparing integers
a = 10
b = 10

if a is b:
    print("a and b refer to the same object")
else:
    print("a and b do not refer to the same object")

# Example 2: Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list2:
    print("list1 and list2 refer to the same object")
else:
    print("list1 and list2 do not refer to the same object")

# Example 3: Assigning one list to another
list3 = list1

if list1 is list3:
    print("list1 and list3 refer to the same object")
else:
    print("list1 and list3 do not refer to the same object")
