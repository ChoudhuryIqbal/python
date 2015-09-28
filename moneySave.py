# Doublefactorial.py
#    Program to compute the couble factorial of a number
#    Illustrates for loop with an accumulator

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-2):
        fact = fact * factor
    print("The double factorial of", n, "is", fact)

main()
