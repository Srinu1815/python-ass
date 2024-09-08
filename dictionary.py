students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
print("Initial dictionary:", students)


students[106] = "Frank"
print("Dictionary after adding a value:", students)


students[102] = "Ben"
print("Dictionary after updating a value:", students)


student_name = students[103]
print("Accessed value for Student ID 103:", student_name)


nested_students = {
    101: {"name": "Alice", "age": 20},
    102: {"name": "Ben", "age": 22},
    103: {"name": "Charlie", "age": 19},
    104: {"name": "David", "age": 21},
    105: {"name": "Eve", "age": 20}
}
print("Nested dictionary:", nested_students)


charlie_age = nested_students[103]["age"]
print("Accessed age for Charlie:", charlie_age)



keys = students.keys()
print("Keys in the dictionary:", list(keys))



del students[104]
print("Dictionary after deleting a value:", students)
