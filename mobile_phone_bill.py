plan = input("Which package did you purchase? A, B or C?")

minutes = int(input("How many minutes were used?"))

if (plan == "A" or plan == "a"):
    if (minutes <= 450):
        print("Total cost: $", 39.99)
    else:
        total = (minutes - 450) * 0.45 + 39.99
        print("Total cost: $", total)

if (plan == "B" or plan == "b"):
    if (minutes <= 900):
        print("Total cost: $", 59.99)
    else:
        total = (minutes - 900) * 0.40 + 59.99
        print("Total cost: $", total)

if (plan == "C" or plan == "c"):
    print("Total cost: $69.99")