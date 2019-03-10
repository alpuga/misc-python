lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(nums):
    total = sum(nums)
    total = float(total)
    result = total / len(nums)
    return result


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    weight_hw = homework * .1
    weight_quiz = quizzes * .3
    weight_test = tests * .6
    sum = weight_hw + weight_quiz + weight_test
    return sum


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)


students = [alice, lloyd, tyler]


print(get_letter_grade(get_class_average(students)))
