# 2. Floating Prime
# Chayoot Sathanbua 6170503404 KMUTT.
# The Intership 2021
# for python 3 only, do not use version 2.

def testPrime(num):
  if num > 1:
   for i in range(2,num):
    if (num % i) == 0:
      return False
   else:
    return True
  else:
    return False

def main():
  _input = ""
  print("")
  while (True):
    _input = input("Enter floating number to test a prime number: ")
    if(_input == "0.0"):
      break
    count = 0
    for c in _input:
      if(c == 0):
        count = count+1
      if(count > 1):
        break
    if(count > 1):
      print("Invalid format.")
    else:
      testFloat = float(_input)
      if(testFloat < 1 and testFloat > 10):
        print("Please enter a floating number in range [1.00 - 10.00]")
      else:
        floatString = str(testFloat)
        testPrimeString = ""
        count1 = 0
        afterDot = False
        for c in floatString:
          if(c != "."):
            if(afterDot):
              count1 = count1 + 1
            testPrimeString = testPrimeString + c
            if(testPrime(int(testPrimeString))):
              print("TRUE")
              break
          else:
            afterDot = True
          if(count1 == 3):
            print("FALSE")
            break
  print("")

main()

  