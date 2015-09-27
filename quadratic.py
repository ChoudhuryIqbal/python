#quadratic py
# a program that computes the real roots of a quadratic equation

import math
def main():
    print("This program finds the real solution to a quadratic")
    print()

    a,b,c=eval(input ("please enter the cooficient:" ))


    discRoot=math.sqrt(b*b-4*a*c)
    root1=(-b+discRoot)/(2*a)
    root2=(-b-discRoot)/2*a
    print()
    pritn("The solution s are", root1, root2)
main()
               
