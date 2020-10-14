def main():
    minGrade = 10
    grade = int(input("How many points did you get on the exams?"))

    if grade < minGrade:
        return print("Sorry, you did not pass the exam.")

    bonusPoints = int(input("How many bonus points did you get from exercises?"))
    grade += bonusPoints
    if grade < 17:
        return print("Your grade is 3")
    elif grade < 24:
        return print("Your grade is 4")
    else:
        return print("Your grade is 5")

main()