def seq(x):
    step = 0
    while 1:
        if x != 1:
            step += 1
            if x % 2 == 0:
                print(x / 2, end="  ")
                x = x / 2
            else:
                print((3 * x) + 1, end="  ")
                x = (3 * x) + 1
        else:
            print("\n", step)
            break


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Enter a positive integer")
    else:
        seq(float(num))
