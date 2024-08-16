# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
text=""
for i in range(5):
    n=input("Enter your numer: ")
    text+=str(n)
    max=text
    min=text
    for i in range(len(text)):
        if text[i]>max:
            max=text[i]
        else:
            max[i]
print("max ", max)
print("min ", min)