#Variable to store user input
strTxt = input("Enter a string: ")
#Variable to store the user input in lowercase
strTxtLower = strTxt.lower()
#Variable to count the vowels
vowelCount = 0
#Loop to traverse the text string
for c in strTxtLower:
    #Condition to update the value of vowelCount
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        vowelCount += 1
#Display the number of vowels       
print(f"The number of vowels in the string is: {vowelCount}")

#Pushed to Wk10ex3 GitHub repo.
