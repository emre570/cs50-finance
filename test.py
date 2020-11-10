s = int(input())

student = list()
notes = list()

for i in range(s):
    name = input()
    student.append(name)
    score = float(input())
    notes.append(score)

classroom = list(zip(student, notes))
classroom.sort()

#print(student)
#print(notes)
#print(classroom[-1])
print(classroom[1][0])
