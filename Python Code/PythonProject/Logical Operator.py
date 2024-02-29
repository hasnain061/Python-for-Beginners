has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for Loan 1")
else:
    print("Not Eligible")

has_high_income = False
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for Loan 2")
else:
    print("Not Eligible")

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for Loan 3")
else:
    print("Not Eligible")

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for Loan 4")
else:
    print("Not Eligible")
