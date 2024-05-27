# Exercise
# Question 1

# To create a func in python, we use "def" keyword, followed by name 0f our func
def generate_multiplication_table():
    number = int(input("Enter the number for which you want the multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table generated: "))
    
    # Generating multiplication table
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{number} * {i} = {number * i}")

# Calling the function to generate multiplication table
generate_multiplication_table()