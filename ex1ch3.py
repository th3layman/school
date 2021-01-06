mylist = [3, 5, 6, 7, 68, 293, 0, 234, 3, 5, 12, 9, 3, 334, 5, 6]
length = len(mylist)
count = mylist.count(0)
if length == count:
    print("The provided list does not duplicate values")
else:
    print("The provided list contains"
          " duplicate values")
