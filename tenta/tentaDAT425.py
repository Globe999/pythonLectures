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

def code_words(text, dictionary):
    strList = text.split()
    newList = []
    for i in strList:
        if i in dictionary:
            newList.append(dictionary[i])
        else:
            newList.append(i)
    return " ".join(newList)


class Robot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.currentDirection = "NORTH"
        self.directions = ["NORTH","EAST","SOUTH","WEST"]
    def turnRight(self):
        i = self.directions.index(self.currentDirection)
        if i == 3:
            self.currentDirection = self.directions[0]
        else:
            self.currentDirection = self.directions[i+1]
    def turnLeft(self):
        i = self.directions.index(self.currentDirection)
        if i == 0:
            self.currentDirection = self.directions[-1]
        else:
            self.currentDirection = self.directions[i-1]
    def forward(self, n):
        if self.currentDirection == "NORTH":
            self.y += n
        elif self.currentDirection == "SOUTH":
            self.y -= n
        elif self.currentDirection == "EAST":
            self.x += n
        elif self.currentDirection == "WEST":
            self.x -= n
