from random import randint
from time import sleep

arr1 = [randint(1,9), randint(1,9), randint(1,9), randint(1,9)]
arr2 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]
arr3 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]
arr4 = [randint(0,1), randint(0,1), randint(0,1), randint(0,1)]

def _sum(a):

    sum = 0

    for i in a:
        sum = sum + i

    return(sum)

print("The following a puzzle that you'll have to solve. to do so,\n you must investigate the first row.")
sleep(3)
print("the numbers under each top number have to be added together and multiplied by the top number.")
sleep(2)
print("if the answer is 0, write nothing for that. do not make spaces. an example would be 2314.")
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
    print("correct!")

else:
    print("wrong. try again. the correct answer was ", answer)




    



