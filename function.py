def func1():
    print("func1")

func1()

def func2(name, age):
    print(name + " " + str(age))

func2("Jack", 23)

# function modify list
def func3(name, assets):
    print(name)
    assets.append("car")
    assets.append("house")

assets = []
func3("Mike", assets)
print(assets)

# function not modify list
def func4(fruits):
    fruits.append("apple")
    fruits.append("banana")
    print(fruits)

fruits = ["pear"]
func4(fruits[:])
print(fruits)

# function tumple
def func5(name, *others):
    print(name)
    print(others)

func5("Amy", "1", "2")

# function dict
def func6(name, **dt):
    print(name)
    print(dt)

func6("Lisa", age=30, score=45)

from test_module import hello as tm_hello, hi as tm_hi

tm_hello()
tm_hi()
