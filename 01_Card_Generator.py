import random

Card = int(input("Choose between Visa = [1] and Mastercard = [2] : \n"))

if Card == 1:
    number = [4]
if Card == 2:
    number = [5]

def luhn(all_values):
    values = []
    all_values = all_values[::-1]
    total = 0
    test = False
    while not test:
        for i in range(0, 15):
            random_values = random.randint(0, 9)
            values.append(random_values)
            all_values = number + values
            print(all_values)
            for x in range(len(all_values)):
                current_number = int(all_values[x])
                if (x % 2) != 0:
                    if (current_number * 2) > 9:
                        total += current_number * 2 - 9
                    else:
                        total += current_number * 2
                else:
                    total += current_number
            return total % 10 == 0
        if test:
            print(all_values)



