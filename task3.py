#Palindrome Checker: 3
#This can be used to suggest palindromes, if the user doesn't input a word that is already a palindrome

user_input = input("Please enter your number or phrase: ")
print("Checking...")

reverse_string = ""

for var in user_input:
    reverse_string = var + reverse_string

if(user_input == reverse_string):
    print(user_input + " is a palindrome.")

else:
    print(user_input + " is not a palindrome, but " + user_input+reverse_string + " is.")
