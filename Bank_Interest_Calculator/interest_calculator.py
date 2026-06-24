running = True


def program(choice):
    years = int(input('How many years are you going to save? >> '))
    amount = int(input('How much are you saving yearly? >> '))
    r = input('What is the interest rate per year? (eg: 10, 0.1) >> ')
    try:
        rate = int(r)
    except ValueError:
        rate = float(r)
    new_amount = 0
    balance = 0
    total = 0
    interest = 0
    n = 0

    if choice.lower() == 'i':
        for i in range(0, int(years)):
            n += 1
            if type(rate) is float:
                interest += amount * rate
            elif type(rate) is int:
                interest += amount * (rate / 100)

            print(f"In year {n}, the interest earned will be ${interest}")
            total += interest
        print(f'By the end of year {n}, the total interest earned will be ${total}.')

    elif choice.lower() == 't':
        for i in range(0, int(years)):
            n += 1
            if type(rate) is float:
                if balance == 0:
                    interest = amount * rate
                    balance = amount + interest
                elif balance > 0:
                    old_balance = balance
                    interest = (old_balance + amount) * rate
                    balance = old_balance + amount + interest
            elif type(rate) is int:
                if balance == 0:
                    interest = amount * (rate / 100)
                    balance = amount + interest
                elif balance > 0:
                    old_balance = balance
                    interest = (old_balance + amount) * (rate / 100)
                    balance = old_balance + amount + interest

            print(f"In year {n}, your total balance will be ${round(balance, 2)}")
        print(f'By the end of year {n}, your total balance will be {round(balance, 2)}.')


while running:
    print(
        "How would you like to be calculated?\n'I' for total interest amount\n'T' for total balance including interest "
        "amount\n'E' to exit program")
    user_choice = input("Method >> ")
    if user_choice.lower() == 'e':
        running = False
    else:
        program(user_choice)
