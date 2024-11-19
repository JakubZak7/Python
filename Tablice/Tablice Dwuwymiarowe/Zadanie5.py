# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

rows = len(cinema_seats)
columns = len(cinema_seats[0])
   
def seats_total(seats):
   counter = 0
   for rowindex in range(0,rows):
       for columnIndex in range(0,columns):
           counter += 1
           
   return counter

def seats_available(seats):
   counterAvalible = 0
   for rowIndex in range(0,rows):
       for columnIndex in range(0,columns):
           if cinema_seats[rowIndex][columnIndex] == "A":
               counterAvalible += 1
   return counterAvalible

def seats_booked(seats):
   counterBooked = 0
   for rowIndex in range(0,rows):
       for columnIndex in range(0,columns):
           if cinema_seats[rowIndex][columnIndex] == "B":
                counterBooked += 1
   return counterBooked


def seat_status(seats, row, place):
   if seats[row-1][place-1] == "A":
       return "Avaliable"
   else:
       return "Not Avaliable"

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))