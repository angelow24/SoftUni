total_students_participated = int(input())

grade_2 = 0
grade_3 = 0  # 3 - 3.99
grade_4 = 0  # 4 - 4.99
grade_5 = 0  # 5 - 5.99
average_grade = 0

for _ in range(total_students_participated):
    grade_received = float(input())
    if 2.00 <= grade_received <= 2.99:
        grade_2 += 1
        average_grade += grade_received
    elif 3.00 <= grade_received <= 3.99:
        grade_3 += 1
        average_grade += grade_received
    elif 4.00 <= grade_received <= 4.99:
        grade_4 += 1
        average_grade += grade_received
    elif 5.00 <= grade_received:
        grade_5 += 1
        average_grade += grade_received

average_2 = (grade_2 / total_students_participated) * 100
average_3 = (grade_3 / total_students_participated) * 100
average_4 = (grade_4 / total_students_participated) * 100
average_5 = (grade_5 / total_students_participated) * 100
average_grade = (average_grade / total_students_participated)

print(f'Top students: {average_5:.2f}%')
print(f'Between 4.00 and 4.99: {average_4:.2f}%')
print(f'Between 3.00 and 3.99: {average_3:.2f}%')
print(f'Fail: {average_2:.2f}%')
print(f'Average: {average_grade:.2f}')



