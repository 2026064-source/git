# num = int(input("number?")) 

# while num >= 0:
#     print(num)
#     num -= 1

# total = 0

# while True:
#     num = int(input("number:"))
#     if num == 0:
#         break 
#     else:
#         total += num

# print(f"Total sum: {total}")
# password = "programming1"

# while True:
#     a = input("Enter password:")
#     if a == password:
#         print("Access granted")
#         break
#     else:
#         print("Wrong. Try again.")



# num = int(input("Number:"))

# a = 1
# while a <=10:
#     print(num, "x", a ,'=', num * a)
#     a+=1

user = int(input("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Quit\nChoice:"))
while True:
    if user == 5:
        break

    a = int(input("1 number:"))
    b = int(input("2 number:"))

    if user == 1:
        print(a+b)
        break
    elif user == 2:
        print(a-b)
        break
    elif user == 3:
        print(a*b)
        break
    elif user == 4:
        print(a/b)
        break
    



      

