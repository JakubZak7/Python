def f(arr):
    number = arr[0]

    for index in range(0,len(arr)):
        if number != arr[index]:
            return arr[index]

    return None


if __name__ == '__main__':
    print(f([7,7,7,7,7,5,7,7]))
    print(f([7,7,7,7,7,7,7,5]))
    print(f([7,7,7,7,7,7,7]))
