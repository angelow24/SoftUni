movie = input()
total_seats_booked = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie != "Finish":
    seats_left = int(input())
    seats_booked_movie = 0

    ticket_type = input()  # student, standard, kid
    while ticket_type != 'End':

        if ticket_type == 'student':
            total_seats_booked += 1
            seats_booked_movie += 1
            student_tickets += 1
        elif ticket_type == 'standard':
            total_seats_booked += 1
            seats_booked_movie += 1
            standard_tickets += 1
        elif ticket_type == 'kid':
            total_seats_booked += 1
            seats_booked_movie += 1
            kids_tickets += 1

        if seats_left == seats_booked_movie:
            break

        ticket_type = input()

    percentage_booked = (seats_booked_movie / seats_left) * 100
    print(f'{movie} - {percentage_booked:.2f}% full.')

    movie = input()

per_student_tickets = (student_tickets / total_seats_booked) * 100
per_standard_tickets = (standard_tickets / total_seats_booked) * 100
per_kids_tickets = (kids_tickets / total_seats_booked) * 100

print(f'Total tickets: {total_seats_booked}')
print(f'{per_student_tickets:.2f}% student tickets.')
print(f'{per_standard_tickets:.2f}% standard tickets.')
print(f'{per_kids_tickets:.2f}% kids tickets.')
