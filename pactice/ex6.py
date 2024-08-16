# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"
number=int(input("Enter Your number:  "))
for i in range(len(number)):
# i=0
    if i % 2==1:
        print("odd")
    else:
        print("Even")