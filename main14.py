# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 72},
#     {"name": "Charlie", "score": 91}
# ]

# print(students[0]["name"], students[1]["name"])
# print(students[2]["score"])
# students[1]["score"] = 100
# print(students[1]["score"])

# students[1]["grade"] = "A"
# print(students[1])
# print(students[2])

#access
# print(students[0]["name"]) #print(students[0]["name"],students[1]["score"])
# print(students[1]["score"])

# students[0]["score"] = 90
# students[0]["score"]+=5

# print(students[0]["score"])


# students = {"name": "Alise", "score": 85}

# print(students["name"])



# movies = [
#     {"title": "Inception", "rating": 8.8},
#     {"title": "Interstellar", "rating": 8.6},
#     {"title": "The Dark Knight", "rating": 9.0}
# ]

# print(movies[0]["title"])
# print(movies[1]["rating"])
# movies[2]["rating"] = 9.5
# print(movies[2]["rating"])
# movies[0]["watched"] = "True"
# print(movies[0])
# print(movies[1])



# countries = {"mongolia": 3_553_434,"Usa": 342_600_000, "Taiwan": 23_400_000, "Korea": 2_800_000, "British": 3_000_000}

# user = int(input("a minimum population:"))

# for i, j in countries.items():
#     if user < j:
#         print(i,j)



students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91}
]



for student in students:
    print(f"{student["name"]} scored {student["score"]}")
