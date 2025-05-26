def filter_students(students, min_grade):
    result = []

    for s, grades in students.items():
        if sum(grades)/len(grades) >= min_grade:
            result.append(s)

    return result


students = {
    's1': [3,4,5,4,4,3,4,5,5],
    's2': [4,5,4,5,4,5,5],
    's3': [3,4,3,4,3,4],
}
min_grade = 4

print(f'filtered students: {filter_students(students, min_grade)}')
