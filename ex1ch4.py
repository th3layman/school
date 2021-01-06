mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]

#Below are my guesses of the results of the expressions
#len(mylist) >>> 5 ; returns the length of the list as int
#mylist[2] >>> "Cairo" ; returns index position 2 starting from 0
#mylist[1:] >>> "Athens", "Barcelona" ; slices the list after index postion 1
#mylist[-1] >>> "Florence" ; index position 1 from last
#mylist.index("Cairo") >>> 2 ; index value of "Cairo"
#mylist.pop(1) >>> "Barcelona" similar to mylist[1]
#mylist.sort(reverse = True) >>> sorts mylist alphabetically.
#mylist.append("Berlin") >>> "Athens", "Barcelona", "Cairo",
#"Florence", "Helsinki", "Berlin" ; adds "Berlin" to the end of the list

#Below are the results of each expression

print( len(mylist))
print(mylist[2])
print(mylist[1:])
print(mylist.index("Cairo"))
print(mylist.pop(1))
print(mylist.sort(reverse = True))
print(mylist.append("Berlin"))
