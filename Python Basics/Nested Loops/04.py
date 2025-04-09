jury_number = int(input())
presentation = input()
total_grades = 0
total_sum_grades = 0

while presentation != 'Finish':
    presentation_grade = 0
    for _ in range(1, jury_number + 1):
        jury_evaluation = float(input())
        total_grades += 1
        presentation_grade += jury_evaluation
        total_sum_grades += jury_evaluation

    avg_presentation_grade = presentation_grade / jury_number
    print(f'{presentation} - {avg_presentation_grade:.2f}.')

    presentation = input()

avg_total = total_sum_grades / total_grades
print(f"Student's final assessment is {avg_total:.2f}.")


