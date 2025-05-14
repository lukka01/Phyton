#Task 1
# finding minimal number value in Dictionary

def min_value (dict):
    minVal = None
    for value in dict.values():
        if isinstance(value, (int, float)):
            if minVal is None or value < minVal:
                minVal = value
    print("The minimal value is:", minVal)
    return minVal



myDict = {
    "name" : "Alejandro",
    "lastName" : "Sosa",
    "Age" : 34,
    "Residence" : "Mexico",
    "birth_year" : 1988,
    "ID" : 114
}

min_value(myDict)

#Task 2 (finding the factorial of number recursively)


def factorial (n):
     if n < 1: print("Illegal value!")
     if n == 0 or n == 1: return 1
     return n * factorial(n-1)

print(factorial(5))












