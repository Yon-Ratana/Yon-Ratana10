# Ex4 - String 
# ----------------Ex4 - String -------
# Q1 - display number 1 by one without space

text = "3 4 5 6"
for i in text:
    if i!=" ":
        print(i)

# Q2 - Sum all number (Total: 18)
text = input("Enter your number : ")
y = 0 
n = " "
for i in range(len(text)) :
    if text[i] == " ":
        n+= ""
    else: 
        n += text[i]
        y += int(text[i])
print("Total :", y)
