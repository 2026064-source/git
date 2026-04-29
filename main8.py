items = ["a"]

def shorten_name(a,b):
   print(f"{a[0]}. {b}")

shorten_name("Ganbold","Erdene") 


def greet(name,greeting="Hello"):
   print(greeting,name)

greet("Bat")
greet("Bat","sain baina uu")


def get_lowest(nums):
    lowest = nums[0]
    for num in nums:
        if lowest>num:
            lowest=num
    print(lowest)
    

get_lowest([1,2,3,4, -6, 10])


def add_tax(price):
    return price * 1.10

def receipt(item,price):
    total = add_tax(price)
    print(f"Item: {item}, Total with tax: {total}")

receipt("Notebook", 5000)


def calculate(a, b):
    result = a + b
    print(result)
calculate(5, 5)


