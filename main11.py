# names  = ["Bat", "Bob", "Josh", "Don", "David"]
# user = input("name:")
# while True:
#     for name in names:
#         if name == user:
#             print("Found:", name)
#             break
#     else:
#         print("Not in the list")
#     break

# while True:
#     a = input("Enter a word:")
#     if a == "quit":
#         print("Goodbye")
#         break
#     else:
#         print(a.upper())
    


# a = 0

# while a <= 29:
    
#     a += 1
#     if a % 3 == 0:
#        continue 
#     else:
#         print(a)

nums = []

while len(nums) < 5:
    a = int(input("enter numbers:"))
 
    if a <= 0:
        print("invalid! Try again")
    else:
        nums.append(a)

    
    
print(sum(nums))