import queue

binaryStack = queue.LifoQueue()

naturalnumber = 18
naturalnumbercopy = 18
binary = ""

while naturalnumber > 0:
    Remainder = int(naturalnumber % 2)
    binaryStack.put(Remainder)
    naturalnumber //= 2
    
while not binaryStack.empty():
    binary += str(binaryStack.get())
    
print(f"Natural number: {naturalnumbercopy}")
print(f"Binary number: {binary}")
