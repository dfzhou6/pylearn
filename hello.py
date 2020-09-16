print("message")

# upper lower
print("upper".upper())
print("lower".lower())

# strip
print(" strip ".strip())

# LF
print("this\nis\nLF")

# string concat
print("a" + "b")

# " '
print("i'm human, this is \"love song\"")

# +-*/
print(10**3)
print(10/3)
print(10*1.0/4)

# string int concat
print("there are " + str(23) + " duck")

# list
list1 = ["a", "b", "c"]
print(list1[1])
print(list1[-3])

# list insert remove append pop del
# remove only del one element
names = ["Jack", "Mike", "Amy"]
names.append("Rose")
print(names)
names.insert(1, "Dick")
print(names)
names.remove("Rose")
print(names)
name = names.pop()
print(name)
print(names)
name = names.pop(1)
print(name)
print(names)
del names[0]
print(names)
elements = ["a", "a", "c"]
elements.remove("a")
print(elements)

# list sort reverse sorted len
cars = ["lambol", "farrari", "benz"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

al = ["c", "a", "b"]
print(sorted(al))
print(sorted(al, reverse=True))
print(al)
al.reverse()
print(al)
print(len(al))

# list foreach range
# range last element is not access
for num in range(2, 11, 2):
    print(num)

nums = [num**2 for num in range(1, 10)]
print(nums)

# list splice copy
# not include last element
als = ['a', 'b', 'c', 'd', 'e']
print(als[1:3])
print(als)
als_cp = als
als_cp.append('f')
print(als)
print(als_cp)
als_cp_real = als[:]
als_cp_real.append('wwww')
print(als)
print(als_cp_real)

# tumple
# element not modify, and other function is same to list
t1 = ("a", "b", "c")
print(t1[1])
t1 = ("dddd", "deeee")
print(t1)


# list in, not in, empty
toys = ["bear", "car", "ball"]
print("bear" in toys)
print("apple" not in toys)

empty_list = []
if empty_list:
    print(empty_list)
else:
    print("empty list")

# string lower upper strip in
# not change string itself
stra = " a "
strb = stra
strb.upper()
print(stra)
print(strb)
print(stra.strip())
print(stra)
strc = "1234567"
print("23" in strc)


# dict del in for keys values set
dt = {"name": "zdf", "age": 23}
for key, value in dt.items():
    print(key + " " + str(value))

for key in sorted(dt.keys()):
    print(key)

for value in set(dt.values()):
    print(value)

del dt["name"]
print(dt)
print("age" in dt)