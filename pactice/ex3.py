# Ex3 - String
# Enter text and check if it contains capital letter or not
text = input("Enter your text: ")
number = False
for i in range(len(text)):
    if text[i]==text[i].upper():
        number = True
if number:
    print("Has!")
else:
    print("No")