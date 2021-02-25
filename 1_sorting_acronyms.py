# 1. Sorting Acronyms
# Chayoot Sathanbua 6170503404 KMUTT.
# The Intership 2021
# for python 3 only, do not use version 2.

print("")
line_toRead = input("Enter number of lines you want to sort\n\t: ")
lines = []
for i in range(int(line_toRead)):
  lines.append(input("line[" + str(i+1) + "]: "))
new_list = []
for _string in lines:
  if(any(letter.isupper() for letter in _string)):
    new_list.append("".join([c for c in _string if c.isupper()]))
_sorted = sorted(new_list,key=lambda item: (-len(item), item))
print("\nSorted:")
for x in _sorted:
  print("\t"+x)
print("")
