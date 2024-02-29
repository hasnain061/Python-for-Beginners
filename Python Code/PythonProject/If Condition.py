price = 10000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: {down_payment}")

n = int(input("Enter Number : "))

if (n % 2) == 0 or n < 20:
    print('Even')
else:
    print('Odd')