#include <iostream>
#using namespace std;

print("================================\n"
      "         AREA OF SQUARE\n"
      "================================\n")
#Loop
print("\nGive informations below and I'll show you the area of your square\n")
while True:
	ln = input("Enter Length: ")
	wd = input("Enter Width: ")
	un = input("What unit? ")
	if float(ln) < float(wd):
		print("\nWidth can't be greater than Length!\nPlease enter again\n")
		continue
		
	print("\nResult:", float(float(ln)*float(wd)), "square", un)
	break
#Loop ended
print("\n================================\n"
      "      PERIMETRE OF SQUARE\n"
        "================================\n")
print("\nGive informations below and I'll show you the perimetre of your square\n")
dor = input("Enter Length: ")
pro = input("Enter Width: ")
uni = input("What unit? ")

print("\nPerimeter:", float(2*(float(dor)+float(pro))), uni)
print("\n================================\n"
        "        AREA OF TRIANGLE\n"
        "================================\n")
print("\nGive informations below and I'll show you the area of your triangle\n")
bs = input("Enter Base Length: ")
lng = input("Enter Height: ")
unt = input("What unit? ")
print("\nResult:",  float(0.5*(float(bs)*float(lng))), "square", unt)
print("\n================================\n"
        "     AREA OF PARALLELOGRAM\n"
        "================================\n")
print("\nGive informations below and I'll show you the area of your triangle\n")
bss = input("Enter Base Length: ")
ht = input("Enter Height: ")
unit = input("What unit? ")
print("\nResult:",  float(bss)*float(ht), "square", unit)