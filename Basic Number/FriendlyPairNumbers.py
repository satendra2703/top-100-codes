#The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.

def printDivisors(n, factors) :
    i = 1
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1 = int(input("Enter the first number: "))
  number2 = int(input("Enter the second number: "))
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")
