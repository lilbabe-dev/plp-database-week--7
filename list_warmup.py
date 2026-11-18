# list_warmup.py

fruits = ["mango", "banana", "orange", "apple"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("pineapple")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

print("Number of fruits remaining:", len(fruits))