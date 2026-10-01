#include <iostream>
print("================================\n"
      "         AREA OF SQUARE\n"
      "================================\n")
print("\nGive informations below and I'll show you the area of your square\n")
ln = input("Enter Length: ")
wd = input("Enter Width: ")
un = input("What unit? ")

print("\nResult:", int(ln)*int(wd), "square", un)
print("\n================================\n"
      "        PERIMETRE OF SQUARE\n"
        "================================\n")
print("\nGive informations below and I'll show you the perimetre of your square\n")
dor = input("Enter Length: ")
pro = input("Enter Width: ")
uni = input("What unit? ")

print("\nPerimeter:", 2*(int(dor)+int(pro)), uni)
print("\n================================\n"
      "         AREA OF TRIANGLE\n"
      "================================\n")
print("\nGive informations below and I'll show you the area of your triangle\n")
bs = input("Enter Base Length: ")
lng = input("Enter Height: ")
unt = input("What unit? ")
print("\nResult:",  int(0.5*(int(bs)*int(lng))), "square", unt)