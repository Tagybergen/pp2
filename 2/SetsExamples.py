#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#7
set1 = {"abc", 34, True, 40, "male"}

#8
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#9
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#10
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#11
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#12
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#13
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#14
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#15
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#16
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#17
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#18
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#19
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#20
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#22
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)