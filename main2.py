#for loop 

# movies = []

# movie = input("what's movie")

# movies.append(movie)

# print(movies)

stores = ["milk","bread"]

stores.append("butter")
stores.append("sugar")
stores.append("apple")
print(stores)

stores.remove("bread")
print(stores)

stores[2] = "brown sugar" # [2]- solih indexee bicne
print(stores)

stores.sort()
print(stores)

print(len(stores))


# grades = [85,90,65,72]
# print(grades)

# add = int(input("Add:"))
# grades.append(add)
# print(grades)
 
# delete = int(input("Remove:"))
# grades.remove(delete)
# print(grades)
  
change = int(input("Which number to change: "))

index = grades.index(change)
# print(index)

new_grade = int(input("What is the new grade?:"))

grades[index]=new_grade

print(grades)







# grades = input("what's change")
# grades = input("what's remove")

# print(grades)
# print(sum(grades))
# print(len(grades))
# average = sum(grades)/ len(grades)
# print(average)
