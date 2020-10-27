def calculate_loan():
    property_price = int(input("What's the property price?"))
    loan_size = int(input("What's the size of the loan? (In integers)"))
    rate = float(input("What's the interest?"))

    percentage = float(loan_size/property_price)
    #Per year
    amortization = 0
    interest = (loan_size*rate/100)
    if percentage >= 0.7:
        amortization = property_price * 0.02
    elif percentage >= 0.5:
        amortization = property_price * 0.01
    
    print("Per month")
    print("---------")
    print("Amortization: {}".format((amortization/12)))
    print("Interest: {}".format((interest/12)))
    print("Total: {}".format(((amortization/12) + (interest/12))))
calculate_loan()
