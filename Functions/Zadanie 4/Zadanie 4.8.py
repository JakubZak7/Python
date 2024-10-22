import time

def time_string(hour,minute,format):
    if format == '24':
        return(f"{hour}:{minute}")

    if format == '12':
        t = str(hour) + ':' + str(minute)
        t = time.strptime(t,"%H:%M")

        return time.strftime("%I:%M %p", t)


hour = int(input("Type hour: "))
minute = int(input("Type minute: "))
format = input("Type format (12/24 hours): ")
