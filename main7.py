# def square(a):
#     return(a*a)
# result=square(5)
# print(result)


# def full_name(first,last):
#     return first + " " + last


# print(full_name("Enkhjin","Buyanjargal"))



# def celsius_to_fahrenheitto(c):
#     return (c * 9/5) + 32
# print(celsius_to_fahrenheitto(0))



# def is_even(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False
    
# b = int(input("number:"))

# print(is_even(b))

def calculate_grade(i):

    if i>=90:
        return('A')
    elif i>=80 and i<=89:
        return("B")
    elif i>=70 and i<=79:
        return("C")
    else:
       return("F") 

print(calculate_grade(89))


def classify_temp(c):                 
    if c <= 0:
        return("freezing")
    elif c>0 and c<=15:
        return("cold")
    elif c>=16 and c<=30:
        return("warm")
    elif c>30:
        return("hot")

a = int(input("What's the temp? "))

print(classify_temp(a))
# a = classify_temp(56)
# b = classify_temp(-100)
# d = classify_temp(16)
# e = classify_temp(100)

# print(a,b,d,e)
