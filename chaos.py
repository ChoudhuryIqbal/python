# File: chaos.py
# A simple program illustrating chaotic behavior.
#question:Modify the chaos program (available from the author's website) so that it prints out 15 values instead of 10.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(15):
        x = 3.9 * x * (1 - x)
        print(x)

main()
