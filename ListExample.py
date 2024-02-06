#1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5
list1 = ["abc", 34, True, 40, "male"]

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7
thislist = list(("apple", "banana", "cherry")) 
print(thislist)

#8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#25
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#26
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#27
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#28
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#29
thislist = ["apple", "banana", "cherry"]
del thislist

#30
thislist = ["apple", "banana", "cherry"]
thislist