#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4
thistuple = ("apple",)
print(type(thistuple))

#5
thistuple = ("apple")
print(type(thistuple))

#6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#7
tuple1 = ("abc", 34, True, 40, "male")

#8
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#9
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#10
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#11
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#12
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)