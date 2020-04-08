number = 10
while True:
    try:
        i_num = int(input("Enter a number:"))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too Large, try again!")

print("Congratulations! You gussed it correctly.")