# Functions 

def greet(): #Declare
    print("Hello world")

def goodbye():
    print("Goodbye")

goodbye()
greet() #Calling 


 
def introduce():
    print(f"Name:Enkhjin , age:20, email:ebbucgd@gmail.com")

def nums():
    for i in range(1,101):
        print(i)

nums()
introduce()

def greet(name, age, email):
    print("Hello", name, age, email)
   
    
greet("Bob", 25, "bob@gmail.com")
greet("Enkhjin", 20, "ejhue@gmail.com")


def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a//b)

add(3,5)  
subtract(6,7)
multiply(7,8) 
divide(8,4)

ingredients = ["coffee", "water", "milk"]
def display():
    for ingredient in ingredients:
        print(ingredient)
display()
display()
display()
display()
display()