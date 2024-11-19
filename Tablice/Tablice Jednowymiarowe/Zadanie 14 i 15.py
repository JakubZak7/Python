###
# Bubble sort
#
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temporary = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temporary
    
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)