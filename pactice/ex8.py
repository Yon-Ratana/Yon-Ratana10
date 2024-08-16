# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
number = "9394884039"
total =0
for i in range(len(number)):
    if number[i]=="8":
        total +=1
print(total)


# Q2 - What is first index of letter 8
number = "9394884039"
counter=0
for i in range (len(number)):
    if number[i] ==8:
        print(i)
