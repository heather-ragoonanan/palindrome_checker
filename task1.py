#Palindrome Checker: Task 1
#This can be used to check if a word is a palindrome or not

user_input = input("Please enter your number or phrase: ")
print("Checking...")

reverse_string = ""
for var in user_input:
    reverse_string = var + reverse_string

#print(reverse_string)

if(user_input == reverse_string):
    print(user_input + " is a palindrome.")

else:
    print(user_input + " is not a palindrome.")
