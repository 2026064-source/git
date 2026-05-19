#Section 1 For loops
    
# for x in range(0,11):
#     print(x)


# fruits = ["apple", "banana", "mango", "grape", "kiwi"]

# for fruit in fruits:
#     print(fruit)

# for fruit in fruits:
#     if len(fruit) > 5:
#         print(fruit)


# numbers = [4,7,2,9,1,6,8,3]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)


#Section2 Functions

def greet():
    print("Hello, welcome")
greet()


def greet_user(name):
    print(f"Hello, {name}!") 
greet_user("Alise")


def add(a,b):
    print(f"Addition: {a+b}")
add(2,3)


def is_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(4)
is_even(7)
is_even(10)


