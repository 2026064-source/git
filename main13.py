student = {"name": "alice", "age": 19, "grade": "A"}
print(student)
print(student.items())
for key, value in student.items():
    print(f"{key}:{value}")

character = {"name": "Mendee", "health": 100, "level": 100, "weapon": "Axe"}
for key, value in character.items():
    print(value)
