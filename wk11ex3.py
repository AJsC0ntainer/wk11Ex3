strTxt = input("Enter a string: ")
strTxtLower = strTxt.lower()
vowelCount = 0

for c in strTxtLower:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        vowelCount += 1
        
print(f"The number of vowels in the string is: {vowelCount}")