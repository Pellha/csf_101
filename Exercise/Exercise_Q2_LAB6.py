# To create a func in python, we use "def" keyword, followed by name 0f our func
def generate_right_triangle():
    # Prompting user for input
    height = int(input("Enter the height of the triangle (number of rows): "))
    
    # Generating right triangle pattern
    print("Right triangle pattern:")
    for i in range(1, height + 1):
        print('*' * i)

# Calling the function to generate right triangle pattern
generate_right_triangle()