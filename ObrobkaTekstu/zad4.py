FILE_PATH = "oceny.txt"

data = []


def avg(values):
    value_sum = 0
    value_count = len(values)

    for value in values:
        value_sum += int(value)

    value_avg = value_sum / value_count

    return value_avg


with open(FILE_PATH) as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace(' \n', '')
        line = line.replace('\n', '')
        record = line.split(" ")
        data.append(record)

allMathGrades = []

for record in data:
    if record[1] == "mat":
        grades = record[2:]
        for grade in grades:
            allMathGrades.append(int(grade))

globalMathGradeAvg = avg(allMathGrades)

names = []

for record in data:
    if record[1] == "mat":
        grades = record[2:]

        gradeAvg = avg(grades)

        if gradeAvg > globalMathGradeAvg:
            names.append(record[0])

print(names)
