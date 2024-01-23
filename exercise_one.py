# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def calculate(first_number,second_number):
    # Calculate product
    product = first_number * second_number
    # Calculate sum
    sum = first_number + second_number
    # Check if product is equal to or lower than 1000. 
    if product <= 1000:
        return product
    else:
        return sum

# First pair of numbers

first_number = 20
second_number = 30
result = calculate (first_number, second_number)
print ("The result is", result)

# Second pair of numbers

first_number = 40
second_number = 30
result = calculate (first_number,second_number)
print ("The result is", result)

