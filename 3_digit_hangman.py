# 3. Digit Hangman
# Chayoot Sathanbua 6170503404 KMUTT.
# The Intership 2021
# for python 3 only, do not use version 2.

def main():
  print("")
  _input = input("Enter 12 digit number with space (x x x x ...)\n\t: ")
  cutSpace = _input.replace(" ","")
  if(cutSpace.isdigit != True):
    print("Not all input is digit!")
    return -1
  if(len(cutSpace) < 12 or len(cutSpace) > 12):
    print("Number is more than 12 digits or less than 12 digits!")
    return -1
  else:
    testGuess = []
    wrongGuess = []
    count = 0
    for i in range(12):
      testGuess.append(False)
    for i in range(5):
      _input1 = input("Geuss[" + str(i+1) +"]: ")
      if(_input1.isalpha()):
        print("Please enter only digit!")
        continue
      if(len(_input1) > 1):
        print("Please enter only 1 digit!")
        continue
      GuessValid = False
      for i in range(12):
        if(_input1 == cutSpace[i] and testGuess[i] == False):
          testGuess[i] = True
          count = count + 1
          GuessValid = True
        elif(i == 11 and GuessValid == False):
          wrongGuess.append(_input1)
      print("")
      for j in range(12):
        if(testGuess[j]):
          print(cutSpace[j],end=" ")
        else:
          print("_",end=" ")
      print(" - ",end="")
      for c in wrongGuess:
        print(c,end=" ")
      print("\n")
    print("\nTotal Score: " + str(count))
    print("Total Wrong: " + str(len(wrongGuess)))
  print("")
  return 0
main()