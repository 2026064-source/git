#While loop

# num = 1

# while num < 6:
#     print(num)
#     num = num + 1

# 2.break

# num = 1

# while num < 6:
#     print(num)

#     if num ==3:
#         break

#     num = num + 1


# num = 0

# while num < 6:
#     num = num + 1
    
#     if num ==3:
#         continue
#     print(num)

# while True:
#     a = input("choose:")

#     if a == 0:
#         break

# num = 1

# while num < 11 :
#     print(num)
#     num += 1

# num = 10
# while num > 0 :
#     print(num)
#     num -=1

# else:
#     print("yay")

# num = 0
# while num < 20:
#     num+=1
   
#     if num % 2 == 1:
#         continue
#     print(num)
   
# import random 
# num = random.randint(1,100)
# print(num)
# while True :
#     user = int(input('numbers:'))

#     if num == user:
#         break
#     elif num < user:
#         print("its too high")
#     elif num > user:
#         print("its too low")




pas = 1234
while True:
    user = int(input("password:"))
    if pas == user:
        print("correct")
        break
    