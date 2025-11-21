students = ["Nozomi", "Haru", "Hoshino"]

for i in range(len(students)):
    print(i + 1, students[i])

students = [
    {"name": "Hermione", "House": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "House": "Syltherin", "patronus": None},
]

for student in students:
    print(student["name"], student["House"], student["patronus"], sep=", ")