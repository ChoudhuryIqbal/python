#Write a program that will print out a conversion table for dollars and another
#currency. The currency you should use is based on the first letter of your first name:

def main():
    print("Choudhury's converting program")
   
    print()
    print()
    print("Dollars :", "\t", "Euros:")
    for i in range(1,6):
        print(i,"\t",i*499.38)
main()
