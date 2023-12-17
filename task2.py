#Palindrome Checker: Task 2
#This can be used to check for palindromes between a set of two numbers

print("How many palindromes are in this range? ")
user_input1 = input("start number: ")
user_input2 = input("end number: ")

count = 0
final_string = ""
var1 = int(user_input1) 
var2 = int(user_input2) 

for i in range(var1, var2):
    reverse_string = ""
    for j in str(i):
        reverse_string = j + reverse_string

    if(str(i) == reverse_string):
        final_string = final_string +  str(i) + " "
        count += 1

    i += 1

print("The number of palindromes between " + user_input1 +  " and " + user_input2 + " are: " + final_string)
