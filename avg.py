# avg2.py
#   A simple program to average two exam scores  
#   Illustrates use of multiple input
#Modify the avg2.py program (Section 2.5.3 from the book and from the book's webpage) to find the average of three exam scores.

def main():
    print("This program computes the average of three exam scores.")

    score1, score2,score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2+score3) / 3

    print("The average of the scores is:", average)

main()

