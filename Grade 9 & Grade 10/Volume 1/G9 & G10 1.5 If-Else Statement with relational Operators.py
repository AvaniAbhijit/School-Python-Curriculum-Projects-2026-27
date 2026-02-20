# Relational operators are used to compare two values.
# They always return True or False.
# We use them inside if statements to make decisions.

#   Operator		                Example	             Result
#   > (Greater than)	            80 > 50	              True
#   < (Less than)	                40 < 50	              True
#   >= (Greater than or equal)	    50 >= 50	          True
#   <= (Less than or equal)	        30 <= 50	          True
#   == (Equal to)	                10 == 10	          True
#   !=	(Not equal to)	            5 != 3	              True

# Task: Write a code to check user enter number that is even or Odd line 23 onwards.
#       Hint: num%2==0

marks = int(input("Marks: "))

if marks >= 50:        # >= is a relational operator, and if the condition is True, this block runs.
    print("Pass")
else:                  # If the condition is False → else block runs.
    print("Fail")





