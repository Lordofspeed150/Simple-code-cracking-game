from random import randint
from time import sleep

ask2 = 0
while ask2.lower() != "yes":
    arr1 = [randint(1,9), randint(1,9), randint(1,9), randint(1,9)]
    arr2 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]
    arr3 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]
    arr4 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]

    print("""
        The following is a puzzle that you'll have to solve. 
        To do so,you must investigate the first row.
    """)
    sleep(3)
    print("The numbers under each top number have to be added together and multiplied by the top number.")
    sleep(2)
    print("If the answer is 0, don't write anything - Leave out any spaces. An example would be 2314, where column 1 i 23, column 2 is 0 (empty), column 3 is 1, etc.")
    sleep(2)

    print("",arr1,"\n",arr2,"\n",arr3,"\n",arr4)

    num1 = arr1[0] * (arr2[0] + arr3[0] + arr4[0])
    num2 = arr1[1] * (arr2[1] + arr3[1] + arr4[1])
    num3 = arr1[2] * (arr2[2] + arr3[2] + arr4[2])
    num4 = arr1[3] * (arr2[3] + arr3[3] + arr4[3])

    if num1 == 0:
        num1 = ""
    
    if num2 == 0:
        num2 = ""
    
    if num2 == 0:
        num2 = ""
    
    if num3 == 0:
        num3 = ""

    if num4 == 0:
        num4 = ""
    
    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    num4 = str(num4)
    
    answer = num1 + num2 + num3 + num4
    
    sleep(4)
    ask = input("Your answer: ")

    if ask == answer:
        print("Correct!")

    else:
        print(f"Wrong. Try again. The correct answer was {answer}")
    ask2 = input("""
    Would you like to do another puzzle? 'Yes' to do another, anything else to exit.
    - 
    """)
    if ask2.lower == "yes":
        continue
    else:
        exit()



    



