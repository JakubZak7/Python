# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
rows = len(monthly_expenses)
colum = len(monthly_expenses[0])

totalcost = 0

for rowindex in range(0,rows):
    for columnindex in range(0,colum):
        totalcost += monthly_expenses[rowindex][columnindex]
        
foodcost = 0 

for rowindex in range(0,rows):
    foodcost += monthly_expenses[rowindex][0]
    
transportcost = 0 

for rowindex in range(0,rows):
    transportcost += monthly_expenses[rowindex][1]

utilitescost = 0 

for rowindex in range(0,rows):
    utilitescost += monthly_expenses[rowindex][2]

week1 = 0 

for rowindex in range(1):
    for columnindex in range(0,colum):
        week1 += monthly_expenses[rowindex][columnindex]

week2 = 0 

for rowindex in range(1):
    for columnindex in range(0,colum):
        week2 += monthly_expenses[rowindex+1][columnindex]
        
week3 = 0 

for rowindex in range(1):
    for columnindex in range(0,colum):
        week3 += monthly_expenses[rowindex+2][columnindex]
        
week4 = 0 

for rowindex in range(1):
    for columnindex in range(0,colum):
        week4 += monthly_expenses[rowindex+3][columnindex]
        
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',foodcost)
print('Transport:',transportcost)
print('Utilities:',utilitescost)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:', totalcost)