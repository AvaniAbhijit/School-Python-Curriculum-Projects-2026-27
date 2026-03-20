# try block: 'Try to run this code; might cause an error.'
# except block: 'If an error happens, handle it.'
# Exception as e: 'Catch the error and store it in a variable called e.'

# Task 1: Enter input as 10 and 2. Run and observe the output
# Task 2: Enter input as 10 and 0. Run and observe the output
# Task 3: Enter input as "hello". What do you observe?
# Task 4: Uncomment lines 9, 16, and 17 and indent lines 10 to 14 inside the
#        try - except block. Do Task 2 and Task 3 again and observe the output.

#try :
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 / num2
print("Result is:", result)

#except Exception as e:
#    print(" Exception occured", e)
