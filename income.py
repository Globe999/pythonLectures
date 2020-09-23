import matplotlib.pyplot as plt

def main():
  salary = int(input("Salary: "))
  taxrate = int(input("Tax rate: "))
  rent = int(input("Rent: "))
  tax = salary * taxrate/100
  net = salary - tax
  remains = net - rent
  print("Remains: ",remains)

  labels = 'tax', 'rent', 'remains'
  sizes = [int(tax),int(rent),int(remains)]
  colors = ['red','yellow','green']
  plt.pie(sizes,labels=labels,colors=colors)
  plt.show()                    
                
main()
