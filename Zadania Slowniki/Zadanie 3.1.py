import queue


liczby = queue.LifoQueue()

liczby.put(2)
liczby.put(3)
liczby.put(7)
liczby.put(4)
liczby.put(1)
liczby.put(9)
liczby.put(8)

print("Number of items on stack", liczby.qsize())

sum = 0

while liczby.qsize() > 5:
    liczba = liczby.get()
    sum += liczba
print(sum)

sumapozostala = 0
while not liczby.empty():
    liczba = liczby.get()
    sumapozostala += liczba
    
print(sumapozostala)





