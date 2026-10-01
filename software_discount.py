units = int(input("How many units are being purchased?"))

if (units >= 100):
    discount = units * 99 * 0.5
    final = (units * 99) - discount
    print("Your total is $", final)
elif (units >= 50):
    discount = units * 99 * 0.4
    final = (units * 99) - discount
    print("Your total is $", final)
elif (units >= 20):
    discount = units * 99 * 0.3
    final = (units * 99) - discount
    print("Your total is $", final)
elif (units >= 10):
    discount = units * 99 * 0.2
    final = (units * 99) - discount
    print("Your total is $", final)
else:
    print("Your total is $", units * 99)
