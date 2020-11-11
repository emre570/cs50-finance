s = int(input())
students = []

for i in range(s):
    students.append([])
    for j in range(s):
        name = input()
        students.append(name)
        score = int(input())
        students.append(score)


print(students)
