# list1 = [1,2, "nodar", True, 13]
#
#
# for i  in range (len(list1)):
#     print(list1[i])
#
# list1[1:3] = [False, False]
# print(list1)
#
# list2 = ["apple", "banana", "orange", "peach", "watermelon"]
#
# list3 = []
#
# for i in list2:
#     if "e" in i:
#         list3.append(i)
#
# print(list3)

# i = 0
# while i < len(list2):
#     print(list2[i])
#     i += 1


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)



# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[3:5])


# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1
#
#
# def changeTuple (myTuple ,index, val):
#     result = list(myTuple)
#     result[index] = val
#     return tuple(result)
#
# newTuple = changeTuple(thistuple, 3,"Yle")
# print(newTuple)


# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#
# x = thistuple.count(5)
#
# print(x)

# myset = {"apple", "banana", "cherry"}
# print(myset)
# print("apple" in myset)
#
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1 | set2
# print(set3)
#


# x = myDict["LastName"]
# print(x)
# myDict.get("Age")
#
# myDict.update({"Age" : 42})
# print(myDict.values())
#
# myDict["Residence"] = "Mexico"
# print(myDict)
#

newDict = {
    "Name" : "Alejandro",
    "lastName" : "Sosa",
    "Age" : 32

}
newDict.update({"Residence " : "Mexico"})

newDict.pop("Age")
print(newDict)

for i in  newDict.values():
    print(i)

for x,y in newDict.items():
    print(x,y)

myFamily = {
    "child1" : {
        "name" : "Nick",
        "Age" : 19
    },

    "child2" : {
        "name" : "George",
        "Age" : 14
    }
}

for x, obj in myFamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])






