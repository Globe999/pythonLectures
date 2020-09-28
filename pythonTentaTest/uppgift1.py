def movieTickets():
    numOfTickets = int(input("Hur många biljetter vill du köpa?"))
    underEighteen = int(input("Hur mårnga är under 18?"))
    showTime = int(input("Vilken tid vill ni se på filmen? (Hela timslag)"))
    discount = 1
    if showTime < 18:
        discount = 0.9

    price = int((numOfTickets * 100 - underEighteen * 50) * discount)
    return print("Biljetterna kostar sammanlagt " + str(price) + " kr.")

def main():
    movieTickets()