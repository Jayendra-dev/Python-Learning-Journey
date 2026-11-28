# 8. How can you check if a number is divisible by both 3 and 5 using the modulus operator?
number=int(input("enter number :"))
if(number%3==0 and  number %5==0 ):
    print("number is divisible by both 3 and 5")
else:
    print ("number is not divisible by  both 3 and 5")

