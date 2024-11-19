arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

index = 0
rowIndex = 0
columnIndex = 0

while index < len(arr):
    arr[rowIndex][columnIndex] = 1
    rowIndex += 1
    columnIndex += 1
    index += 1
    
for row in arr:
    print(row)