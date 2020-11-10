s = int(input())

student = list()
notes = list()
classroom = [student] + [notes]

for i in range(s):
    name = input()
    student.append(name)
    score = float(input())
    notes.append(score)

print(student)
print(notes)
print(classroom)
