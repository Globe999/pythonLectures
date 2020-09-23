import sys

def hSum(num_terms):
      
  result = 0
  for n in range(num_terms+1):
    #Skip if we're on 0 to avoid division w/ 0
    if n == 0:
      continue
    result += (1/n)
  return result

def main(num):
  for i in range (0, num):
    print(str(i) + " " + str(hSum(i)))

main(int(sys.argv[1]))
