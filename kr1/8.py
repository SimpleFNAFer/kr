import random

SEAT_TAKEN = '*'
SEAT_AVAILABLE = '0'

ROWS = 10
SEATS_PER_ROW = 10

seat_state = (SEAT_TAKEN, SEAT_AVAILABLE)
seat_matrix = []

# Заполнение матрицы
for i in range(ROWS):
    seat_matrix.append([])
    for j in range(SEATS_PER_ROW):
        seat_matrix[i].append(random.choice(seat_state))

print("seat matrix:")
for i in range(ROWS):
    print(seat_matrix[i])

print('enter number of seats')
n = int(input())

if n <= 0:
    print("no seats required")
    exit(0)

available_seats = {}

for i in range(len(seat_matrix)):
    k = 0 # число свободных сидений подряд

    for j in range(len(seat_matrix[i])):
        if seat_matrix[i][j] == SEAT_TAKEN:
            k = 0
            continue

        k += 1
        if k >= n:
            available_seats_tuples = available_seats.get(i+1, [])
            available_seats_tuples.append((j+2-n, j+1))
            available_seats[i+1] = available_seats_tuples

if len(available_seats) == 0:
    print('no available seats')
    exit(0)

print('available seats:')
for k, v in available_seats.items():
    print(f"\trow {k}:")
    for i in range(len(v)):
        print(f"\t\tfrom {v[i][0]} to {v[i][1]}")
